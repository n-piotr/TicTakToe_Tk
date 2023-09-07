#  define the logic for game, functions for checking win conditions, validating moves,
#  updating the game state.
from const import *
from random import randint
from tkinter import *


def start_game():  # TODO
    print('start_game()')
    # if 2 players logged in choose first:
    first_move = randint(1, 2)  # TODO where to define first move player?
    print(first_move)
    return first_move


# Store the active player globally  #
active_player = start_game()  #


# def initialize_game():
#     global active_player
#     active_player = start_game()

    # setup empy 2d array for field?


class Cell:  # TODO
    def __init__(self, surface, x_coord, y_coord):
        self.surface = surface
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.image_label = None
        self.c_image = PhotoImage(file=C_IMAGE)
        self.x_image = PhotoImage(file=X_IMAGE)
        self.o_image = PhotoImage(file=O_IMAGE)
        self.player = 0

    def spawn(self):
        self.image_label = Label(self.surface, image=self.c_image, bd=0, bg=WIDGETS_BG)  # bd=0 - border to 0
        self.image_label.place(x=self.x_coord, y=self.y_coord)
        self.image_label.bind('<Button-1>', self.cell_click)

    def cell_click(self, event):
        global active_player  #
        self.player = active_player
        print('cell clicked by', self.player)
        # check if can be clicked (state or 2d array?)
        # if _player1_ click then switch image to X
        if self.player == 1:
            self.image_label.configure(image=self.x_image)
            self.player = 2
            # active_player = self.player
        # if _player2_ click then switch image to O
        elif self.player == 2:
            self.image_label.configure(image=self.o_image)
            self.player = 1
            # active_player = self.player
        active_player = self.player  # update players turn
        self.image_label.bind('<Button-1>', self.temp)

    # @staticmethod
    def temp(self, event):
        print('cell already clicked')


        # update _field array_
        # check for winning condition
        # if no win switch player

        # active_player = self.player  #
        # start_game()


class Field:  # TODO maybe combine with Cell
    def __init__(self):
        self.console_field = [[0, 0, 0] for col in range(COLS)]
        self.create()

    def create(self):
        # for row in range(ROWS):  # adding objects in place of zeroes in 2d array
        #     for col in range(COLS):
        #         self.console_field[row][col] =  # place Cell object?
        print(self.console_field)


# f = Field()
# f.create()


class Game:  # TODO
    def __init__(self):
        pass

    # def fill_field(self, surface):  # fill field with clear cells
    #     for row in range(ROWS):
    #         for col in range(COLS):
    #             Cell.spawn(surface, FIELD_X_0 + 140 * col, FIELD_Y_0 + 140 * row)
            

