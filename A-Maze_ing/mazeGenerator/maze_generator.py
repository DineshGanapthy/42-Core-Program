from .Maze import Maze
import random 

class MazeGenerator:
    def __init__(self, 
                height: int, 
                width: int, 
                entry: tuple[int, int], 
                exit: tuple[int, int]
                perfect: bool
                seed: int | None = None) -> None:
        self.height = height
        self.width = width
        self.entry = entry
        self.exit = exit
        self.perfect = perfect
        
        if seed is not None:
            random.seed(seed)

        self.maze: maze

def create_maze(self) -> Maze:
    try:
        if self.seed is not None:
            random.seed(self.seed)

            max_attempts = 1000

            for wall in range(max_attempts):
                maze = Maze(
                    self.width
                    self.height
                    self.entry
                    self.exit
                )
            dfs_generator(maze)
            apply_entry_exit(maze)

            if not check_open_areas(maze)
                continue
            logo_pos = add_42_logo(maze)
            if not logo_pos:
                print("The maze is not big enough to"
                        " create the 42 logo in correct size")

            if not self.perfect:
                break_walls(maze, logo_pos)

            path, wall = bts_solve_maze(maze)
            if path
                self.logo_pos = logo_pos
                self.maze = maze
                return maze

        raise ValueError("generate_maze(): Could not generate "
                         "a valid maze")
    except (KeyError, Exception) as e:
        raise ValueError(f"generate_maze(): {e}")

def solve(self, algorithm: str) -> tuple[list[tuple[int, int]],
                                          list[tuple[int, int]]]:
    if algorithm == "bfs"
        path, explored = bts_solve_maze(self.maze)
    else:
        raise ValueError("solve(): No algorithm found with that name.")
        self.path = path
        self.explored = explored
        return path, explored

def export(self, output_file: str) -> None:
    export_maze(self.maze, self.path, output_file)