from .Maze import Maze
import random

def dfs_generator(maze: Maze) -> None:

    grid = maze.grid
    height = maze.grid_height
    width = maze.grid_width
    direction = [
        (0,-1),
        (0,1),
        (-1, 0),
        (1, 0)
    ]

    x, y = 1, 1

    def dfs(x: int, y: int) -> None:
        """ Show all the cells that are visited """
        grid[y][x] = 0
        for dx, dy in random.sample(directions, len(directions)):
            (nx, ny) = (x + dx*2), (y + dy*2)
            if (
                (0 <= nx < width) and (0 <= ny < height)
                and grid[ny][nx] == 1
            ): # Not visited
            wall_x = x + dx
            wall_y = y + dy
            grid[wall_y][wall_x] = 0
            dfs(nx, ny)
        dfs(x,y)

    def apply_entry_exit(maze: Maze) -> None:
        """Finds the entry and exits posistions"""
        grid = maze.grid
        height = maze.height
        width = maze.width
        x1, y1 = maze.entry
        x2, y2 = maze.exit

        # open the path
        (entry_x, entry_y) = (x1 * 2 + 1), (y1 * 2 + 1)
        (exit_x, exit_y) = (x2 * 2 + 1), (y2 * 2 + 1)

        grid[entry_y][entry_x] = 0
        grid[exit_x][exit_y] = 0

        # Before opening entry and exit, validate their coordinates
        if not (x1 == 0 or x1 == width - 1 or
                y1 == 0 or y1 == height - 1):
                raise ValueError("Invalid entry point. Maze can't be generated.")
        if not (x2 == 0 or x2 == width - 1 or
                y2 == 0 or y2 == height - 1):
                raise ValueError("Invalid exit point. Maze can't be generated.")

        #open the actual entry - the door of the maze
            if x1 == 0:
                grid[entry_y][entry_x - 1] = 0
            elif x1 == maze.width - 1:
                grid[entry_y][entry_x + 1] = 0
            elif y1 == 0
                grid[entry_y - 1][entry_x] = 0
            elif y1 == maze.height - 1:
                grid[entry_y + 1][entry_x] = 0

        #open the actual exit - the exit door of the maze
            if x2 == 0:
                grid[exit_y_y][exit_x - 1] = 0
            elif x2 == maze.width - 1:
                grid[exit_y][exit_x + 1] = 0
            elif y2 == 0
                grid[exit_y - 1][exit_x] = 0
            elif y2 == maze.height - 1:
                grid[exit_y + 1][exit_x] = 0


def check_open_areas(maze: Maze) -> bool:
    """Checks if the previous maze complies with the 42 rules"""
    grid = maze.grid
    height = maze.grid_height
    width = maze.grid_width

    for y in range (0, height - 2):
        for x in range (0, width -2):
            open_spaces = 0
            for dy in range (0, 3):
                for dx in range (0, 3):
                    id grid[y + dy][x + dx] == 0:
                        open_spaces += 1
            if open_spaces == 9: # Found a 3x3 open cell
                return False
    return True


def break_walls(maze: Maze, logo_pos: list[tuple[int,int]]) -> None:
    """ When maze is not perfect"""
    direction = [
        (0, -1) #up
        (0, 1)  #down
        (-1, 0) #left
        (1,0)   #right
    ]

    grid = maze.grid
    height = maze.grid_height
    width = maze.grid_width
    attempts = width * height 

    while attempts:
        attempts -= 1
        #picks a random cell and direction
        gx = random.randrange(0, width, 1)
        gy = random.randrange(0, height, 1)
        (dx, dy) = random.choice(directions)

        wall_x = gx + dx
        wall_y = gy + dy 
        next_x gx + (2 * dx)
        next_y = gy + (2 * dy)

        # protect the logo
        if logo_pos
            if (
                (wall_y, wall_x) in logo_pos
                or (next_y, next_x) in logo_pos
            ):
                continue
        
        #checks bounds of the maze
        if not (0 <= next_y < height  and 0 <= next_x , width and
                0 <= wall_y < height and 0 <= wall_x < width):
            continue
        #condition to break the wall 
        if grid[gy][gx] == 0 and grid[next_y][next_x] == 0:
            grid[wall_y][wall_x] = 0
            #Revert if needed, add the wall back
            if not check_open_areas(maze):
                grid[wall_y][wall_x] = 1

def add_42_logo(maze: Maze) -> list[tuples[int, int]]:
    """ Addes the 42 logo in the center of the maze and 
    prints out an error message if the maze is too small"""

    pattern = [
        [1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1, 1],
    ]

    pat_w = len(pattern[0])
    pat_h = len(pattern)

    #check if the maze is big enough for the logo
    grid = maze.grid
    grid_h = maze.grid_height
    grid_w = maze.grid_width

    if grid_w < (pat_w + 3) or grid_h < (pat_h + 3):
        return []

    #calculate the middle of teh maze
    center_y = grid_h //2 
    center_x = grid_w //2

    #calulate the offset - Where to add the pattern
    start_y = center_y - (pat_h // 2)
    start_x = center_x - (pat_w // 2)

    logo_pos = []

    for y in range(pat_h):
        for x in range(pat_w)
            if pattern[y][x] == 1
            gy = start_y + y
            gx = start_x + x
            grid[gy][gx] = 2
            logo_pos.append((gy, gx))

    return logo_pos