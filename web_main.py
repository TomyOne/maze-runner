
# from window import Window
from maze import Maze


from web_window import WebWindow

win = WebWindow()

# win.wait_for_close()

num_rows = 4#12
num_cols = 4#16
margin = 50
screen_x = win.get_width()
screen_y = win.get_height()
cell_size_x = (screen_x - 2 * margin) / num_cols
cell_size_y = (screen_y - 2 * margin) / num_rows
    
# win = Window(screen_x, screen_y)

maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)

# maze.solve()

# win.wait_for_close()
