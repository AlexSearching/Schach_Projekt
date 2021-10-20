from typing import Optional

import pygame
from lucapiece import Piece
from lucapiece import Rook
from lucapiece import Knight
from lucapiece import Bishop
from lucapiece import Queen
from lucapiece import King
from lucapiece import Pawn

pygame.init()

#Set Dimensions
screen_width = 800
screen_height = 800

display_screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Chess Game")

#Set colors
WHITE = (255,255,255)
OPTIONAL = (100,100,100)
RED = (255,0,0)

field_rects = []


def draw_board(OPTIONAL):
    for i in range(8):
        for j in range(8):
            if i %2 == 0 and j %2 != 0:
                pygame.draw.rect(display_screen,(OPTIONAL),((100*i),(100*j),100,100))
            if i %2 != 0 and j %2 != 0:
                pygame.draw.rect(display_screen, (OPTIONAL), ((100 * i), ((100 * j)-100), 100, 100))





#Set a Font type
font = pygame.font.SysFont("consolas",20)

letter_image_list =[]
letter_rect_list = []

#Convert numbers from 97 to 104 to letters (a-h)
for i in range(97,105):
    text_image = font.render(chr(i), True, (0, 0, 0))
    letter_image_list.append(text_image)
    for j in range(8):
        text_rect = text_image.get_rect()
        text_rect.topright = ((j*100+100),700)
        letter_rect_list.append(text_rect)



def describe_fields():
    #Column description
    for i in range(8):
            display_screen.blit(letter_image_list[i], letter_rect_list[i])

    # Row description
    for i in range(1, 9):
        i_text = font.render(str(i), True, (0, 0, 0))
        i_rect = i_text.get_rect()
        i_rect.topleft = (0, (800 - (i * 100)))
        display_screen.blit(i_text, i_rect)





class GameState():

    def __init__(self, col: int, row: int):
        self.col = col
        self.row = row
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.move_list = []
        self.whiteToMove = True
        self.startPos = True

        if self.startPos:
            self.board[0][0] = Rook(1,1,"black")
            self.board[0][1] = Knight(2, 1, "black")
            self.board[0][2] = Bishop(3, 1, "black")
            self.board[0][3] = Queen(4, 1, "black")
            self.board[0][4] = King(5, 1, "black")
            self.board[0][5] = Bishop(6, 1, "black")
            self.board[0][6] = Knight(7, 1, "black")
            self.board[0][7] = Rook(8, 1, "black")

            for i in range(8):
                self.board[1][i] = Pawn(i+1, 2, "black")

            self.board[7][0] = Rook(1, 8, "white")
            self.board[7][1] = Knight(2, 8, "white")
            self.board[7][2] = Bishop(3, 8, "white")
            self.board[7][3] = Queen(4, 8, "white")
            self.board[7][4] = King(5, 8, "white")
            self.board[7][5] = Bishop(6, 8, "white")
            self.board[7][6] = Knight(7, 8, "white")
            self.board[7][7] = Rook(8, 8, "white")

            for i in range(8):
                self.board[6][i] = Pawn(i+1, 7, "white")




    def create_board(self):
        for x in range(self.row):
            for y in range(self.col):
                if self.board[x][y] != None:
                    self.board[x][y].draw()


    def show_board(self):
        pass


                    #self.board[x][y].valid_moves()


    def Piece_selection(self,x: int,y: int):
        #Careful with the order of x and y!!!
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != None:
                    self.board[i][j].PieceChosen = False

        if self.board[y][x] != None:
            self.board[y][x].PieceChosen = True
            self.board[y][x].move()

            self.board[y][x].possible_moves()

    def move(self, move):
        self.board[move.stSqCol][move.stSqRow] = None
        self.board[move.endSqCol][move.endSqRow] = move.pieceCaptured
        self.move_list.append(move)
        self.whiteToMove = not self.whiteToMove




    def Square_selection(self, x: int, y: int):
        if self.board[y][x] == None:
            print("Square")




class Move():
    def __init__(self, start_square, end_square, board):
        self.stSqCol = start_square[0]
        self.stSqRow = start_square[1]
        self.endSqCol = end_square[0]
        self.endSqRow = end_square[1]
        self.pieceMoved = board[self.stSqCol][self.stSqRow]
        self.pieceCaptured = board[self.endSqCol][self.endSqRow]























