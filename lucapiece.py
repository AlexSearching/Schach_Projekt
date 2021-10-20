import pygame
import math
#Set Dimensions
screen_width = 800
screen_height = 800

display_screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Chess Game")

#Load Images
#Chess Pieces for black
b_rook = pygame.image.load("Black_Rook.png")
b_knight = pygame.image.load("Black_Knight.png")
b_bishop = pygame.image.load("Black_Bishop.png")
b_queen = pygame.image.load("Black_Queen.png")
b_king = pygame.image.load("Black_King.png")

b_pawn = pygame.image.load("Black_Pawn.png")



#Chess pieces for white
w_rook = pygame.image.load("White_Rook.png")
w_knight = pygame.image.load("White_Knight.png")
w_bishop = pygame.image.load("White_Bishop.png")
w_queen = pygame.image.load("White_Queen.png")
w_king = pygame.image.load("White_King.png")

w_pawn = pygame.image.load("White_Pawn.png")

b_list = [b_rook, b_knight, b_bishop, b_queen, b_king, b_pawn]
w_list = [w_rook, w_knight, w_bishop, w_queen, w_king, w_pawn]

B = []
W = []

for image in b_list:
    B.append(pygame.transform.scale(image,(100,100)))
for image in w_list:
    W.append(pygame.transform.scale(image,(100,100)))

#Set colors
WHITE = (255,255,255)
OPTIONAL = (100,100,100)
RED = (255,0,0)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)

# All rects on the chessboard
field_rects = []
for i in range(8):
    for j in range(8):
        rect = pygame.rect.Rect(i*100,j*100, 100,100)
        field_rects.append(rect)





class Piece:
    #Set for default
    img = -1
    piece_rect = (0,0,100,100)


    def __init__(self, col: int, row: int, color):
        self.col = col
        self.row = row
        self.color = color
        self.PieceChosen = False
        self.NoPieceChosen = False

    def draw(self):
        if self.color == "white":
            drawingPiece = W[self.img]


        elif self.color == "black":
            drawingPiece = B[self.img]


        x_coordinate = ((self.col *100)-100)
        y_coordinate = ((self.row *100)-100)

        display_screen.blit(drawingPiece, (x_coordinate,y_coordinate))

        if self.PieceChosen:
            pygame.draw.rect(display_screen, (BLUE), (x_coordinate,y_coordinate,100,100), 2)
            #pygame.draw.circle(display_screen, (RED), (x_coordinate+50,y_coordinate+50), 25)
        if self.NoPieceChosen:
            pass








#Inherit from Mother Class Piece
class Rook(Piece):
    img = 0
    possible_squares = []

    def possible_moves(self):
        pass






    def move(self):
        self.col += 1














        #if len(player_move_destination) >= 1:
            #self.col = player_move_destination[1][0]
            #self.row = player_move_destination[1][1]

class Knight(Piece):
    img = 1
    def possible_moves(self):
        possible_squares = []
        
    def move(self):
        pass
class Bishop(Piece):
    img = 2
    def possible_moves(self):
        pass
    def move(self):
        pass
class Queen(Piece):
    img = 3
    def possible_moves(self):
        pass
    def move(self):
        pass
class King(Piece):
    img = 4
    def possible_moves(self):
        pass
    def move(self):
        pass
class Pawn(Piece):
    img = 5

    def __init__(self, col, row, color):
        super().__init__(col, row, color)
        self.start = True

    def possible_moves(self):
        possible_squares = []
        if self.start:
            if self.color == "white":
                if self.row == 7:
                    #Need to shorten this list into [(a,b),(c,d)]
                    possible_square = (self.col, self.row-1), (self.col, self.row-2)
                    possible_squares.append(possible_square)


            if self.color != "white":
                if self.row == 2:
                    possible_square = ((self.col,self.row+1),(self.col,self.row+2))
                    possible_squares.append(possible_square)


    def move(self):
        pass












