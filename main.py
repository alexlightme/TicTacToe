import random

import numpy as np

from Engine import *
from Table import *
from random import randrange

random.seed(3456)


DF = pd.DataFrame(np.zeros((3, 3)).astype(int), columns=['A', 'B', 'C'])

engine = game_engine(DF)

print(engine.board)

player = 1
for i in range(200):
    move = randrange(9)
    engine.make_move(player, move)
    print(engine.board)
    engine.check_win(player)
    engine.check_draw()
    player = (engine.turn-1) % 2 +1






































