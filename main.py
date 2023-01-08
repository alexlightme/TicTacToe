import random
import time
from Agent import *
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
random_gen = True

red     = "\033[0;31m"
print(red)
pg_display = pygame_display(DF)

count = 0
gamecount = 0
# Pygame
print("\n")

states = pg_display.legal_moves_index()
player1 = Agent(states,1)
player2 = Agent(states, 2)
agent_list = [player1, player2]
curr_player = 0

def buffer ():
    ev = pg.event.Event ( pg.USEREVENT )
    pg.event.post ( ev )
while (True):
    # time.sleep(.5)
    buffer()
    event_list = pg.event.get()
    # event_list.append(pg.USEREVENT)
    if random_gen:
        count += 1
        try:
            player = agent_list[curr_player]
            legal_moves = pg_display.legal_moves_index()
            move = player.choose_action(legal_moves,legal_moves)
            # move = pg_display.random_move()
        except:
            print("Uhoh")

        # pg.quit()
        # sys.exit()
        column = move[1] + 1
        row = move[0] + 1
        pg_display.draw_state(row, column, player)
        pg_display.draw_status()

        #next player
        curr_player += 1
        curr_player = curr_player % 2

        if (pg_display.winner or pg_display.draw):
            gamecount += 1
            pg_display.reset_game()
            player.learn()
            curr_player = 0
            pg.event.clear

    else:
        for event in event_list:
            t1 = time.time()
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                count += 1
                pg_display.user_click()
                if (pg_display.winner or pg_display.draw):
                    pg_display.reset_game()
                    pg.event.clear
                    break

            t2 = time.time()
            # print(f"\rAverage event time: {(t2-t1)/len(event_list)}")
            if ((t2-t1)/len(event_list)) > 1:
                print("SLOWPOKE")
            pg.display.update()

    sys.stdout.write(f"\rNumber of events:{len(event_list)} - --- - Game#: {gamecount}")# {progress_bar(count, 9)}")
    sys.stdout.flush()

    pg_display.CLOCK.tick(pg_display.fps)





































