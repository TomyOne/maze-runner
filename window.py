import time
from tkinter import Tk, BOTH, Canvas

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y        

class Line():
    def __init__(self, point1: Point, point2: Point):
        self.p1 = point1
        self.p2 = point2

    def draw(self, canvas: Canvas, color):
        canvas.create_line(self.p1.x, self.p1.y, 
                           self.p2.x, self.p2.y, 
                           fill=color, width=2)
        canvas.pack(fill=BOTH, expand=1)

class Window():
    def __init__(self, width=400, height=300):
        self.__root = Tk()
        # self.__root.geometry(f"{width}x{height}+50+50")
        self.__root.title = "Maze Runner"
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
    
    def close(self):
        self.__is_running = False
        
    def draw_line(self, line: Line, color="black"):
        line.draw(self.__canvas, color)
        
        
    