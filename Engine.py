import sys

import numpy as np
from Table import Board
from Errors import *
import os

class game_engine():
    def __init__(self, df):
        self.df = df
        self.board = Board(df)
        self.turn = 1

    def check_win(self, player):
        df = self.df.copy()
        df[df != player] = int(0)
        df = df.mask(df == player, 1)
        if sum(np.diagonal(df))/3 == 1\
                or sum(np.diagonal(np.rot90(df,1)))/3 == 1\
                or sum(df.iloc[ : , 0])/3 == 1\
                or sum(df.iloc[ : , 1])/3 == 1\
                or sum(df.iloc[ : , 2])/3 == 1\
                or sum(df.iloc[ 0 , :])/3 == 1\
                or sum(df.iloc[ 1 , :])/3 == 1\
                or sum(df.iloc[ 2 , :])/3 == 1:
            print(f"Result: Player {player} wins!!")
            return sys.exit(0)
        else:
            return

    def check_draw(self):
        if self.turn==10:
            print("Result: Draw!")
            sys.exit(0)
        return
    def check_legal_move(self):



        return

    def update_board(self):
        self.board.df = self.df
        self.board.update_line()
        return

    def make_move(self, player, position, user_input):
        print(f"{'-' * 5}Player: {player} Turn: {self.turn}{'-' * 5}\n")
        print(f"{'-'*5}Input moves{'-'*5}\n")

        # Decode position
        d = {
            0: (0,0),
            1: (1,0),
            2: (2, 0),
            3: (0, 1),
            4: (1, 1),
            5: (2, 1),
            6: (0, 2),
            7: (1, 2),
            8: (2, 2),
        }

        while True:
            while True:
                try:
                    if user_input:
                        x = int(input("Input row (0 to 2): "))
                    else:
                        x = d[position][0]
                    if x < 0 or x > 2:
                        raise NotInRangeError
                    break
                except ValueError:
                    print("\nOops!  That was no valid number.  Try again...\n")
                except NotInRangeError:
                    print("\nInput needs to be between 0 and 2\n")
                    print()
            while True:
                try:
                    if user_input:
                        y = int(input("\nInput Column (0 to 2): \n"))
                    else:
                        y = d[position][1]
                    if y < 0 or y > 2:
                        raise NotInRangeError
                    break
                except ValueError:
                    print("\nOops!  That was no valid number.  Try again...\n")
                except NotInRangeError:
                    print("Input needs to be between 0 and 2")
                    print()

            try:
                if self.df.iloc[x,y] != 0:
                    raise Occupied
                self.update_df(x, y, player)
                self.update_board()
                self.turn += 1
                break
            except Occupied:
                print("\nSpace is already occupied!!\n")
                print("Try Again!\n")
                break

        return

    def update_df(self, x, y, player):
        self.df.iloc[x, y] = player
        return



