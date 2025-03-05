from cell import Cell
import random
import time

class Maze():
    #Constructor for maze 
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self.seed = seed
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        

    #Method to create a 2D list of Cell objects
    def _create_cells(self):

        #Loop through each column of matrix
        for i in range(0, self._num_rows):
            #Create empty col list
            row_cells = []
            #Loop through each row of the matrix
            for j in range(0, self._num_cols):
                #Create a cell object and append to row list
                row_cells.append(Cell(self._win))
            #Append row list to matrix list   
            self._cells.append(row_cells)
        #Loop through matrix to draw each cell
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
    

    #Method to draw cells 
    def _draw_cell(self, i, j):
        #Return if no window exists
        if self._win is None:
            return
        
        #Calculate positions for specific cell
        x1 = self._x1 + j * self._cell_size_x
        y1 = self._y1 + i * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        #Draw the specific cell and animate
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    #Method to animate each cell
    def _animate(self):
        #Return if no window exists
        if self._win is None:
            return
        #Redraw to Tkinter window and sleep
        self._win.redraw()
        time.sleep(0.05)


    #Method to break entrance and exit of maze
    def _break_entrance_and_exit(self):
        #Break enterance - top of top-left cell
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        #Break exit - bottom of bottom-right cell
        self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)


    #Method to break walls throughout enterance
    def _break_walls_r(self, i, j):
        #Mark current cell as visited
        self._cells[i][j].visited = True

        #Infinite loop for DFS
        while True:
            #Empty list for cells to visit
            to_visit = []

            #Add adjacent cells not yet visited
            #Left
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            #Right
            if j < self._num_cols - 1 and not self._cells[i][j+1].visited: 
                to_visit.append((i, j+1))
            #Up
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            #Down
            if i < self._num_rows - 1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))

            #If no directions to traverse, draw cell and return
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            #If directions available, pick randomly
            next_i, next_j = random.choice(to_visit)

            #Break walls between current cell and chosen cell
            #Next cell is to the left
            if next_j < j:  
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            #Next cell is to the right
            if next_j > j:  
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False
            #Next cell is up
            if next_i < i:  
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            #Next cell is down
            if next_i > i: 
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False

            # Recursively visit the next cell
            self._break_walls_r(next_i, next_j)


    #Method to reset the cells visited property to False
    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    
    #Method to solve the maze
    def solve(self):
        return self._solve_r(0, 0)
    

    #Helper method to recursively solve maze
    def _solve_r(self, i, j):

        #Call animate method
        self._animate()

        #Mark current cell as visited
        self._cells[i][j].visited = True

        if i == self._num_rows -1 and j == self._num_cols - 1:
            return True
        
        #Check each direction for solution
        #Left
        if (
            j > 0 
            and not self._cells[i][j].has_left_wall
            and not self._cells[i][j-1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)
    
        #Right
        if (j < self._num_cols - 1
            and not self._cells[i][j].has_right_wall 
            and not self._cells[i][j+1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)
        #Up
        if (i > 0 
            and not self._cells[i][j].has_top_wall
            and not self._cells[i-1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)
        #Down
        if (i < self._num_rows - 1
            and not self._cells[i][j].has_bottom_wall 
            and not self._cells[i+1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)

        return False