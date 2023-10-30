# import python GUI from tkinter, import all with *
from tkinter import *

# self explanatory
import random

# constants (uppercase convention)
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR ="#000000"

class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass

# game window 
window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'

# create score label
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

# create background (score and background)
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.mainloop()