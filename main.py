from Game import *
from tkinter import *

def main():
    
    root = Tk()
    
    Game(400, 400, root)
    
    root.mainloop()
    
if __name__ == "__main__":
    main()