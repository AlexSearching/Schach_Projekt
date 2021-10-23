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
moving_sound = pygame.mixer.Sound("Chess_move.wav") #Downloaded from https://freesound.org/people/mh2o/sounds/351518/
alert_sound = pygame.mixer.Sound("Chess_alert.wav") #Download from https://freesound.org/people/JustinBW/sounds/80921/
capture_sound = pygame.mixer.Sound("Capture_sound2.wav") #Download from https://github.com/ornicar/lila/blob/master/public/sound/lisp/Capture.mp3
castling_sound = pygame.mixer.Sound("Castling_sound.mp3") #Download from https://github.com/ornicar/lila/blob/master/public/sound/lisp/Castles.mp3
defeat_sound = pygame.mixer.Sound("Defeat_sound.mp3") #Download from https://github.com/ornicar/lila/blob/master/public/sound/lisp/Defeat.mp3

#The color of the dark squares is optional, thus the user can change it where the function is executed (lucamain2.py)
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
        self.white_king_start = [4,7]
        self.black_king_start = [4,0]
        self.GameOverW = False
        self.GameOverB = False
        self.CastleShortW = False
        self.CastleShortB = False
        self.CastleLongW = False
        self.CastleLongB = False

    def check_for_nonesquare(self, click, list):
        if len(list) == 1:
            # Is a none square clicked before a piece?
            if self.board[click[1]][click[0]] is None:
                list.clear()
        if len(list) == 3:
            # Is a none square clicked after a piece has moved?
            if self.board[list[2][1]][list[2][0]] is None:
                list.clear()
            if len(list) != 0:
                if self.board[list[2][1]][list[2][0]] is not None:
                    list.clear()
                    list.append(click)

    def check_for_doubleclicks(self,click, list):
        if len(list) == 2:
            if self.board[list[0][1]][list[0][0]] is not None:
                possible_moves = self.board[list[0][1]][list[0][0]].possible_moves((list[0][0], list[0][1]), self.board)
                if self.board[click[1]][click[0]] is not None:
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
                if self.board[i][j] is not None:
                    if self.board[i][j] == wk:
                        wking_coordinates = [j, i]
                        return wking_coordinates

    def king_coordinates_black(self):
        #Black Kings coordinates
        for i in range(8):
            for j in range(8):
                if self.board[i][j] is not None:
                    if self.board[i][j] == bk:
                        bking_coordinates = [j, i]
                        return bking_coordinates

    def threat_moves_black(self):
        #Create all possible moves for black
        possible_threat_moves_black = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] is not None:
                    if self.board[i][j].color == "b":
                        possible_moves_b = self.board[i][j].possible_moves((j, i), self.board)
                        for move in possible_moves_b:
                            possible_threat_moves_black.append(move)
        return possible_threat_moves_black

    def threat_moves_white(self):
        #Create all possible moves for white
        possible_threat_moves_white = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] is not None:
                    if self.board[i][j].color == "w":
                        possible_moves_w = self.board[i][j].possible_moves((j, i), self.board)
                        for move in possible_moves_w:
                            possible_threat_moves_white.append(move)
        return possible_threat_moves_white

    def king_in_check(self):
        #If the white king is in one of the possible moves of black, he is in check
        danger_moves_b = self.threat_moves_black()
        if [self.white_king_start[0],self.white_king_start[1]] in danger_moves_b:
            wk.WhiteInCheck = True
            self.CastleShortW = False
            self.CastleLongW = False
        else:
            wk.WhiteInCheck = False

        #If the white king is in one of the possible moves of black, he is in check
        danger_moves_w = self.threat_moves_white()
        if [self.black_king_start[0], self.black_king_start[1]] in danger_moves_w:
            bk.BlackInCheck = True
            self.CastleShortB = False
            self.CastleLongB = False
        else:
            bk.BlackInCheck = False

    def remove_king_moves(self):
        if wk.WhiteInCheck:
            king_row = self.white_king_start[1]
            king_col = self.white_king_start[0]
            enemy_moves = self.threat_moves_black()
            king_moves = self.board[king_row][king_col].possible_moves((king_col, king_row), self.board)
            for moves in king_moves:
                for e_moves in enemy_moves:
                    if [moves[0], moves[1]] == [e_moves[0], e_moves[1]]:
                        print([moves[0], moves[1]])
                        king_moves.remove([moves[0], moves[1]])
                        print(king_moves)

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

        if self.board[move.stSqRow][move.stSqCol] is not None and self.whiteToMove:
            #possible_moves generated from Piece Class at specific click location
            possible_moves = self.board[move.stSqRow][move.stSqCol].possible_moves((move.stSqCol, move.stSqRow),
                                                                                   self.board)
            # A white piece is being clicked
            if self.board[move.stSqRow][move.stSqCol].color == "w":

                 #Check if either the king or rook has moved once, then castling is not possible anymore
                if self.board[move.stSqRow][move.stSqCol] == wk:
                    self.white_king_start = [move.endSqCol, move.endSqRow]
                    if [move.endSqRow,move.endSqCol] != [7,6]:
                        self.CastleShortW = False
                        moving_sound.play()
                    if [move.endSqRow,move.endSqCol] != [7,2]:
                        self.CastleLongW = False
                        moving_sound.play()

                #Pawn promotion white
                if self.board[move.stSqRow][move.stSqCol] == wp:
                    if [move.endSqCol, move.endSqRow] in possible_moves:
                        if move.endSqRow == 0:
                            self.board[move.stSqRow][move.stSqCol] = None
                            self.board[0][move.endSqCol] = wq
                            moving_sound.play()
                            self.whiteToMove = not self.whiteToMove

                if self.board[move.endSqRow][move.endSqCol] is not None:
                    #Piece which is not white is clicked
                    if self.board[move.endSqRow][move.endSqCol].color != "w":
                        #Check if black piece is in possible_moves; if so, then capture and leave a None square behind
                        if [move.endSqCol, move.endSqRow] in possible_moves:
                            # Black King is captured
                            if self.board[move.endSqRow][move.endSqCol] == bk:
                                self.GameOverB = True
                                defeat_sound.play()

                            #Other Pieces are captured
                            self.board[move.stSqRow][move.stSqCol] = None
                            self.board[move.endSqRow][move.endSqCol] = move.pieceMoved
                            capture_sound.play()
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
                                castling_sound.play()
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
                                castling_sound.play()
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
                #Check if either the king or rook has moved once, then castling is not possible anymore
                if self.board[move.stSqRow][move.stSqCol] == bk:
                    self.black_king_start = [move.endSqCol, move.endSqRow]
                    if [move.endSqRow, move.endSqCol] != [0, 6]:
                        self.CastleShortB = False
                        moving_sound.play()
                    if [move.endSqRow,move.endSqCol] != [0,2]:
                        self.CastleLongB = False
                        moving_sound.play()
                #Pawn promotion black
                if self.board[move.stSqRow][move.stSqCol] == bp:
                    if [move.endSqCol, move.endSqRow] in possible_moves:
                        if move.endSqRow == 7:
                            self.board[move.stSqRow][move.stSqCol] = None
                            self.board[7][move.endSqCol] = bq
                            moving_sound.play()
                            self.whiteToMove =  True

                if self.board[move.endSqRow][move.endSqCol] is not None:
                    #Piece which is not black is clicked
                    if self.board[move.endSqRow][move.endSqCol].color != "b":
                        if self.board[move.endSqRow][move.endSqCol].color == "b":
                            self.whiteToMove = True
                        if [move.endSqCol, move.endSqRow] in possible_moves:
                            # Whtie King is captured
                            if self.board[move.endSqRow][move.endSqCol] == wk:
                                self.GameOverW = True
                                defeat_sound.play()

                            #Other pieces are captured
                            self.board[move.stSqRow][move.stSqCol] = None
                            self.board[move.endSqRow][move.endSqCol] = move.pieceMoved
                            capture_sound.play()
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
                                castling_sound.play()
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
                                castling_sound.play()
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

    def draw_pieces(self):
        for j in range(8): # j for row
            for i in range(8): # i for col
                if self.board[j][i] is not None:
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
        self.black_king_start = [4, 0]
        self.GameOverW = False
        self.GameOverB = False
        self.CastleShortW = False
        self.CastleShortB = False
        self.CastleLongW = False
        self.CastleLongB = False

    #Select each piece by clicking on it to show its possible moves, if it is that piece's turn
    def select(self, list, board):

        if board[list[0][1]][list[0][0]] is not None: #Careful: Row and col in self.board are board[row][col]
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

#With inspirations from Eddie Sharick's video: Chess Engine in Python - Part 2 - Moving the pieces (https://www.youtube.com/watch?v=o24J3WcBGLg&t=1765s&ab_channel=EddieSharick)
class Move():
    def __init__(self, start_square, end_square, board):
        self.stSqCol = start_square[0]
        self.stSqRow = start_square[1]
        self.endSqCol = end_square[0]
        self.endSqRow = end_square[1]
        self.pieceMoved = board[self.stSqRow][self.stSqCol]
        self.pieceCaptured = board[self.endSqRow][self.endSqCol]






