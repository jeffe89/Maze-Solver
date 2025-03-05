from graphics import Line, Point

class Cell:
    #Constructor for each cell in the maze
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False   


    #Method to draw each cell on the Tkinter window
    def draw(self, x1, y1, x2, y2):

        #Return if window does not exist
        if self._win is None:
            return
        
        #Set x and y values
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        #Draw left wall black if True - White if False
        if self.has_left_wall:
            left_line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_line)
        else:
            left_line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_line, "white")

        #Draw right wall black if True - White if False
        if self.has_right_wall:
            right_line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_line)
        else:
            right_line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_line, "white")

        #Draw top wall black if True - White if False
        if self.has_top_wall:
            top_line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_line)
        else:
            top_line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_line, "white")
        
        #Draw bottom wall black if True - White if False
        if self.has_bottom_wall:
            bottom_line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_line)
        else:
            bottom_line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_line, "white")


    #Method to draw a path between two cells
    def draw_move(self, to_cell, undo=False):

        #Calculate the center values for first cell
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        #Calculate the center values for second cell
        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        #Set fill color according to undo flag
        fill_color = "red"
        if undo:
            fill_color = "gray"
        
        #Create a line between points and draw it 
        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color)