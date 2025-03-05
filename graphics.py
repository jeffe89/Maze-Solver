from tkinter import Tk, BOTH, Canvas

class Window:
    #Constructor for a Tkinter window
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("My Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width = width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        

    #Method to redraw all the graphics in Tkinter window
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()


    #Method set Tkinter window's running state to 'True'
    def wait_for_close(self):
        self.__running = True
        #Redraw continuously while running state remaings 'True'
        while self.__running:
            self.redraw()
        print("window closed...")


    #Method takes instance of a Line and a Fill Color and calls Line's draw() method
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


    #Method to set Tkinter window's running state to 'False'
    def close(self):
        self.__running = False


class Point:
    #Constructor for a point object
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    #Constructor for a line object
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


    #Method takes a Canvas and a Fill Color to draw a line
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )