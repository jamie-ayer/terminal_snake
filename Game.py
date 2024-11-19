import tkinter as tk
from tkinter import ttk

class Game:
    
    def __init__(self, h, w) -> None:
        self._height = h
        self._width = w
    
    def render(self):
        
        print(f'rendering first board\nH: {self._height}\nW: {self._width}')
        
        root = tk.Tk()
        root.title("Snake")
        root.geometry(f"{self._height}x{self._width}")
        root.mainloop()
        
    
        
    