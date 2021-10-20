'''
Moves for the pieces if needed again
'''
#Rook
'''
        if color == "w":
            # Left
            if col > 0:
                for i in range((col - 1), -1, -1):
                    if board[row][i] != None:
                        if board[row][i].color != "w":
                            possible_moves_list.append([i, row])
                        if board[row][i].color == "w":
                            break
                    if board[row][i] == None:
                        possible_moves_list.append([i, row])
            # Right
            if col < 7:
                for i in range((col + 1), 8, +1):
                    if board[row][i] != None:
                        if board[row][i].color != "w":
                            possible_moves_list.append([i, row])
                        if board[row][i].color == "w":
                            break
                    if board[row][i] == None:
                        possible_moves_list.append([i, row])
            #Up
            if row > 0:
                for i in range((row-1), -1,-1):
                    if board[i][col] != None:
                        if board[i][col].color != "w":
                            possible_moves_list.append([col,i])
                            if board[i][col].color == "b":
                                break
                        if board[i][col].color == "w":
                            break


                    if board[i][col] == None:
                        possible_moves_list.append([col, i])
            #Down
            if row < 7:
                for i in range((row+1),8,+1):
                    if board[i][col] != None:
                        if board[i][col].color != "w":
                            possible_moves_list.append([col,i])
                        if board[i][col].color == "w":
                            break
                    if board[i][col] == None:
                        possible_moves_list.append([col, i])
        #For Black
        if color == "b":
            # Left
            if col > 0:
                for i in range((col - 1), -1, -1):
                    if board[row][i] != None:
                        if board[row][i].color != "b":
                            possible_moves_list.append([i, row])
                        if board[row][i].color == "b":
                            break
                    if board[row][i] == None:
                        possible_moves_list.append([i, row])
            # Right
            if col < 7:
                for i in range((col + 1), 8, +1):
                    if board[row][i] != None:
                        if board[row][i].color != "b":
                            possible_moves_list.append([i, row])
                        if board[row][i].color == "b":
                            break
                    if board[row][i] == None:
                        possible_moves_list.append([i, row])
            # Up
            if row > 0:
                for i in range((row - 1), -1, -1):
                    if board[i][col] != None:
                        if board[i][col].color != "b":
                            possible_moves_list.append([col, i])
                            if board[i][col].color == "b":
                                break
                            if board[i][col].color == "w":
                                break


                    if board[i][col] == None:
                        possible_moves_list.append([col, i])
                # Down
            if row < 7:
                for i in range((row + 1), 8, +1):
                    if board[i][col] != None:
                        if board[i][col].color != "b":
                            possible_moves_list.append([col, i])
                        if board[i][col].color == "b":
                            break
                        if board[i][col].color == "w":
                            break
                    if board[i][col] == None:
                        possible_moves_list.append([col, i])
                        
'''
#Knight
'''
        # Up and left
        if color == "w":
            if row >= 2 and col > 0:
                if board[row-2][col-1] != None:
                    if board[row-2][col-1].color != "w":
                        possible_moves_list.append([col-1, row-2])
                if board[row - 2][col - 1] == None:
                    possible_moves_list.append([col - 1, row - 2])
        if color == "b":
            if row >= 2 and col > 0:
                if board[row-2][col-1] != None:
                    if board[row-2][col-1].color != "b":
                        possible_moves_list.append([col-1, row-2])
                if board[row - 2][col - 1] == None:
                    possible_moves_list.append([col - 1, row - 2])



        #Up and right
        if color == "w":
            if row >= 2 and col < 7:
                if board[row-2][col+1] != None:
                    if board[row-2][col+1].color != "w":
                        possible_moves_list.append([col + 1, row - 2])
                if board[row - 2][col + 1] == None:
                    possible_moves_list.append([col + 1, row - 2])

        if color == "b":
            if row >= 2 and col < 7:
                if board[row-2][col+1] != None:
                    if board[row-2][col+1].color != "b":
                        possible_moves_list.append([col + 1, row - 2])
                if board[row - 2][col + 1] == None:
                    possible_moves_list.append([col + 1, row - 2])

        #Left and up
        if color == "w":
            if row > 0 and col >= 2:
                if board[row-1][col-2] != None:
                    if board[row-1][col-2].color != "w":
                        possible_moves_list.append([col - 2, row - 1])
                if board[row -1][col - 2] == None:
                    possible_moves_list.append([col - 2, row - 1])

        if color == "b":
            if row > 0 and col >= 2:
                if board[row-1][col-2] != None:
                    if board[row-1][col-2].color != "b":
                        possible_moves_list.append([col - 2, row - 1])
                if board[row -1][col - 2] == None:
                    possible_moves_list.append([col - 2, row - 1])

        #Left and down
        if color == "w":
            if row < 7 and col >= 2:
                if board[row+1][col-2] != None:
                    if board[row+1][col-2].color != "w":
                        possible_moves_list.append([col - 2, row + 1])
                if board[row + 1][col - 2] == None:
                    possible_moves_list.append([col - 2, row + 1])
        if color == "b":
            if row < 7 and col >= 2:
                if board[row+1][col-2] != None:
                    if board[row+1][col-2].color != "b":
                        possible_moves_list.append([col - 2, row + 1])
                if board[row + 1][col - 2] == None:
                    possible_moves_list.append([col - 2, row + 1])


        #Down and left
        if color == "w":
            if row < 6 and col > 0:
                if board[row+2][col-1] != None:
                    if board[row+2][col-1].color != "w":
                        possible_moves_list.append([col - 1, row + 2])
                if board[row + 2][col - 1] == None:
                    possible_moves_list.append([col - 1, row + 2])
        if color == "b":
            if row < 6 and col > 0:
                if board[row+2][col-1] != None:
                    if board[row+2][col-1].color != "b":
                        possible_moves_list.append([col - 1, row + 2])
                if board[row + 2][col - 1] == None:
                    possible_moves_list.append([col - 1, row + 2])


        #Down and right
        if color == "w":
            if row < 6 and col < 7:
                if board[row+2][col+1] != None:
                    if board[row+2][col+1].color != "w":
                        possible_moves_list.append([col + 1, row + 2])
                if board[row + 2][col + 1] == None:
                    possible_moves_list.append([col + 1, row + 2])
        if color == "b":
            if row < 6 and col < 7:
                if board[row+2][col+1] != None:
                    if board[row+2][col+1].color != "b":
                        possible_moves_list.append([col + 1, row + 2])
                if board[row + 2][col + 1] == None:
                    possible_moves_list.append([col + 1, row + 2])



        #Right and up
        if color == "w":
            if row > 0 and col < 6:
                if board[row-1][col+2] != None:
                    if board[row-1][col+2].color != "w":
                        possible_moves_list.append([col + 2, row -1])
                if board[row - 1][col +2] == None:
                    possible_moves_list.append([col + 2, row - 1])
        if color == "b":
            if row > 0 and col < 6:
                if board[row-1][col+2] != None:
                    if board[row-1][col+2].color != "b":
                        possible_moves_list.append([col + 2, row -1])
                if board[row - 1][col +2] == None:
                    possible_moves_list.append([col + 2, row - 1])


        #Right and down
        if color == "w":
            if row < 7 and col < 6:
                if board[row+1][col+2] != None:
                    if board[row+1][col+2].color != "w":
                        possible_moves_list.append([col + 2, row +1])
                if board[row +1][col + 2] == None:
                    possible_moves_list.append([col + 2, row + 1])

        if color == "b":
            if row < 7 and col < 6:
                if board[row+1][col+2] != None:
                    if board[row+1][col+2].color != "b":
                        possible_moves_list.append([col + 2, row +1])
                if board[row +1][col + 2] == None:
                    possible_moves_list.append([col + 2, row + 1])
        '''
#Bishop

'''
if color == "w":

    #Go up right or up left
    up_right = col +1
    up_left = col - 1
    for i in range((row-1),-1,-1):
        if up_right < 8:
            if board[i][up_right] != None:
                if board[i][up_right].color != "w":
                    possible_moves_list.append([up_right,i])
                    if board[i][up_right].color == "b":
                        break
                if board[i][up_right].color == "w":
                    break

            if board[i][up_right] == None:
                possible_moves_list.append([up_right, i])

        up_right += 1

    for i in range((row - 1), -1, -1):
        if up_left > -1:
            if board[i][up_left] != None:
                if board[i][up_left].color != "w":
                    possible_moves_list.append([up_left,i])
                    if board[i][up_left].color == "b":
                        break
                if board[i][up_left].color == "w":
                    break
            if board[i][up_left] == None:
                possible_moves_list.append([up_left, i])
            up_left -= 1

    #Go down left or down right
    down_right = col + 1
    down_left = col - 1
    for i in range((row + 1), 8,+1):
        if down_right < 8:
            if board[i][down_right] != None:
                if board[i][down_right].color != "w":
                    possible_moves_list.append([down_right,i])
                    if board[i][down_right].color == "b":
                        break
                if board[i][down_right].color == "w":
                    break
            if board[i][down_right] == None:
                possible_moves_list.append([down_right, i])
        down_right += 1

    for i in range((row + 1), 8, +1):
        if down_left > -1:
            if board[i][down_left] != None:
                if board[i][down_left].color != "w":
                    possible_moves_list.append([down_left,i])
                    if board[i][down_left].color == "b":
                        break
                if board[i][down_left].color == "w":
                    break
            if board[i][down_left] == None:
                possible_moves_list.append([down_left, i])
            down_left -= 1

#For black
if color == "b":

    # Go up right or up left
    up_right = col + 1
    up_left = col - 1
    for i in range((row - 1), -1, -1):
        if up_right < 8:
            if board[i][up_right] != None:
                if board[i][up_right].color != "b":
                    possible_moves_list.append([up_right, i])

                    if board[i][up_right].color == "w":
                        break
                if board[i][up_right].color == "b":
                    break

            if board[i][up_right] == None:
                possible_moves_list.append([up_right, i])

        up_right += 1

    for i in range((row - 1), -1, -1):
        if up_left > -1:
            if board[i][up_left] != None:
                if board[i][up_left].color != "b":
                    possible_moves_list.append([up_left, i])
                    if board[i][up_left].color == "w":
                        break
                if board[i][up_left].color == "b":
                    break
            if board[i][up_left] == None:
                possible_moves_list.append([up_left, i])
            up_left -= 1

    # Go down left or down right
    down_right = col + 1
    down_left = col - 1
    for i in range((row + 1), 8, +1):
        if down_right < 8:
            if board[i][down_right] != None:
                if board[i][down_right].color != "b":
                    possible_moves_list.append([down_right, i])
                    if board[i][down_right].color == "w":
                        break
                if board[i][down_right].color == "b":
                    break
            if board[i][down_right] == None:
                possible_moves_list.append([down_right, i])
        down_right += 1

    for i in range((row + 1), 8, +1):
        if down_left > -1:
            if board[i][down_left] != None:
                if board[i][down_left].color != "b":
                    possible_moves_list.append([down_left, i])
                    if board[i][down_left].color == "w":
                        break
                if board[i][down_left].color == "b":
                    break
            if board[i][down_left] == None:
                possible_moves_list.append([down_left, i])
            down_left -= 1

    # Go up right or up left
    up_right = col + 1
    up_left = col - 1
    for i in range((row - 1), -1, -1):
        if up_right < 8:
            if board[i][up_right] != None:
                if board[i][up_right].color != "b":
                    possible_moves_list.append([up_right, i])
                if board[i][up_right].color == "w":
                    break
                if board[i][up_right].color == "b":
                    break

            if board[i][up_right] == None:
                possible_moves_list.append([up_right, i])
        up_right += 1

        if up_left > -1:
            if board[i][up_left] != None:
                if board[i][up_left].color != "b":
                    possible_moves_list.append([up_left, i])
                if board[i][up_left].color == "w":
                    break
                if board[i][up_left].color == "b":
                    break
            if board[i][up_left] == None:
                possible_moves_list.append([up_left, i])
            up_left -= 1

    # Go down left or down right
    down_right = col + 1
    down_left = col - 1
    for i in range((row + 1), 8, +1):
        if down_right < 8:
            if board[i][down_right] != None:
                if board[i][down_right].color != "b":
                    possible_moves_list.append([down_right, i])
                if board[i][down_right].color == "w":
                    break
                if board[i][down_right].color == "b":
                    break
            if board[i][down_right] == None:
                possible_moves_list.append([down_right, i])
        down_right += 1

        if down_left > -1:
            if board[i][down_left] != None:
                if board[i][down_left].color != "b":
                    possible_moves_list.append([down_left, i])
                if board[i][down_left].color == "w":
                    break
                if board[i][down_left].color == "b":
                    break
            if board[i][down_left] == None:
                possible_moves_list.append([down_left, i])
        down_left -= 1
'''

#Move black
'''
    def move_black(self, move):
        if self.board[move.stSqRow][move.stSqCol] is not None and not self.whiteToMove:

            possible_moves = self.board[move.stSqRow][move.stSqCol].possible_moves((move.stSqCol, move.stSqRow),
                                                                           self.board)
            if self.board[move.stSqRow][move.stSqCol].color == "b":
                if self.board[move.endSqRow][move.endSqCol] != None:
                    if self.board[move.endSqRow][move.endSqCol].color != "b":  # Piece which is not black is clicked
                        if self.board[move.endSqRow][move.endSqCol].color == "b":
                            self.whiteToMove = True
                        if [move.endSqCol, move.endSqRow] in possible_moves:
                            self.board[move.stSqRow][move.stSqCol] = None
                            self.board[move.endSqRow][move.endSqCol] = move.pieceMoved
                            moving_sound.play()
                            self.move_list.append(move)
                            self.whiteToMove = True


                if self.board[move.endSqRow][move.endSqCol] == None and not self.whiteToMove:  # A square without a piece on it is clicked
                    if [move.endSqCol, move.endSqRow] in possible_moves:
                        self.board[move.stSqRow][move.stSqCol] = None
                        self.board[move.endSqRow][move.endSqCol] = move.pieceMoved
                        moving_sound.play()
                        self.move_list.append(move)
                        self.whiteToMove = True
    '''

#If white is clicked
'''
                        #If white piece is clicked, simply let whiteToMove stay True
                        if self.board[move.endSqRow][move.endSqCol].color == "w":
                            self.whiteToMove = True
                        '''

list = [x for x in range(8)]
print(list)

"""
This file is going to keep track of the current state of the board with its pieces on it in the GameState Class.
It will also save every move made so that the Game afterwards can be looked at.
"""

import pygame
import time

#Initialize pygame
pygame.init()

#Initialize mixer module for sounds
pygame.mixer.init()

from lucapiece2 import br
from lucapiece2 import bkn
from lucapiece2 import bb
from lucapiece2 import bq
from lucapiece2 import bk
from lucapiece2 import bp

from lucapiece2 import wr
from lucapiece2 import wkn
from lucapiece2 import wb
from lucapiece2 import wq
from lucapiece2 import wk
from lucapiece2 import wp

#Set dimensions of the screen
WIDTH = 800
HEIGHT = 800

#Size of a square
SQUARE = WIDTH//8 or HEIGHT//8

#Set a display screen
DISPLAY_SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Luca de Pietro Chess Game")

#RGB Colors
WHITE = (255,255,255)
OPTIONAL = (100,100,100)
RED = (255,0,0)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)

#Chess Sounds
moving_sound = pygame.mixer.Sound("Chess_move.wav")
alert_sound = pygame.mixer.Sound("Chess_alert.wav")



#The color of the dark squares is optional. Thus the user can change it.
def draw_board(OPTIONAL):
    for i in range(8):
        for j in range(8):
            if i %2 == 0 and j %2 != 0:
                pygame.draw.rect(DISPLAY_SCREEN,(OPTIONAL),((SQUARE*i),(SQUARE*j),SQUARE,SQUARE))
            if i %2 != 0 and j %2 != 0:
                pygame.draw.rect(DISPLAY_SCREEN, (OPTIONAL), ((SQUARE * i), ((SQUARE * j)-SQUARE), SQUARE, SQUARE))

#Set a Font type
font = pygame.font.SysFont("consolas",20)

#Convert numbers from 97 to 104 to letters (a-h)
letter_image_list =[]
letter_rect_list = []
for i in range(97,105):
    text_image = font.render(chr(i), True, (0, 0, 0))
    letter_image_list.append(text_image)
    for j in range(8):
        text_rect = text_image.get_rect()
        text_rect.topright = ((j*100+100),700)
        letter_rect_list.append(text_rect)

#Describe the fields in a chess likely notation
def describe_fields():
    #Column description
    for i in range(8):
            DISPLAY_SCREEN.blit(letter_image_list[i], letter_rect_list[i])

    # Row description
    for i in range(1, 9):
        i_text = font.render(str(i), True, (0, 0, 0))
        i_rect = i_text.get_rect()
        i_rect.topleft = (0, (800 - (i * 100)))
        DISPLAY_SCREEN.blit(i_text, i_rect)



'''
The Game State Class will keep track of the location of each piece. A square without a piece on it is defined as a None
square. This 2 dimensional grid allows an efficient way of checking the type of each piece and thus which moves can be
played in regards to the other pieces on the board. Careful: the row value is given first when accessing the grid 
(self.board[row][col]).
'''

class GameState():


    def __init__(self):
        self.board = [
            [br, bkn, bb, bq, bk, bb, bkn, br],
            [bp, bp,  bp, bp, bp, bp, bp,  bp],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [wp, wp,  wp, wp, wp, wp, wp,  wp],
            [wr, wkn, wb, wq, wk, wb, wkn, wr],
        ]
        self.move_list = []
        self.whiteToMove = True
        self.white_king_start = [4,7]
        self.black_king_start = [4,0]
        self.inCheck = False
        self.inPin = False
        self.GameOverW = False
        self.GameOverB = False
        self.CastleShortW = False
        self.CastleShortB = False
        self.CastleLongW = False
        self.CastleLongB = False


    def check_for_nonesquare(self, click, list):
        if len(list) == 1:
            if self.board[click[1]][click[0]] is None: #Is a none square clicked before a piece?
                list.clear()
        if len(list) == 3:
            if self.board[list[2][1]][list[2][0]] is None: #Is a none square clicked after a piece has moved?
                list.clear()
            if len(list) != 0:
                if self.board[list[2][1]][list[2][0]] is not None:
                    list.clear()
                    list.append(click)

    def check_for_doubleclicks(self,click, list):

        if len(list) == 2:
            if self.board[list[0][1]][list[0][0]] != None:
                possible_moves = self.board[list[0][1]][list[0][0]].possible_moves((list[0][0], list[0][1]), self.board)
                if self.board[click[1]][click[0]] != None:
                    #Are pieces with the same color clicked, clear list and append the new click
                    if self.board[list[1][1]][list[1][0]].color == self.board[list[0][1]][list[0][0]].color:
                        list.clear()
                        list.append(click)
                        return list
                    #Are pieces with opposite color clicked, do the same as above
                    if self.board[list[1][1]][list[1][0]].color != self.board[list[0][1]][list[0][0]].color:
                        if [list[1][0],list[1][1]] not in possible_moves:
                            list.clear()
                            list.append(click)
                        else:
                            list.pop()
                            list.append(click)

    def king_coordinates_white(self):
        #White Kings coordinates
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != None:
                    if self.board[i][j] == wk:
                        wking_coordinates = [j, i]
                        return wking_coordinates

    def king_coordinates_black(self):
        #Black Kings coordinates
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != None:
                    if self.board[i][j] == bk:
                        bking_coordinates = [j, i]
                        return bking_coordinates
    '''
    def get_valid_moves(self, white_king, black_king):
        #Check if the possible moves lead to check
        for i in range(8): #i for row
            for j in range(8): #j for col
                if self.board[i][j] is not None:
                    #Generate all possible moves for white
                    if self.board[i][j].color == "w":
                        possible_moves_w = self.board[i][j].possible_moves((j, i), self.board)
                        if [black_king[0],black_king[1]] in possible_moves_w:
                            self.board[black_king[1]][black_king[0]].BlackInCheck = True
                            alert_sound.play()

                    # Generate all possible moves for black
                    if self.board[i][j].color == "b":
                        possible_moves_b = self.board[i][j].possible_moves((j, i), self.board)
                        if [white_king[0], white_king[1]] in possible_moves_b:
                            self.board[white_king[1]][white_king[0]].WhiteInCheck = True
                            alert_sound.play()
    '''

    def is_king_in_check(self):
        #Check if the possible moves lead to check
        for i in range(8): #i for row
            for j in range(8): #j for col
                if self.board[i][j] is not None:
                    #Generate all possible moves for white
                    if self.board[i][j].color == "w":
                        possible_moves_w = self.board[i][j].possible_moves((j, i), self.board)
                        if [self.black_king_start[0], self.black_king_start[1]] in possible_moves_w:
                            self.board[self.black_king_start[1]][self.black_king_start[0]].BlackInCheck = True
                        else:
                            self.board[self.black_king_start[1]][self.black_king_start[0]].BlackInCheck = False


                    # Generate all possible moves for black
                    if self.board[i][j].color == "b":
                        possible_moves_b = self.board[i][j].possible_moves((j, i), self.board)
                        if [self.white_king_start[0], self.white_king_start[1]] in possible_moves_b:
                            self.board[self.white_king_start[1]][self.white_king_start[0]].WhiteInCheck = True
                        else:
                            self.board[self.white_king_start[1]][self.white_king_start[0]].WhiteInCheck = False



    def white_in_check(self,wx,wy):
        surface = pygame.Surface((SQUARE, SQUARE))
        # Choose the transparency
        surface.set_alpha(80)
        surface.fill(pygame.Color("red"))
        DISPLAY_SCREEN.blit(surface, (wx * 100, wy * 100))

    def black_in_check(self, bx, by):
        surface = pygame.Surface((SQUARE, SQUARE))
        # Choose the transparency
        surface.set_alpha(80)
        surface.fill(pygame.Color("red"))
        DISPLAY_SCREEN.blit(surface, (bx * 100, by * 100))


    def check_for_castling(self):
        #Check for the white king
        for j in range(8):
            for i in range(8):
                if self.board[j][i] is not None:
                    if self.board[j][i] == wk:
                        #Check for short castling
                        if self.board[j][5] is None and self.board[j][6] is None:
                            self.CastleShortW = True
                        #Check for long castling
                        if self.board[j][1] is None and self.board[j][2] is None and self.board[j][3] is None:
                            self.CastleLongW = True

        #Check for the black king
        for j in range(8):
            for i in range(8):
                if self.board[j][i] is not None:
                    if self.board[j][i] == bk:
                        #Check for short castling
                        if self.board[j][5] is None and self.board[j][6] is None:
                            self.CastleShortB = True
                        #Check for long castling
                        if self.board[j][1] is None and self.board[j][2] is None and self.board[j][3] is None:
                            self.CastleLongB = True


    '''
    The move_piece function will set the rules for moving a piece . It takes the two squares of the move (start and end) 
    and will execute the move by moving the piece. If the piece is moved, it will leave a None square behind. This is 
    crucial for making the game going. 
    '''

    def move_piece(self, move):

        #A white piece is being clicked
        if self.board[move.stSqRow][move.stSqCol] is not None and self.whiteToMove:
            #possible_moves generated from Piece Class at specific click location
            possible_moves = self.board[move.stSqRow][move.stSqCol].possible_moves((move.stSqCol, move.stSqRow),
                                                                                   self.board)

            if self.board[move.stSqRow][move.stSqCol].color == "w":
                #Check if either the king or rook has moved once, then castling is not possible anymore
                if self.board[move.stSqRow][move.stSqCol] == wk:
                    self.white_king_start = [move.endSqRow, move.endSqCol]
                    if [move.endSqRow,move.endSqCol] != [7,6]:
                        self.CastleShortW = False
                    if [move.endSqRow,move.endSqCol] != [7,2]:
                        self.CastleLongW = False

                #Pawn promotion
                if self.board[move.stSqRow][move.stSqCol] == wp:
                    if move.endSqRow == 0:
                        self.board[move.stSqRow][move.stSqCol] = None
                        self.board[0][move.endSqCol] = wq
                        self.whiteToMove = not self.whiteToMove
                '''
                #Store the location of the white king
                if self.board[move.stSqRow][move.stSqCol] == wk:
                    self.white_king_start = [move.endSqCol, move.endSqRow]
                '''

                if self.board[move.endSqRow][move.endSqCol] is not None:
                    #Piece which is not white is clicked
                    if self.board[move.endSqRow][move.endSqCol].color != "w":
                        #Check if black piece is in possible_moves; if so, then capture and leave a None square behind
                        if [move.endSqCol, move.endSqRow] in possible_moves:
                            # Black King is captured
                            if self.board[move.endSqRow][move.endSqCol] == bk:
                                self.GameOverB = True
                            #Other Pieces are captured
                            self.board[move.stSqRow][move.stSqCol] = None
                            self.board[move.endSqRow][move.endSqCol] = move.pieceMoved
                            moving_sound.play()
                            self.move_list.append(move)
                            self.whiteToMove = not self.whiteToMove



                #A square without a piece on it is clicked
                if self.board[move.endSqRow][move.endSqCol] is None:
                    if self.board[move.stSqRow][move.stSqCol] == wk:
                        #Castle Short
                        if self.CastleShortW:
                            if move.endSqRow == 7 and move.endSqCol == 6:
                                #Move the king
                                self.board[7][6] = wk
                                self.board[move.stSqRow][move.stSqCol] = None
                                #Move the rook
                                self.board[7][5] = wr
                                self.board[7][7] = None
                                self.whiteToMove = not self.whiteToMove
                        #Castle long
                        if self.CastleLongW:
                            if move.endSqRow == 7 and move.endSqCol == 2:
                                #Move the king
                                self.board[7][2] = wk
                                self.board[move.stSqRow][move.stSqCol] = None
                                #Move the rook
                                self.board[7][3] = wr
                                self.board[7][0] = None
                                self.whiteToMove = not self.whiteToMove



                    if [move.endSqCol, move.endSqRow] in possible_moves:
                        self.board[move.stSqRow][move.stSqCol] = None
                        self.board[move.endSqRow][move.endSqCol] = move.pieceMoved
                        moving_sound.play()
                        self.move_list.append(move)
                        self.whiteToMove = not self.whiteToMove
                        self.board[move.endSqRow][move.endSqCol].selected = False

        #A black piece is being clicked
        if self.board[move.stSqRow][move.stSqCol] is not None and not self.whiteToMove:

            possible_moves = self.board[move.stSqRow][move.stSqCol].possible_moves((move.stSqCol, move.stSqRow),
                                                                           self.board)
            if self.board[move.stSqRow][move.stSqCol].color == "b":
                # Check if either the king or rook has moved once, then castling is not possible anymore
                if self.board[move.stSqRow][move.stSqCol] == bk:
                    self.black_king_start = [move.endSqRow, move.endSqCol]
                    if [move.endSqRow, move.endSqCol] != [0, 6]:
                        self.CastleShortB = False
                    if [move.endSqRow,move.endSqCol] != [0,2]:
                        self.CastleLongB = False
                #Pawn promotion
                if self.board[move.stSqRow][move.stSqCol] == bp:
                    if move.endSqRow == 7:
                        self.board[move.stSqRow][move.stSqCol] = None
                        self.board[7][move.endSqCol] = bq
                        self.whiteToMove = True

                if self.board[move.endSqRow][move.endSqCol] is not None:
                    #Piece which is not black is clicked
                    if self.board[move.endSqRow][move.endSqCol].color != "b":
                        if self.board[move.endSqRow][move.endSqCol].color == "b":
                            self.whiteToMove = True
                        if [move.endSqCol, move.endSqRow] in possible_moves:
                            # Whtie King is captured
                            if self.board[move.endSqRow][move.endSqCol] == wk:
                                self.GameOverW = True
                            #Other pieces are captured
                            self.board[move.stSqRow][move.stSqCol] = None
                            self.board[move.endSqRow][move.endSqCol] = move.pieceMoved
                            moving_sound.play()
                            self.move_list.append(move)
                            self.whiteToMove = True


                if self.board[move.endSqRow][move.endSqCol] is None and not self.whiteToMove:
                    if self.board[move.stSqRow][move.stSqCol] == bk:
                        #Castle Short
                        if self.CastleShortB:
                            if move.endSqRow == 0 and move.endSqCol == 6:
                                #Move the king
                                self.board[0][6] = bk
                                self.board[move.stSqRow][move.stSqCol] = None
                                #Move the rook
                                self.board[0][5] = br
                                self.board[0][7] = None
                                self.whiteToMove = True
                        # Castle long
                        if self.CastleLongB:
                            if move.endSqRow == 0 and move.endSqCol == 2:
                                # Move the king
                                self.board[0][2] = bk
                                self.board[move.stSqRow][move.stSqCol] = None
                                # Move the rook
                                self.board[0][3] = br
                                self.board[0][0] = None
                                self.whiteToMove = not self.whiteToMove

                    if [move.endSqCol, move.endSqRow] in possible_moves:
                        self.board[move.stSqRow][move.stSqCol] = None
                        self.board[move.endSqRow][move.endSqCol] = move.pieceMoved
                        moving_sound.play()
                        self.move_list.append(move)
                        self.whiteToMove = True

    "***"
    def return_move(self):
        if len(self.move_list) != 0:
            move = self.move_list.pop()

            self.board[move.stSqRow][move.stSqCol] = move.pieceMoved
            self.board[move.endSqRow][move.endSqCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

    def draw_pieces(self):
        for j in range(8): # j for row
            for i in range(8): # i for col
                if self.board[j][i] != None:
                    piece_image = pygame.image.load(self.board[j][i].image) #Get the image file name "Piece.png"
                    piece_scaled = pygame.transform.scale(piece_image,(SQUARE,SQUARE)) #Scale the image to square size

                    #Blit the scaled images on the board
                    DISPLAY_SCREEN.blit(piece_scaled, pygame.Rect(i*SQUARE, j*SQUARE,SQUARE,SQUARE))

    #When the game is restarted or over, simply reset the board
    def restart_game(self):
        self.board = [
            [br, bkn, bb, bq, bk, bb, bkn, br],
            [bp, bp, bp, bp, bp, bp, bp, bp],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [wp, wp, wp, wp, wp, wp, wp, wp],
            [wr, wkn, wb, wq, wk, wb, wkn, wr],
        ]
        self.move_list = []
        self.whiteToMove = True
        self.white_king_start = [4, 7]
        self.black_king_start = [0, 7]
        self.inCheck = False
        self.inPin = False

    '''
    def game_over(self, white_king, black_king):
        #White has won
        for i in range(8):
            for j in range(8):
                if self.board[j][i] is not None:
                    if self.board[j][i] == bk:
                        if [i,j] == [black_king[0], black_king[1]]:
                            print("king alive")
                        if [i,j] != [black_king[0], black_king[1]]:
                            print("king dead")
    '''

    #Select each piece by clicking on it to show its possible moves, if it is that piece's turn
    def select(self, list, board):

        if board[list[0][1]][list[0][0]] != None: #Careful: Row and col in self.board are board[row][col]
            if board[list[0][1]][list[0][0]].color == "w" and self.whiteToMove:
                board[list[0][1]][list[0][0]].selected = True
                board[list[0][1]][list[0][0]].select_piece(list[0])
                board[list[0][1]][list[0][0]].possible_moves(list[0], self.board)

                for move in board[list[0][1]][list[0][0]].possible_moves(list[0], self.board):
                    pygame.draw.circle(DISPLAY_SCREEN, (200,200,203), (move[0] * 100 + 50, move[1] * 100 + 50), 25)

            if board[list[0][1]][list[0][0]].color == "b" and not self.whiteToMove:
                board[list[0][1]][list[0][0]].selected = True
                board[list[0][1]][list[0][0]].select_piece(list[0])
                board[list[0][1]][list[0][0]].possible_moves(list[0], self.board)

                for move in board[list[0][1]][list[0][0]].possible_moves(list[0], self.board):
                    pygame.draw.circle(DISPLAY_SCREEN, (200,200,203), (move[0] * 100 + 50, move[1] * 100 + 50), 25)

'''
The move class will save the row and column values of each added sqaure in the player_move_destination list. It allows
an simple usage of the different start and end squares of each move. 
'''

#With inspirations from Eddie Sharick's video: Chess Engine in Python - Part 2 - Moving the pieces
class Move():
    def __init__(self, start_square, end_square, board):
        self.stSqCol = start_square[0]
        self.stSqRow = start_square[1]
        self.endSqCol = end_square[0]
        self.endSqRow = end_square[1]
        self.pieceMoved = board[self.stSqRow][self.stSqCol]
        self.pieceCaptured = board[self.endSqRow][self.endSqCol]






