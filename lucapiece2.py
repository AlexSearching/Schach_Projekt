"""
This file is going to set the class for the pieces. It will set the information needed to define each piece.
"""

import pygame

#Set Dimensions
WIDTH = 800
HEIGHT = 800

#Size of a square
SQUARE = WIDTH//8 or HEIGHT//8

#Initialize pygame
pygame.init()

#Set a display screen
DISPLAY_SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Luca de Pietro Chess Game")

#RGB Colors
WHITE = (255,255,255)
OPTIONAL = (200,200,203)
RED = (255,0,0)
GREY = (128, 128, 128)
ORANGE = (255, 160, 0)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)

'''
Every piece is defined by its color, its type and its image. The Piece parent class will give each piece its basic
characteristics. It will mainly check if a piece is selected and will then mark the square around the piece for the user.
'''

class Piece:
    def __init__(self, color, type, image):
        self.color = color
        self.type = type
        self.image = image
        self.selected = False

    def select_piece(self, click): #The click essentially will give us the piece's location
        if self.selected:
            surface = pygame.Surface((SQUARE, SQUARE))
            #Choose the transparency
            surface.set_alpha(80)
            surface.fill(pygame.Color("grey"))
            #Mark the square which the piece is on
            DISPLAY_SCREEN.blit(surface,(click[0]*SQUARE, click[1]*SQUARE) )

'''
Every piece has its own way of moving. Therefore it is crucial to differentiate between those types of moving and check 
for all possible moves. The possible_moves_list will store every move that can be made and will be used in the 
lucaboard2 file to check, whether a move can be made or not.
'''

class Rook(Piece):

    def possible_moves(self, click, board):
        col = click[0]  #Rounded math.floor value of the x-coordinate
        row = click[1]  #Rounded math.floor value of the y-coordinate

        possible_moves_list = [] #First value for col, second for row

        #Go left
        if col > 0:
            for i in range((col - 1), -1, -1):
                if board[row][i] is not None:
                    if board[row][col] is not None:
                        if board[row][i].color != board[row][col].color: #Enemy piece
                            possible_moves_list.append([i,row])
                            break
                        else:
                            break

                if board[row][i] is None:
                    possible_moves_list.append([i, row])

        #Go right
        if col < 7:
            for i in range((col + 1), 8, +1):
                if board[row][i] is not None:
                    if board[row][col] is not None:
                        if board[row][i].color != board[row][col].color:
                            possible_moves_list.append([i, row])
                            break
                        else:
                            break
                if board[row][i] is None:
                    possible_moves_list.append([i, row])

        #Go up
        if row > 0:
            for i in range((row - 1), -1, -1):
                if board[i][col] is not None:
                    if board[row][col] is not None:
                        if board[i][col].color != board[row][col].color:
                            possible_moves_list.append([col, i])
                            break
                        else:
                            break
                if board[i][col] is None:
                    possible_moves_list.append([col, i])


        #Go down
        if row < 7:
            for i in range((row + 1), 8, +1):
                if board[i][col] is not None:
                    if board[row][col] is not None:
                        if board[i][col].color != board[row][col].color:
                            possible_moves_list.append([col, i])
                            break
                        else:
                            break
                if board[i][col] is None:
                    possible_moves_list.append([col, i])

        #Return the list of possible moves
        return possible_moves_list

class Knight(Piece):

    def possible_moves(self, click, board):
        col = click[0]
        row = click[1]

        possible_moves_list = []

        #Up and left
        if row >= 2 and col > 0:
            if board[row - 2][col - 1] is not None:
                if board[row][col] is not None:
                    if board[row - 2][col - 1].color != board[row][col].color:
                        possible_moves_list.append([col - 1, row - 2])
            if board[row - 2][col - 1] is None:
                possible_moves_list.append([col - 1, row - 2])

        #Up and right
        if row >= 2 and col < 7:
            if board[row - 2][col + 1] is not None:
                if board[row][col] is not None:
                    if board[row - 2][col + 1].color != board[row][col].color :
                        possible_moves_list.append([col + 1, row - 2])
            if board[row - 2][col + 1] is None:
                possible_moves_list.append([col + 1, row - 2])

        #Left and up
        if row > 0 and col >= 2:
            if board[row - 1][col - 2] is not None:
                if board[row][col] is not None:
                    if board[row - 1][col - 2].color != board[row][col].color:
                        possible_moves_list.append([col - 2, row - 1])
            if board[row - 1][col - 2] is None:
                possible_moves_list.append([col - 2, row - 1])

        #Left and down
        if row < 7 and col >= 2:
            if board[row + 1][col - 2] is not None:
                if board[row][col] is not None:
                    if board[row + 1][col - 2].color != board[row][col].color:
                        possible_moves_list.append([col - 2, row + 1])
            if board[row + 1][col - 2] is None:
                possible_moves_list.append([col - 2, row + 1])

        #Down and left
        if row < 6 and col > 0:
            if board[row + 2][col - 1] is not None:
                if board[row][col] is not None:
                    if board[row + 2][col - 1].color != board[row][col].color:
                        possible_moves_list.append([col - 1, row + 2])
            if board[row + 2][col - 1] is None:
                possible_moves_list.append([col - 1, row + 2])

        #Down and right
        if row < 6 and col < 7:
            if board[row + 2][col + 1] is not None:
                if board[row][col] is not None:
                    if board[row + 2][col + 1].color != board[row][col].color:
                        possible_moves_list.append([col + 1, row + 2])
            if board[row + 2][col + 1] is None:
                possible_moves_list.append([col + 1, row + 2])

        #Right and down
        if row < 7 and col < 6:
            if board[row + 1][col + 2] is not None:
                if board[row][col] is not None:
                    if board[row + 1][col + 2].color != board[row][col].color:
                        possible_moves_list.append([col + 2, row + 1])
            if board[row + 1][col + 2] is None:
                possible_moves_list.append([col + 2, row + 1])
        #Right and up
        if row > 0 and col < 6:
            if board[row - 1][col + 2] is not None:
                if board[row][col] is not None:
                    if board[row - 1][col + 2].color != board[row][col].color:
                        possible_moves_list.append([col + 2, row - 1])
            if board[row - 1][col + 2] is None:
                possible_moves_list.append([col + 2, row - 1])

        return possible_moves_list

class Bishop(Piece):

    #With inspirations from Tech with Tim's video: 24 Hour Coding Livestream - Creating an Online Chess Game With Python
    def possible_moves(self, click, board):
        color = self.color
        col = click[0]
        row = click[1]

        possible_moves_list = []

        # Go down left or down right
        down_right = col + 1
        down_left = col - 1
        for i in range((row + 1), 8, +1):
            if down_right < 8:
                if board[i][down_right] is not None:
                    if board[row][col] is not None:
                        if board[i][down_right].color != board[row][col].color:
                            possible_moves_list.append([down_right, i])
                            break
                        else:
                            break
                if board[i][down_right] is None:
                    possible_moves_list.append([down_right, i])
            down_right += 1

        for i in range((row + 1), 8, +1):
            if down_left > -1:
                if board[i][down_left] is not None:
                    if board[row][col] is not None:
                        if board[i][down_left].color != board[row][col].color:
                            possible_moves_list.append([down_left, i])
                            break
                        else:
                            break
                if board[i][down_left] is None:
                    possible_moves_list.append([down_left, i])
                down_left -= 1

        #Go up right or up left
        up_right = col + 1
        up_left = col - 1
        for i in range((row - 1), -1, -1):
            if up_right < 8:
                if board[i][up_right] is not None:
                    if board[row][col] is not None:
                        if board[i][up_right].color != board[row][col].color:
                            possible_moves_list.append([up_right, i])
                            break
                        else:
                            break


                if board[i][up_right] is None:
                    possible_moves_list.append([up_right, i])

            up_right += 1

        for i in range((row - 1), -1, -1):
            if up_left > -1:
                if board[i][up_left] is not None:
                    if board[row][col] is not None:
                        if board[i][up_left].color != board[row][col].color:
                            possible_moves_list.append([up_left, i])
                            break
                        else:
                            break

                if board[i][up_left] is None:
                    possible_moves_list.append([up_left, i])
                up_left -= 1

        return possible_moves_list

class Queen(Piece):

    def possible_moves(self, click, board):
        color = self.color
        col = click[0]
        row = click[1]

        possible_moves_list = []

        # Go left
        if col > 0:
            for i in range((col - 1), -1, -1):
                if board[row][i] is not None:
                    if board[row][col] is not None:
                        if board[row][i].color != board[row][col].color:  # Enemy piece
                            possible_moves_list.append([i, row])
                            break
                        else:
                            break

                if board[row][i] is None:
                    possible_moves_list.append([i, row])

        # Go right
        if col < 7:
            for i in range((col + 1), 8, +1):
                if board[row][i] is not None:
                    if board[row][col] is not None:
                        if board[row][i].color != board[row][col].color:
                            possible_moves_list.append([i, row])
                            break
                        else:
                            break
                if board[row][i] is None:
                    possible_moves_list.append([i, row])

        # Go up
        if row > 0:
            for i in range((row - 1), -1, -1):
                if board[i][col] is not None:
                    if board[row][col] is not None:
                        if board[i][col].color != board[row][col].color:
                            possible_moves_list.append([col, i])
                            break
                        else:
                            break
                if board[i][col] is None:
                    possible_moves_list.append([col, i])

        # Go down
        if row < 7:
            for i in range((row + 1), 8, +1):
                if board[i][col] is not None:
                    if board[row][col] is not None:
                        if board[i][col].color != board[row][col].color:
                            possible_moves_list.append([col, i])
                            break
                        else:
                            break
                if board[i][col] is None:
                    possible_moves_list.append([col, i])

        # Go down left or down right
        down_right = col + 1
        down_left = col - 1
        for i in range((row + 1), 8, +1):
            if down_right < 8:
                if board[i][down_right] is not None:
                    if board[row][col] is not None:
                        if board[i][down_right].color != board[row][col].color:
                            possible_moves_list.append([down_right, i])
                            break
                        else:
                            break
                if board[i][down_right] is None:
                    possible_moves_list.append([down_right, i])
            down_right += 1

        for i in range((row + 1), 8, +1):
            if down_left > -1:
                if board[i][down_left] is not None:
                    if board[row][col] is not None:
                        if board[i][down_left].color != board[row][col].color:
                            possible_moves_list.append([down_left, i])
                            break
                        else:
                            break
                if board[i][down_left] is None:
                    possible_moves_list.append([down_left, i])
                down_left -= 1

        # Go up right or up left
        up_right = col + 1
        up_left = col - 1
        for i in range((row - 1), -1, -1):
            if up_right < 8:
                if board[i][up_right] is not None:
                    if board[row][col] is not None:
                        if board[i][up_right].color != board[row][col].color:
                            possible_moves_list.append([up_right, i])
                            break
                        else:
                            break

                if board[i][up_right] is None:
                    possible_moves_list.append([up_right, i])
            up_right += 1

        for i in range((row - 1), -1, -1):
            if up_left > -1:
                if board[i][up_left] is not None:
                    if board[row][col] is not None:
                        if board[i][up_left].color != board[row][col].color:
                            possible_moves_list.append([up_left, i])
                            break
                        else:
                            break

                if board[i][up_left] is None:
                    possible_moves_list.append([up_left, i])
                up_left -= 1

        return possible_moves_list

class King(Piece):

    def __init__(self, color, type, image):
        super().__init__(color, type, image)
        self.BlackInCheck = False
        self.WhiteInCheck = False

    def possible_moves(self, click, board):
        col = click[0]
        row = click[1]


        possible_moves_list = []

        if self.WhiteInCheck == False or self.BlackInCheck == False:
            # Go up
            if row > 0:
                if board[row - 1][col] is not None:
                    if board[row][col] is not None:
                        if board[row - 1][col].color != board[row][col].color:
                            possible_moves_list.append([col, row - 1])
                if board[row - 1][col] is None:
                    possible_moves_list.append([col, row - 1])

            # Go up left
            if row > 0 and col > 0:
                if board[row - 1][col - 1] is not None:
                    if board[row][col] is not None:
                        if board[row - 1][col - 1].color != board[row][col].color:
                            possible_moves_list.append([col - 1, row - 1])
                if board[row - 1][col - 1] is None:
                    possible_moves_list.append([col - 1, row - 1])

            # Go left
            if col > 0:
                if board[row][col - 1] is not None:
                    if board[row][col] is not None:
                        if board[row][col - 1].color != board[row][col].color:
                            possible_moves_list.append([col - 1, row])
                if board[row][col - 1] is None:
                    possible_moves_list.append([col - 1, row])

            # Go left down
            if row < 7 and col > 0:
                if board[row + 1][col - 1] is not None:
                    if board[row][col] is not None:
                        if board[row + 1][col - 1].color != board[row][col].color:
                            possible_moves_list.append([col - 1, row + 1])
                if board[row + 1][col - 1] is None:
                    possible_moves_list.append([col - 1, row + 1])

            # Go down
            if row < 7:
                if board[row + 1][col] is not None:
                    if board[row][col] is not None:
                        if board[row + 1][col].color != board[row][col].color:
                            possible_moves_list.append([col, row + 1])
                if board[row + 1][col] is None:
                    possible_moves_list.append([col, row + 1])

            # Go down right
            if row < 7 and col < 7:
                if board[row + 1][col + 1] is not None:
                    if board[row][col] is not None:
                        if board[row + 1][col + 1].color != board[row][col].color:
                            possible_moves_list.append([col + 1, row + 1])
                if board[row + 1][col + 1] is None:
                    possible_moves_list.append([col + 1, row + 1])

            # Go right
            if col < 7:
                if board[row][col + 1] is not None:
                    if board[row][col] is not None:
                        if board[row][col + 1].color != board[row][col].color:
                            possible_moves_list.append([col + 1, row])
                if board[row][col + 1] is None:
                    possible_moves_list.append([col + 1, row])

            # Go right up
            if row > 0 and col < 7:
                if board[row - 1][col + 1] is not None:
                    if board[row][col] is not None:
                        if board[row - 1][col + 1].color != board[row][col].color:
                            possible_moves_list.append([col + 1, row - 1])
                if board[row - 1][col + 1] is None:
                    possible_moves_list.append([col + 1, row - 1])

            return possible_moves_list

        if self.WhiteInCheck:
            for i in range(8):
                for j in range(8):
                    if board[j][i] is not None:
                        if board[j][i].color == "b":
                            possible_moves_b = board[j][i].possible_moves((i,j),board)
                            print(possible_moves_b)

            # Go up
            if row > 0:
                if board[row - 1][col] is not None:
                    if board[row][col] is not None:
                        if board[row - 1][col].color != board[row][col].color:
                            possible_moves_list.append([col, row - 1])
                if board[row - 1][col] is None:
                    possible_moves_list.append([col, row - 1])

class Pawn(Piece):

    def __init__(self, color, type, image):
        super().__init__(color, type, image)
        #self.promotion_possible = False

    def possible_moves(self,click, board):
        color = self.color
        col = click[0]
        row = click[1]

        possible_moves_list  =[]

        if row < 7 and color == "w":
            if board[row-1][col] is None:
                possible_moves_list.append([col, row - 1])
                if row == 6 and board[row - 2][col] is None:
                    possible_moves_list.append([col, row -2])
            #Capture sideways
            if col < 7:
                if board[row - 1][col +1] is not None:
                    if board[row - 1][col + 1].color != "w":
                        possible_moves_list.append([col+1, row - 1])
            if col > 0:
                if board[row - 1][col - 1] is not None:
                    if board[row - 1][col - 1].color != "w":
                        possible_moves_list.append([col - 1, row - 1])


        if row > 0 and color == "b":

            if board[row+1][col] is None:
                possible_moves_list.append([col, row +1])
                if row == 1 and board[row + 2][col] is None:
                    possible_moves_list.append([col, row +2])
            #Capture sideways
            if col < 7:
                if board[row + 1][col +1] is not None:
                    if board[row + 1][col + 1].color != "b":
                        possible_moves_list.append([col+1, row + 1])
            if col > 0:
                if board[row + 1][col - 1] is not None:
                    if board[row + 1][col - 1].color != "b":
                        possible_moves_list.append([col - 1, row + 1])

        return possible_moves_list

'''
The inherited classes from the parent class Piece will now be given their color ("b" for black, "w" for white), their 
type and lastly their image. It is the setup for the 2 dimensional grid in lucaboard2.
'''

#Black pieces
br = Rook("b", "rook", "Black_Rook.png")
bkn = Knight("b", "knight", "Black_Knight.png")
bb = Bishop("b", "bishop", "Black_Bishop.png")
bq = Queen("b", "queen", "Black_Queen.png")
bk = King("b", "king", "Black_King.png")
bp = Pawn("b", "pawn", "Black_pawn.png")

#White pieces
wr = Rook("w", "rook", "White_Rook.png")
wkn = Knight("w", "knight", "White_Knight.png")
wb = Bishop("w", "bishop", "White_Bishop.png")
wq = Queen("w", "queen", "White_Queen.png")
wk = King("w", "king", "White_King.png")
wp = Pawn("w", "paw", "White_Pawn.png")



