
import pygame as pg
import time


class pygame_display():
    def __init__(self, engine):
        self.XO = 'x'

        # storing the winner's value at
        # any instant of code
        self.winner = None

        # to check if the game is a draw
        self.draw = None

        # to set width of the game window
        self.width = 400

        # to set height of the game window
        self.height = 400

        # to set background color of the
        # game window
        self.white = (255, 255, 255)

        # color of the straightlines on that
        # white game board, dividing board
        # into 9 parts
        self.line_color = (0, 0, 0)

        # setting up a 3 * 3 board in canvas
        self.board = engine.df

        # initializing the pygame window
        pg.init()

        # setting fps manually
        self.fps = 30

        # this is used to track time
        self.CLOCK = pg.time.Clock()

        # this method is used to build the
        # infrastructure of the display
        self.screen = pg.display.set_mode((self.width, self.height + 100), 0, 32)

        # setting up a nametag for the
        # game window
        pg.display.set_caption("My Tic Tac Toe")

        # loading the images as python object
        self.initiating_window = pg.image.load("images/modified_cover-100x100.png")
        self.x_img = pg.image.load("images/X_modified-100x100.png")
        self.y_img = pg.image.load("images/o_modified-100x100.png")

        # resizing images
        self.initiating_window = pg.transform.scale(self.initiating_window, (self.width, self.height + 100))
        self.x_img = pg.transform.scale(self.x_img, (80, 80))
        self.o_img = pg.transform.scale(self.y_img, (80, 80))

        self.game_initiating_window()

    def draw_status(self):
        # getting the global variable draw
        # into action
        draw = self.draw

        if self.winner is None:
            message = self.XO.upper() + "'s Turn"
        else:
            message = self.winner.upper() + " won !"
        if draw:
            message = "Game Draw !"

        # setting a font object
        font = pg.font.Font(None, 30)

        # setting the font properties like
        # color and width of the text
        text = font.render(message, 1, (255, 255, 255))

        # copy the rendered message onto the board
        # creating a small block at the bottom of the main display
        self.screen.fill((0, 0, 0), (0, 400, 500, 100))
        text_rect = text.get_rect(center=(self.width / 2, 500 - 50))
        self.screen.blit(text, text_rect)

    def game_initiating_window(self):
        # displaying over the screen
        self.screen.blit(self.initiating_window, (0, 0))

        # updating the display
        pg.display.update()
        time.sleep(3)
        self.screen.fill(self.white)

        # drawing vertical lines
        pg.draw.line(self.screen, self.line_color, (self.width / 3, 0), (self.width / 3, self.height), 7)
        pg.draw.line(self.screen, self.line_color, (self.width / 3 * 2, 0), (self.width / 3 * 2, self.height), 7)

        # drawing horizontal lines
        pg.draw.line(self.screen, self.line_color, (0, self.height / 3), (self.width, self.height / 3), 7)
        pg.draw.line(self.screen, self.line_color, (0, self.height / 3 * 2), (self.width, self.height / 3 * 2), 7)
        self.draw_status()

    def user_click(self):
        # get coordinates of mouse click
        x, y = pg.mouse.get_pos()

        # get column of mouse click (1-3)
        if (x < self.width / 3):
            col = 1

        elif (x < self.width / 3 * 2):
            col = 2

        elif (x < self.width):
            col = 3

        else:
            col = None

        # get row of mouse click (1-3)
        if (y < self.height / 3):
            row = 1

        elif (y < self.height / 3 * 2):
            row = 2

        elif (y < self.height):
            row = 3

        else:
            row = None

        # after getting the row and col,
        # we need to draw the images at
        # the desired positions
        if (row and col and board[row - 1][col - 1] is None):
            global XO
            drawXO(row, col)
            check_win()

    def reset_game(self):
        global board, winner, XO, draw
        time.sleep(3)
        XO = 'x'
        draw = False
        self.game_initiating_window()
        winner = None
        board = [[None] * 3, [None] * 3, [None] * 3]






