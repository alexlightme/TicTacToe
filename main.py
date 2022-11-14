import random

import numpy as np

from Engine import *
from Table import *
from random import randrange
import pygame as pg


random.seed(34567)


DF = pd.DataFrame(np.zeros((3, 3)).astype(int), columns=['A', 'B', 'C'])

engine = game_engine(DF)

print(engine.board)

user_input =True
player = 1
for i in range(200):
    move = randrange(9)
    engine.make_move(player, move, user_input=user_input)
    print(engine.board)
    engine.check_win(player)
    engine.check_draw()
    player = (engine.turn-1) % 2 +1



# Pygame
while (True):

    event_list = pg.event.get()
    for event in event_list:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            user_click()
            if (winner or draw):
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)





































