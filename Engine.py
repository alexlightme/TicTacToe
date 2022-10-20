import sys

import numpy as np
from Table import Board
from Errors import *
import os

class game_engine():
    def __init__(self, df):
        self.df = df
        self.board = Board(df)

    def check_win(self, player):
        df = self.df.copy()
        df[df != player] = int(0)
        if sum(df.to_numpy().diagonal())/3 == 1\
                or sum(np.flip(df.to_numpy(),0).diagonal())/3 == 1\
                or sum(df.iloc[ : , 0])/3 == 1\
                or sum(df.iloc[ : , 1])/3 == 1\
                or sum(df.iloc[ : , 2])/3 == 1\
                or sum(df.iloc[ 0 , :])/3 == 1\
                or sum(df.iloc[ 1 , :])/3 == 1\
                or sum(df.iloc[ 2 , :])/3 == 1:
            print("Congrats")
            return sys.exit(0)
        else:
            return

    def check_legal_move(self):



        return

    def update_board(self):
        self.board.df = self.df
        self.board.update_line()
        return

    def make_move_user(self, player):
        print(f"{'-'*5}Input moves{'-'*5}\n\n")

        while True:
            while True:
                try:
                    x = int(input("Input row (0 to 2): "))
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
                    y = int(input("\nInput Column (0 to 2): \n"))
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
                break
            except Occupied:
                print("\nSpace is already occupied!!\n")
        self.df.iloc[x, y] = player

        self.update_board()

        return

    def make_move(self, player, position):
        print(f"{'-'*5}Input moves{'-'*5}\n\n")

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
                break
            except Occupied:
                print("\nSpace is already occupied!!\n")
                sys.exit(1)
        self.df.iloc[x, y] = player

        self.update_board()

        return





