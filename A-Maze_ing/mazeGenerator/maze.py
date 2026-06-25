import random 

class Maze:
    def __init__(self, 
                height: int, 
                width: int, 
                entry: turple[int, int], 
                exit: turple[int, int]) -> None:
        self.height = height
        self.width = width
        self.entry = entry
        self.exit = exit

        self.grid: list[list[int]] = []

        self.grid_height = 2 * height + 1
        self.grid_width = 2 * width + 1

        for wall in range(0, self.grid_height):
            row: list[int] = []
            for wall in range(0, self.grid_width):
                row.append(1)
            self.grid.append(row)