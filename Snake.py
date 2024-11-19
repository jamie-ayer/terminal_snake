class Snake:
    
    def __init__(self) -> None:
        self._bodysize = 2
        self._coords = [(200, 200), (180, 200), (160, 200)]
        
    
    
    @property
    def coord(self) -> list[tuple]: return self._coords
    @coord.setter
    def coord(self, val: list[tuple]): self._coords = val
    
    
        