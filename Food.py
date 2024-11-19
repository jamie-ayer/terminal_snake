import random as r

class Food:
    
    def __init__(self) -> None:
        self.coords = [5, 5]
        
    def createFood(self):
        
        self.coords[0] = r.randint(0, 20)
        self.coords[1] = r.randint(0, 20)
        
    @property
    def x(self) -> int: return self.coords[0] * 20
    @property
    def y(self) -> int: return self.coords[1] * 20