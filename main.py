import random

from pygame_board_AL import pygame_display
import numpy as np

from Engine import *
from Table import *
from random import randrange
import pygame as pg


random.seed(34567)


DF = pd.DataFrame(np.zeros((3, 3)).astype(int), columns=['A', 'B', 'C'])

engine = game_engine(DF)
user_input =True
player = 1
#/////////////////////////////////////////////////////////////////////////////
# OLD DISPLAY AND ENGINE
# for i in range(200):
#     move = randrange(9)
#     engine.make_move(player, move, user_input=user_input)
#     print(engine.board)
#     engine.check_win(player)
#     engine.check_draw()
#     player = (engine.turn-1) % 2 +1
#/////////////////////////////////////////////////////////////////////////////

pg_display = pygame_display(engine)

# Pygame
while (True):

    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            pg_display.user_click()
            if (pg_display.winner or pg_display.draw):
                pg_display.reset_game()
    pg.display.update()
    pg_display.CLOCK.tick(pg_display.fps)





































