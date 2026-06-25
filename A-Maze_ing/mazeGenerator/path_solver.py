from collection import deque
from MazeGenerator.Maze import Maze

def bfs_solve_maze(maze: Maze) -> tuple[list[tuple[int, int]],
                                          list[tuple[int, int]]]:

    grid = maze.grid
    height = maze.grid_height
    width = maze.grid_width
    x1, y1 = maze.entry
    x2, y2 = maze.exit

    (entry_x, entry_y) = (x1 * 2 + 1), (y1 * 2 + 1)
    (exit_x, exit_y) =(x2 * 2 + 1), (y2 * 2 + 1)

    queue: deque[tuple[int,int]] = deque()
    visited: set[tuple[int, int]] = set()
    explored: list[tuple[int,int]] = []
    parent: dict[tuple[int, int], tuple[int, int]] ={}


