from typing import Any, cast, Final
from dataclasses import dataclass

WALL: Final[int] = 1
PATH: Final[int] = 0


class Maze():
    LOGO_42 = [
            "▇   ▇▇▇",
            "▇     ▇",
            "▇▇▇ ▇▇▇",
            "  ▇ ▇  ",
            "  ▇ ▇▇▇"
        ]

    def __init__(
            self,
            width: int,
            height: int,
            entry: tuple[int, int],
            exit: tuple[int, int]
    ) -> None:
        self.width: int = width
        self.height: int = height
        self.entry: tuple[int, int] = entry
        self.exit: tuple[int, int] = exit
        self.grid: list[list[int]] = [
            [WALL for _ in range(width)]
            for _ in range(height)
        ]

    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def is_wall(self, x: int, y: int) -> bool:
        return self.grid[y][x] == WALL

    def set_wall(self, x: int, y: int) -> None:
        self.grid[y][x] = WALL

    def set_path(self, x: int, y: int) -> None:
        self.grid[y][x] = PATH

    def get_cell(self, x: int, y: int) -> int:
        return self.grid[y][x]

    def neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        result: list[tuple[int, int]] = []

        #  up, right, down, left (x, y)
        directions = ((0, -1), (1, 0), (0, 1), (-1, 0))

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if self.in_bounds(nx, ny):
                result.append((nx, ny))

        return result

    def stamp_pattern(
            self, pattern: list[str], start_x: int, start_y: int
            ) -> None:
        for y, row in enumerate(pattern):
            for x, char in enumerate(row):
                px = start_x + x
                py = start_y + y

                if not self.in_bounds(px, py):
                    continue

                if char == "▇":
                    self.set_wall(px, py)
                else:
                    self.set_path(px, py)

    def logo_42(self) -> None:
        logo_height = len(self.LOGO_42)
        logo_width = len(self.LOGO_42[0])

        start_x = (self.width - logo_width) // 2
        start_y = (self.height - logo_height) // 2

        self.stamp_pattern(self.LOGO_42, start_x, start_y)

    def __str__(self) -> str:
        lines: list[str] = []

        for y, row in enumerate(self.grid):
            chars: list[str] = []

            for x, cell in enumerate(row):
                if (x, y) == self.entry:
                    chars.append("E")
                elif (x, y) == self.exit:
                    chars.append("X")
                elif cell == WALL:
                    chars.append("▇")
                else:
                    chars.append(" ")

            lines.append("".join(chars))

        return "\n".join(lines)

    def print_maze(self, filename: str | None = None) -> None:
        maze_str = str(self)

        print(maze_str)

        if filename is not None:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(maze_str)


@dataclass
class MazeConfig():
    width: int
    height: int
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str
    perfect: bool

# ConfigValue: TypeAlias = str | int | tuple[int, ...]


class ConfigReader():
    def __init__(self) -> None:
        self.data: dict[str, Any] = {}

    def read(self, filename: str) -> MazeConfig:
        self.data.clear()

        with open(filename, "r") as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue
                if "=" not in line:
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
                        raise ValueError(
                            f"Invalid coordinate format for {key}: {value}"
                        )
                    try:
                        x, y = tuple(int(part.strip()) for part in parts)
                        parsed_value = (x, y)
                    except ValueError:
                        raise ValueError(
                            f"Coordinates for {key} must be integers"
                        )

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
                raise TypeError(
                    f"{key} should be {expected_type.__name__} type"
                )

        if self.data["WIDTH"] < 2:
            raise ValueError("WIDTH must be at least 2")
        if self.data["HEIGHT"] < 2:
            raise ValueError("HEIGHT must be at least 2")

        for coord_key in ("ENTRY", "EXIT"):
            coord = self.data[coord_key]

            if not isinstance(coord, tuple):
                raise TypeError(f"{coord_key} should be a tuple")

            if len(coord) != 2:
                raise ValueError(
                    f"{coord_key} should have only 2 coordinates"
                )

            if not self.in_bounds(coord):
                raise ValueError(
                    f"{coord_key} {coord} is outside maze bounds "
                    f"(WIDTH={self.data['WIDTH']}, "
                    f"HEIGHT={self.data['HEIGHT']})"
                )

        if self.data["ENTRY"] == self.data["EXIT"]:
            raise ValueError("ENTRY and EXIT cannot be the same location")


def main() -> None:
    try:
        reader = ConfigReader()
        config = reader.read("config.txt")

        maze = Maze(
            width=config.width,
            height=config.height,
            entry=config.entry,
            exit=config.exit
        )

        print("===== CONFIG =====")
        print(f"width: {maze.width}")
        print(f"height: {maze.height}")
        print(f"entry: {maze.entry}")
        print(f"exit: {maze.exit}")

        # turns everything to path = for logo testin
        for y in range(maze.height):
            for x in range(maze.width):
                maze.set_path(x, y)

        maze.logo_42()

        if config.output_file:
            maze.print_maze(config.output_file)
            print(f"\nMaze saved to '{config.output_file}'")
        else:
            maze.print_maze()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

# c.validate()
# m = Maze(c.get("width"), c.get("height"))
