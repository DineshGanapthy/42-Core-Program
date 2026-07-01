import random
from collections import deque
from dataclasses import dataclass
from typing import Any, cast

# ==========================================
# 1. CONFIGURATION CLASSES & UTILITIES
# ==========================================

@dataclass
class MazeConfig:
    width: int
    height: int
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str
    perfect: bool


class ConfigReader:
    def __init__(self) -> None:
        self.data: dict[str, Any] = {}

    def read(self, filename: str) -> MazeConfig:
        self.data.clear()

        with open(filename, "r") as f:
            for line in f:
                line = line.strip()

                if not line or "=" not in line:
                    continue

                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip()

                if key in self.data:
                    raise ValueError(f"This key {key} already exists")

                parsed_value: Any

                if key in ("ENTRY", "EXIT"):
                    parts = value.split(",")
                    if len(parts) != 2:
                        raise ValueError(f"Invalid coordinate format for {key}: {value}")
                    try:
                        x, y = tuple(int(part.strip()) for part in parts)
                        parsed_value = (x, y)
                    except ValueError:
                        raise ValueError(f"Coordinates for {key} must be integers")

                elif value.lower() in ("true", "false"):
                    parsed_value = value.lower() == "true"

                elif value.lstrip("- ").isdigit():
                    parsed_value = int(value.lstrip("- "))

                else:
                    parsed_value = value

                self.data[key] = parsed_value

        self.validate()

        return MazeConfig(
            width=self.data["WIDTH"],
            height=self.data["HEIGHT"],
            entry=self.data["ENTRY"],
            exit=self.data["EXIT"],
            output_file=self.data["OUTPUT_FILE"],
            perfect=self.data["PERFECT"]
        )

    def in_bounds(self, coord: tuple[int, int]) -> bool:
        x, y = coord
        width = cast(int, self.data["WIDTH"])
        height = cast(int, self.data["HEIGHT"])
        return 0 <= x < width and 0 <= y < height

    def validate(self) -> None:
        required_data = {
            "WIDTH": int,
            "HEIGHT": int,
            "ENTRY": tuple,
            "EXIT": tuple,
            "OUTPUT_FILE": str,
            "PERFECT": bool
        }

        for key, expected_type in required_data.items():
            if key not in self.data:
                raise ValueError(f"Missing config data: {key}")

            if not isinstance(self.data[key], expected_type):
                raise TypeError(f"{key} should be {expected_type.__name__} type")

        if self.data["WIDTH"] < 2:
            raise ValueError("WIDTH must be at least 2")
        if self.data["HEIGHT"] < 2:
            raise ValueError("HEIGHT must be at least 2")

        for coord_key in ("ENTRY", "EXIT"):
            coord = self.data[coord_key]
            if not isinstance(coord, tuple):
                raise TypeError(f"{coord_key} should be a tuple")
            if len(coord) != 2:
                raise ValueError(f"{coord_key} should have only 2 coordinates")
            if not self.in_bounds(coord):
                raise ValueError(
                    f"{coord_key} {coord} is outside maze bounds "
                    f"(WIDTH={self.data['WIDTH']}, HEIGHT={self.data['HEIGHT']})"
                )

        if self.data["ENTRY"] == self.data["EXIT"]:
            raise ValueError("ENTRY and EXIT cannot be the same location")


# ==========================================
# 2. CORE MAZE ENGINE
# ==========================================

class Maze:
    def __init__(self, 
                 height: int, 
                 width: int, 
                 entry: tuple[int, int], 
                 exit: tuple[int, int]) -> None:
        self.height = height
        self.width = width
        self.entry = entry
        self.exit = exit

        self.grid_height = 2 * height + 1
        self.grid_width = 2 * width + 1

        # Initialize grid entirely with walls (1)
        self.grid: list[list[int]] = [[1 for _ in range(self.grid_width)] for _ in range(self.grid_height)]


# ==========================================
# 3. GENERATION & SOLVER ALGORITHMS
# ==========================================

def dfs_generator(maze: Maze) -> None:
    grid = maze.grid
    height = maze.grid_height
    width = maze.grid_width
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def dfs(x: int, y: int) -> None:
        grid[y][x] = 0
        for dx, dy in random.sample(directions, len(directions)):
            nx, ny = (x + dx * 2), (y + dy * 2)
            if (0 <= nx < width) and (0 <= ny < height) and grid[ny][nx] == 1:
                wall_x = x + dx
                wall_y = y + dy
                grid[wall_y][wall_x] = 0
                dfs(nx, ny)

    dfs(1, 1)


def apply_entry_exit(maze: Maze) -> None:
    grid = maze.grid
    height = maze.height
    width = maze.width
    x1, y1 = maze.entry
    x2, y2 = maze.exit

    # Standard path transformations
    entry_x, entry_y = (x1 * 2 + 1), (y1 * 2 + 1)
    exit_x, exit_y = (x2 * 2 + 1), (y2 * 2 + 1)

    grid[entry_y][entry_x] = 0
    grid[exit_y][exit_x] = 0

    # Open outer boundaries for entry point
    if x1 == 0:
        grid[entry_y][entry_x - 1] = 0
    elif x1 == width - 1:
        grid[entry_y][entry_x + 1] = 0
    elif y1 == 0:
        grid[entry_y - 1][entry_x] = 0
    elif y1 == height - 1:
        grid[entry_y + 1][entry_x] = 0

    # Open outer boundaries for exit point
    if x2 == 0:
        grid[exit_y][exit_x - 1] = 0
    elif x2 == width - 1:
        grid[exit_y][exit_x + 1] = 0
    elif y2 == 0:
        grid[exit_y - 1][exit_x] = 0
    elif y2 == height - 1:
        grid[exit_y + 1][exit_x] = 0


def check_open_areas(maze: Maze) -> bool:
    grid = maze.grid
    height = maze.grid_height
    width = maze.grid_width

    for y in range(0, height - 2):
        for x in range(0, width - 2):
            open_spaces = 0
            for dy in range(0, 3):
                for dx in range(0, 3):
                    if grid[y + dy][x + dx] == 0:
                        open_spaces += 1
            if open_spaces == 9:  # Invalid 3x3 layout
                return False
    return True


def break_walls(maze: Maze, logo_pos: list[tuple[int, int]]) -> None:
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    grid = maze.grid
    height = maze.grid_height
    width = maze.grid_width
    attempts = width * height

    while attempts > 0:
        attempts -= 1
        gx = random.randrange(1, width - 1, 2)
        gy = random.randrange(1, height - 1, 2)
        dx, dy = random.choice(directions)

        wall_x = gx + dx
        wall_y = gy + dy
        next_x = gx + (2 * dx)
        next_y = gy + (2 * dy)

        if logo_pos:
            if (wall_y, wall_x) in logo_pos or (next_y, next_x) in logo_pos:
                continue

        if not (0 <= next_y < height and 0 <= next_x < width and 
                0 <= wall_y < height and 0 <= wall_x < width):
            continue

        if grid[gy][gx] == 0 and grid[next_y][next_x] == 0 and grid[wall_y][wall_x] == 1:
            grid[wall_y][wall_x] = 0
            if not check_open_areas(maze):
                grid[wall_y][wall_x] = 1


def add_42_logo(maze: Maze) -> list[tuple[int, int]]:
    pattern = [
        [1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 1],
    ]
    pat_w = len(pattern[0])
    pat_h = len(pattern)

    grid = maze.grid
    grid_h = maze.grid_height
    grid_w = maze.grid_width

    if grid_w < (pat_w + 3) or grid_h < (pat_h + 3):
        return []

    center_y = grid_h // 2
    center_x = grid_w // 2

    start_y = center_y - (pat_h // 2)
    start_x = center_x - (pat_w // 2)

    logo_pos = []
    for y in range(pat_h):
        for x in range(pat_w):
            if pattern[y][x] == 1:
                gy = start_y + y
                gx = start_x + x
                grid[gy][gx] = 2  # Unique representation identifier for Logo walls
                logo_pos.append((gy, gx))
    return logo_pos


def bfs_solve_maze(maze: Maze) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    grid = maze.grid
    height = maze.grid_height
    width = maze.grid_width
    x1, y1 = maze.entry
    x2, y2 = maze.exit

    entry_x, entry_y = (x1 * 2 + 1), (y1 * 2 + 1)
    exit_x, exit_y = (x2 * 2 + 1), (y2 * 2 + 1)

    # Shift outer perimeter boundary adjustments for pathfinders
    if x1 == 0: entry_x -= 1
    elif x1 == width - 1: entry_x += 1
    elif y1 == 0: entry_y -= 1
    elif y1 == height - 1: entry_y += 1

    if x2 == 0: exit_x -= 1
    elif x2 == width - 1: exit_x += 1
    elif y2 == 0: exit_y -= 1
    elif y2 == height - 1: exit_y += 1

    queue = deque([(entry_x, entry_y)])
    visited = {(entry_x, entry_y)}
    explored = []
    parent = {}

    while queue:
        curr_x, curr_y = queue.popleft()
        explored.append((curr_x, curr_y))

        if (curr_x, curr_y) == (exit_x, exit_y):
            break

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = curr_x + dx, curr_y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if grid[ny][nx] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (curr_x, curr_y)
                    queue.append((nx, ny))

    path = []
    curr = (exit_x, exit_y)
    if curr in visited:
        while curr != (entry_x, entry_y):
            path.append(curr)
            curr = parent[curr]
        path.append((entry_x, entry_y))
        path.reverse()

    return path, explored


# ==========================================
# 4. MAZE GENERATION MANAGED WRAPPER
# ==========================================

class MazeGenerator:
    def __init__(self, 
                 height: int, 
                 width: int, 
                 entry: tuple[int, int], 
                 exit: tuple[int, int],
                 perfect: bool,
                 seed: int | None = None) -> None:
        self.height = height
        self.width = width
        self.entry = entry
        self.exit = exit
        self.perfect = perfect
        self.seed = seed
        self.maze: Maze | None = None
        self.path: list[tuple[int, int]] = []
        self.explored: list[tuple[int, int]] = []

    def create_maze(self) -> Maze:
        try:
            if self.seed is not None:
                random.seed(self.seed)

            max_attempts = 1000

            for _ in range(max_attempts):
                maze = Maze(self.height, self.width, self.entry, self.exit)
                dfs_generator(maze)
                apply_entry_exit(maze)

                if not check_open_areas(maze):
                    continue

                logo_pos = add_42_logo(maze)
                if not logo_pos:
                    print("The maze is not big enough to create the 42 logo in correct size")

                if not self.perfect:
                    break_walls(maze, logo_pos)

                path, explored = bfs_solve_maze(maze)
                if path:
                    self.maze = maze
                    self.path = path
                    self.explored = explored
                    return maze

            raise ValueError("generate_maze(): Could not generate a valid maze")
        except Exception as e:
            raise ValueError(f"generate_maze(): {e}")

    def solve(self, algorithm: str) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        if algorithm == "bfs":
            path, explored = bfs_solve_maze(self.maze)
            self.path = path
            self.explored = explored
            return path, explored
        else:
            raise ValueError("solve(): No algorithm found with that name.")


# ==========================================
# 5. VISUAL TESTING HELPER
# ==========================================

def print_maze_with_path(maze: Maze, path: list[tuple[int, int]]) -> None:
    path_set = set(path)
    for y in range(maze.grid_height):
        row_str = ""
        for x in range(maze.grid_width):
            if (x, y) in path_set:
                row_str += "· "  # Dynamic shortest solution path
            elif maze.grid[y][x] == 1:
                row_str += "██"  # Solid interior wall
            elif maze.grid[y][x] == 2:
                row_str += "▒▒"  # 42 Logo wall elements
            else:
                row_str += "  "  # Empty walkable passage
        print(row_str)


# ==========================================
# 6. RUNTIME APPLICATION ENTRYPOINT
# ==========================================

def main() -> None:
    try:
        # Load and validate settings using ConfigReader
        reader = ConfigReader()
        config = reader.read("config.txt")

        print("===== CONFIG LOADED & VALIDATED =====")
        print(f"Width:       {config.width}")
        print(f"Height:      {config.height}")
        print(f"Entry Point: {config.entry}")
        print(f"Exit Point:  {config.exit}")
        print(f"Is Perfect:  {config.perfect}")
        print(f"Save Path:   {config.output_file}\n")

        # Set up Generator instance
        generator = MazeGenerator(
            height=config.height, 
            width=config.width, 
            entry=config.entry, 
            exit=config.exit, 
            perfect=config.perfect,
            seed=None  # Changes every execution
        )

        print("Generating maze...")
        maze = generator.create_maze()

        print("\nMaze with Solution Path:")
        print_maze_with_path(maze, generator.path)

        # Output representation to target file destination if configured
        if config.output_file:
            with open(config.output_file, "w") as f:
                for y in range(maze.grid_height):
                    row_str = ""
                    for x in range(maze.grid_width):
                        if (x, y) in set(generator.path):
                            row_str += "· "
                        elif maze.grid[y][x] == 1:
                            row_str += "██"
                        elif maze.grid[y][x] == 2:
                            row_str += "▒▒"
                        else:
                            row_str += "  "
                    f.write(row_str + "\n")
            print(f"\nMaze saved to '{config.output_file}'")

    except Exception as e:
        print(f"An execution error occurred: {e}")


if __name__ == "__main__":
    main()