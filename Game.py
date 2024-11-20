from tkinter import *
from tkinter import ttk
from Snake import *
from Food import *
import random as r

SQUARE_SIZE = 20

class Game:
    
    def __init__(self, h, w, root: Tk) -> None:
        self._height = h
        self._width = w
        self._snake = Snake()
        self._food = Food()
        self.score = 0
        
        self._direction = 'Right'
        
        self.root = root
        self.root.title("Snake")
        self.game_over = False
        self.grow = False
        
        self.board()
        self.root.bind('<Key>', self.change_direction)
        
        self.draw_food()
        
        self.game_loop()
        
    def change_direction(self, event):
        print(f'inside change direction | key: {event.char}')
        if event.char == 'w' and self._direction != 'Down': self._direction = 'Up'
        if event.char == 's' and self._direction != 'Up': self._direction = 'Down'
        if event.char == 'a' and self._direction != 'Right': self._direction = 'Left'
        if event.char == 'd' and self._direction != 'Left': self._direction = 'Right'
        
    def check_collisions(self):
        head = self._snake.head
        sq = SQUARE_SIZE
        #check OOB
        if head[0] > 380 or head[1] > 380:
            self.game_over = True
            return
        
        if head[0] < 0 or head[1] < 0:
            self.game_over = True
            return
        
        #check if snake hit self
        for i in self._snake.coord[1:]:
            if head == i:
                self.game_over = True
                break
    
    def check_food(self):
        
        head = self._snake.head
        print(f'Head {head} Food: {self._food.c}')
        if head == tuple(self._food.c):
            print('WOOOOOOOOOOOOOOOOO')
            self.score += 1
            self.grow = True
            self.draw_food()
        
    def board(self):
        self.canvas = Canvas(self.root, background='white', width=self._width, height=self._height+20)
        self.canvas.pack() # Doesn't seem to do anything
        
        for line in range(0, self._width, 20):
            self.canvas.create_line([(line, 0), (line, self._height)], fill='black', tags='grid_line_w')
        for line in range(0, self._height, 20):
            self.canvas.create_line([(0, line), (self._width, line)], fill='black', tags='grid_line_h')

        self.canvas.grid(row=0, column=0)
        
    def draw_snake(self):
        sq = SQUARE_SIZE
        c = self._snake.coord
        self.canvas.delete('snake')
        scoreLabel = Label(self.root, text=f'Score: {self.score}')
        scoreLabel.place(x=200, y=400)
        for i, (x, y) in enumerate(c):
            if i == 0:
                self.canvas.create_rectangle(x, y, x+sq, y+sq, fill='red', tags='snake')
            else:
                self.canvas.create_rectangle(x, y, x+sq, y+sq, fill='blue', tags='snake')
    
    def move_snake(self):
        
        head = self._snake.coord[0]
        
        if self._direction == 'Up': newHead = (head[0], head[1]-20)
        if self._direction == 'Down': newHead = (head[0], head[1]+20)
        if self._direction == 'Right': newHead = (head[0]+20, head[1])
        if self._direction == 'Left': newHead = (head[0]-20, head[1])
        
        self._snake.coord.insert(0, newHead)
        if self.grow == False:
            self.canvas.delete(self._snake.coord[-1])
            self._snake.pop()
        else:
            self.grow = False
        
    def draw_food(self):
        
        sq = SQUARE_SIZE
        self.canvas.delete('food')
        self._food.createFood()
        print(f'\nFood spawned at {self._food.c}\n')
        x = self._food.x ; y = self._food.y
        self.canvas.create_oval(x, y, x+sq, y+sq, fill='green', tags='food')
          
    def restart(self):
        
        self.rBut.destroy()
        self.canvas.delete('GOText')
        self.game_over = False
        self._snake = Snake()
        self._food = Food()
        self.score = 0
        self.draw_food()
        
        self.game_loop()
         
    def game_ova(self):
        
        self.canvas.create_text(200, 200, text='Game Over', fill='red', font=('Helvetica', 30), tags='GOText')
        self.rBut = Button(self.canvas, text='restart', fg='black', command=self.restart)
        self.rBut.place(x=150, y=250)
        
    def game_loop(self):
        
        if not self.game_over:
            self.draw_snake()
            self.move_snake()
            self.check_collisions()
            self.check_food()
            if not self.game_over:
                self.root.after(90, self.game_loop)
            else:
                self.game_ova()

    
        
    