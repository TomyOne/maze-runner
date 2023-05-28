import time
from js import document, console, window
from math import pi, sqrt
from pyodide.ffi import create_proxy
from random import randint
from dataclasses import dataclass, field

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y       
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
    
    def __str__(self):
        return f"x={self.x}:y={self.y}"

class Line():
    def __init__(self, point1: Point, point2: Point):
        self.p1 = point1
        self.p2 = point2

    def draw(self, canvas, color):
        canvas.beginPath()
        canvas.moveTo(self.p1.x, self.p1.y)
        canvas.lineTo(self.p2.x, self.p2.y)
        canvas.stroke()
    
    def __eq__(self, other):
        return self.p1 == other.p1 and self.p2 == other.p2

    def __ne__(self, other):
        return self.p1 != other.p1 or self.p2 != other.p2
    def __str__(self):
        return f"p1:{str(self.p1)},p2:{str(self.p2)}"
        
class WebWindow():
    def __init__(self, width=400, height=300):
        self.__canvas = document.getElementById("circle-canvas")
        self.__ctx = self.__canvas.getContext("2d")
        self.__ctx.fillStyle = "white"
        self.__ctx.fillRect(0,0, self.__canvas.width, self.__canvas.height)
        self.__width = self.__canvas.width
        self.__height = self.__canvas.height
        self.__is_running = False
        self._on_click = create_proxy(self.__on_click)
        document.getElementById("circle-canvas").addEventListener("mousedown", self._on_click)
        self._lines = []
        self._gen_maze_cb = None
        
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    def __on_click(self, e):
        print("Clicked")
        if self._gen_maze_cb is not None:
            self._gen_maze_cb()
    
    def _clear_screen(self):
        self.__ctx.fillStyle = "white"
        self.__ctx.fillRect(0,0, self.__canvas.width, self.__canvas.height)

    def redraw(self):
        self._clear_screen()
        for line in self._lines:
            line[0].draw(self.__ctx, line[1])
        # self.__root.update_idletasks()
        # self.__root.update()
    
    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            time.sleep(0.001)
            self.redraw()
    
    def close(self):
        self.__is_running = False
        
    def draw_line(self, line: Line, color="black"):
        print(f"Drawing line: {line}")
        line.draw(self.__ctx, color)
        # if line not in self._lines:
        #     self._lines.append((line, color))
        print(f"Num of Lines: {len(self._lines)}")
        
        
    