from tkinter import *
from tkinter import ttk
from Snake import *
from Food import *

SQUARE_SIZE = 20

class Game:
    
    def __init__(self, h, w) -> None:
        self._height = h
        self._width = w
        self._snake = Snake()
        self._food = Food()
        
        root = Tk()
        root.title("Snake")
        
        self.board(root)
        self.draw_snake()
        self.draw_food()
        self.render(root)
        
        
        
        
    def board(self, root):
        self.canvas = Canvas(root, background='white', width=self._width, height=self._height)
        self.canvas.pack() # Doesn't seem to do anything
        
        for line in range(0, self._width, 20):
            self.canvas.create_line([(line, 0), (line, self._height)], fill='black', tags='grid_line_w')
        for line in range(0, self._height, 20):
            self.canvas.create_line([(0, line), (self._width, line)], fill='black', tags='grid_line_h')

        self.canvas.grid(row=0, column=0)
        
    def draw_snake(self):
        sq = SQUARE_SIZE
        c = self._snake.coord
        for i, (x, y) in enumerate(c):
            if i == 0:
                self.canvas.create_rectangle(x, y, x+sq, y+sq, fill='red', tags='snake')
            else:
                self.canvas.create_rectangle(x, y, x+sq, y+sq, fill='blue', tags='snake')
        
    def draw_food(self):
        sq = SQUARE_SIZE
        x = self._food.x ; y = self._food.y
        self.canvas.create_oval(x, y, x+sq, y+sq, fill='green', tags='food')
        
        
    def render(self, root):
        
        print(f'\nRendering first board\nH: {self._height}\nW: {self._width}\n')
        
        #root.geometry(f"{self._height}x{self._width}")
        
        
        
        root.mainloop()
    
    
    
    """l = tk.Label(root, text='POOP')
        l.place(x=0, y=0)"""
        
    
        
    