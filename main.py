from graphics import Window
from maze import Maze
import sys
import time

#Main Function to run script
def main():

    #Setup some initial parameters for maze 
    num_rows = 12
    num_cols = 10
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    seed = int(time.time()) % 10000

    #Set recursion limit
    sys.setrecursionlimit(10000)

    #Create a Window
    win = Window(screen_x, screen_y)

    #Create maze matrix
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, seed)

    #Generate random maze and attempt to solve
    print("maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")

    #Display window
    win.wait_for_close()

if __name__ == "__main__":
    main()