import random
import time
import curses

from pygame_board_AL import pygame_display

from Engine import *
from OLD.Table import *
import pygame as pg
import time as t
from Tools import *
import sys
random.seed(34567)


DF = pd.DataFrame(np.zeros((3, 3)).astype(int), columns=['A', 'B', 'C'])

engine = game_engine(DF)
user_input =True
player = 1
random_gen = False
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
red     = "\033[0;31m"
print(red)
pg_display = pygame_display(DF)

count = 0
# Pygame
print("\n")
while (True):
    time.sleep(.3)
    event_list = pg.event.get()
    for event in event_list:
        t1 = time.time()
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif random_gen:
            count += 1
            move = pg_display.random_move()
            # pg.quit()
            # sys.exit()
            column = pg_display.df.columns.get_loc(move[1])+1
            row = move[0]+1
            pg_display.draw_state(row,column, player)
            pg_display.draw_status()
            if (pg_display.winner or pg_display.draw):
                pg_display.reset_game()

        elif event.type == pg.MOUSEBUTTONDOWN:
            count += 1
            pg_display.user_click()
            if (pg_display.winner or pg_display.draw):
                pg_display.reset_game()

        t2 = time.time()
        # print(f"\rAverage event time: {(t2-t1)/len(event_list)}")
        if ((t2-t1)/len(event_list)) > 1:
            print("SLOWPOKE")

        sys.stdout.write(f"\rNumber of events:{progress_bar(count, 9)}")
        sys.stdout.flush()

        pg.display.update()
    pg_display.CLOCK.tick(pg_display.fps)





































