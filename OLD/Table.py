
import pandas as pd
import numpy as np

class Board():
    def __init__(self, DF):
        self.name = "Table"
        self.df = DF


        self.horizontal_line = "_"*3
        self.vertical_line = "|"

        self.first_line = f"{self.horizontal_line}{self.vertical_line}{self.horizontal_line}{self.vertical_line}{self.horizontal_line}"
        self.second_line = f"{self.vertical_line}   {self.vertical_line}"

        self.frame_board = self.box3 = "_"*5*3
        self.box1 = "_"*3+"|"
        self.box2 = "_"*3+"|"
        self.box3 = "_"*3
        self.box4 = "_"*3+"|"
        self.box5 = "_"*3+"|"
        self.box6 = "_"*3
        self.box7 = " "*3+"|"
        self.box8 = " "*3+"|"
        self.box9 = " "*3



        self.line1 = " "*3+"|"+" "*3+"|"
        self.line2 = " "*3+"|"+" "*3+"|"
        self.last_line = " " * 3 + "|" + " " * 3 + "|"

        # print(f"\n{self.box3*5}\n{self.line1}\n{self.box1}{self.box2}{self.box3}\n{self.last_line}\n{self.box4}{self.box5}{self.box6}\n{self.last_line}")
        self.update_line()

        # print(self.board_df)

    def __str__(self):

        return f"\n{self.frame_board}\n{self.line1}\n{self.box1}{self.box2}{self.box3}\n{self.line2}\n{self.box4}{self.box5}{self.box6}\n{self.box7}{self.box8}{self.box9}\n{self.last_line}\n{self.frame_board}"

    def update_df(self):
        self.df = self.engine.df
        return

    def update_line(self):
        df = self.df
        # check_empty
        position = []
        for row in range(3):
            for col in range(3):
                position.append(self.empty_tile_convert(df.iloc[row, col]))
        self.line1 = f" {position[0]} | {position[1]} | {position[2]}"
        self.line2 = f" {position[3]} | {position[4]} | {position[5]}"
        self.last_line = f" {position[6]} | {position[7]} | {position[8]}"


    def empty_tile_convert(self, value):
        if value!=2 and value!=1:
            return " "
        if value == 1:
            return "X"
        if value == 2:
            return "O"

        return value








