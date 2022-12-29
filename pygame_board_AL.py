
import pygame as pg
import time
from Engine import game_engine

class pygame_display(game_engine):
    def __init__(self, DF):
        game_engine.__init__(self,DF)
        self.XO = 1
        # vars(self).update(vars(engine))

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
        self.board = DF

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
            message = str(self.XO) + "'s Turn"
        else:
            message = str(self.winner[0]) + " won !"
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
        pg.display.update()

    def drawXO(self, row, col):
        # for the first row, the image
        # should be pasted at a x coordinate
        # of 30 from the left margin
        if row == 1:
            posx = 30

        # for the second row, the image
        # should be pasted at a x coordinate
        # of 30 from the game line
        if row == 2:
            # margin or width / 3 + 30 from
            # the left margin of the window
            posx = self.width / 3 + 30

        if row == 3:
            posx = self.width / 3 * 2 + 30

        if col == 1:
            posy = 30

        if col == 2:
            posy = self.height / 3 + 30

        if col == 3:
            posy = self.height / 3 * 2 + 30

        # setting up the required board
        # value to display

        self.update_df(row, col, self.XO)

        if (self.XO == 1):

            # pasting x_img over the screen
            # at a coordinate position of
            # (pos_y, posx) defined in the
            # above code
            self.screen.blit(self.x_img, (posy, posx))
            self.XO = 2

        else:
            self.screen.blit(self.o_img, (posy, posx))
            self.XO = 1
        pg.display.update()

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
        board = self.board
        XO = self.XO
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
        if (row and col and self.df.iloc[row - 1][col - 1] == 0):
            self.draw_state(row,col,XO)
            self.draw_status()

    def reset_game(self):
        time.sleep(3)
        self.XO = 1
        self.draw = False
        self.game_initiating_window()
        self.winner = None
        self.reset()




    def draw_state(self, row, col, XO):
        self.drawXO(row, col)
        self.draw = self.check_draw()
        self.winner = self.check_win(XO)
        if self.winner:
            result = self.winner[1]
            if result.index[result.iloc[0, :] == 1].tolist():
                if len(result.index[result.iloc[0, :] == 1].tolist()) == 3:
                    max_c1 = max(result.index[result.iloc[0, :] == 1].tolist())
                    pg.draw.line(self.screen, (250, 0, 0),
                                 (1 * self.width / 3 - self.width / 6, (1) * self.height / 3 - self.height / 6),
                                 (2 * self.width / 3 + self.width / 6, (1) * self.height / 3 - self.height / 6),
                                 4)
                else:
                    max_c1 = max(result.index[result.iloc[0, :] == 1].tolist())
                    max_c3 = max(result.index[result.iloc[2, :] == 1].tolist())
                    pg.draw.line(self.screen, (250, 0, 0),
                                 (max_c1 * self.width / 3 + self.width / 6, (1) * self.height / 3 - self.height / 6),
                                 (max_c3 * self.width / 3 + self.width / 6, (3) * self.height / 3 - self.height / 6),
                                 4)

            else:
                max_r1 = max(result.index[result.iloc[:, 0] == 1].tolist())
                max_r3 = max(result.index[result.iloc[:, 2] == 1].tolist())
                pg.draw.line(self.screen, (250, 0, 0),
                             (1 * self.width / 3 - self.width / 6, (max_r1) * self.height / 3 + self.height / 6),
                             (3 * self.width / 3 - self.width / 6, (max_r3) * self.height / 3 + self.height / 6),
                             4)


