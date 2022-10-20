import numpy as np

from Engine import *
from Table import *
from random import randrange




DF = pd.DataFrame(np.zeros((3, 3)).astype(int), columns=['A', 'B', 'C'])

engine = game_engine(DF)

print(engine.board)

player = 1
for i in range(9):
    move = randrange(9 )
    engine.make_move(player,move)
    print(engine.board)
    engine.check_win(player)
    player = (player % 2) + 1





































