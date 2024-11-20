import random as r

class Food:
    
    def __init__(self) -> None:
        self.coords = [1, 1]
        
    def createFood(self):
        
        self.coords[0] = (r.randint(0, 19) * 20)
        self.coords[1] = (r.randint(0, 19) * 20)
        
    @property
    def c(self):
        return self.coords
        
    @property
    def x(self) -> int: return self.coords[0]
    @property
    def y(self) -> int: return self.coords[1]