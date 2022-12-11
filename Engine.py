import sys

import numpy as np
from OLD.Table import Board


class game_engine():
    def __init__(self, df):
        self.initial_df = df.copy()
        self.df = df.copy()
        self.turn = 1
        self.player = 1

    def check_win(self, player):
        df = self.df.copy()
        df[df != self.player] = int(0)
        df = df.mask(df == self.player, 1)
        result = self.initial_df.copy()
        if sum(np.diagonal(df))/3 == 1:
            np.fill_diagonal(result.to_numpy(),1)

            print(f"Result: Player {player} wins!!")
            return [player, result]

        elif sum(np.diagonal(np.rot90(df,1)))/3 == 1:
            np.fill_diagonal(np.rot90(result.to_numpy()),1)

            print(f"Result: Player {player} wins!!")
            return [player, result]

        elif sum(df.iloc[ : , 0])/3 == 1:
            result.iloc[ : , 0] = 1
            print(f"Result: Player {player} wins!!")
            return [player, result]

        elif sum(df.iloc[ : , 1])/3 == 1:
            result.iloc[ : , 1] = 1
            print(f"Result: Player {player} wins!!")
            return [player, result]

        elif sum(df.iloc[ : , 2])/3 == 1:
            result.iloc[ : , 2] = 1
            print(f"Result: Player {player} wins!!")
            return [player, result]

        elif sum(df.iloc[ 0 , :])/3 == 1:
            result.iloc[ 0 , :] = 1
            print(f"Result: Player {player} wins!!")
            return [player, result]

        elif sum(df.iloc[ 1 , :])/3 == 1:
            result.iloc[ 1 , :] = 1
            print(f"Result: Player {player} wins!!")
            return [player, result]

        elif sum(df.iloc[ 2 , :])/3 == 1:
            result.iloc[ 2 , :] = 1
            print(f"Result: Player {player} wins!!")
            return [player, result]
        else:
            self.turn += 1
            return

    def check_draw(self):
        if self.turn==10:
            print("Result: Draw!")
            return [0]
        else:
            return None

    def update_df(self, x, y, player):
        self.player = player
        self.df.iloc[x-1, y-1] = player
        return


    def reset(self):
        self.df = self.initial_df.copy()
        self.turn = 1
        self.player = 1

