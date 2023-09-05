#  define the logic for game, functions for checking win conditions, validating moves,
#  updating the game state.
from random import randint
from tkinter import *

FIELD_X_0 = 50  # top left of field, 1 cell = 140 px x 140 px
FIELD_Y_0 = 122
ROWS = 3
COLS = 3


def start_game():  # TODO
    print('start_game()')
    # if 2 players logged in choose first:
    first_move = randint(1, 2)  # TODO where to define first move player?
    print(first_move)

    # setup empy 2d array for field?


class Cell:  # TODO
    def __init__(self):
        pass

    def cell_click(self):
        pass

    def spawn(self, surface, x_coord, y_coord):
        c_image = PhotoImage(file='images/clear_cell.png')
        self.image_label = Label(surface, image=c_image, bd=0)  # bd=0 - border to 0, bg=widgets_bg
        self.image_label.place(x=x_coord, y=y_coord)
        self.image_label.bind('<ButtonRelease-1>', lambda e: self.cell_click(e, self.image_label))


class Game:  # TODO
    def __init__(self):
        pass

    def fill_field(self, surface):  # fill field with clear cells
        for row in range(ROWS):
            for col in range(COLS):
                Cell.spawn(surface, FIELD_X_0 + 140 * col, FIELD_Y_0 + 140 * row)
            

