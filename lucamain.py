import pygame
import sys
import math
from lucapiece import Pawn

from lucaboard import describe_fields
from lucaboard import draw_board
from lucaboard import GameState
from lucaboard import Move

pygame.init()

#Set Dimensions
screen_width = 500
screen_height = 500

SQUARE = screen_height//8

display_screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Chess Game")

king = pygame.image.load("White_King.png")
king = pygame.transform.scale(king, (100,100))
king2 = pygame.image.load("Black_King.png")

#FPS
clock = pygame.time.Clock()



gs = GameState(8,8)






#Set colors
WHITE = (255,255,255)
ORANGE = (255, 160, 0)
OPTIONAL = (100,100,100)
RED = (255,0,0)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)




def reset_gamewindow():
    #if the game is finished reset the board
    pass




def click_pos():
    x, y = pygame.mouse.get_pos()
    rounded_x = math.floor((x / 100))
    rounded_y = math.floor((y / 100))

    return rounded_x, rounded_y

def draw_boardd(OPTIONAL):
    for i in range(8):
        for j in range(8):
            if i %2 == 0 and j %2 != 0:
                pygame.draw.rect(display_screen,(OPTIONAL),((SQUARE*i),(SQUARE*j),SQUARE,SQUARE))
            if i %2 != 0 and j %2 != 0:
                pygame.draw.rect(display_screen, (OPTIONAL), ((SQUARE * i), ((SQUARE * j)-SQUARE), SQUARE, SQUARE))





def main():
    clicked_square = ()
    player_move_destination = []  # Takes two squares which define a move
    running = True
    while running:
        #Set FPS
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                pass
            mouse_pressed = pygame.mouse.get_pressed(num_buttons=3)
            if mouse_pressed == (True, False, False):
                print("Left key")



            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = click_pos()

                if clicked_square == (x,y):
                    clicked_square = ()
                    player_move_destination = []
                else:
                    clicked_square = (x,y)
                    player_move_destination.append(clicked_square)

                if len(player_move_destination) > 2:
                    player_move_destination = []
                    player_move_destination.append(clicked_square)

                print(player_move_destination)
                if len(player_move_destination) == 1:
                    print(player_move_destination[0][0])
                    print(player_move_destination[0][1])
                if len(player_move_destination) ==2:
                    print(player_move_destination[1][0])
                    print(player_move_destination[1][1])
                if len(player_move_destination) == 0:
                    print(None)
                if len(player_move_destination) == 2:
                    move = Move(player_move_destination[0],player_move_destination[1],gs.board)
                    print(move)
                    gs.move(move)
                    clicked_square = ()
                    player_move_destination = []

                gs.Piece_selection(x,y)
                gs.show_board()


        #Fill the screen white
        display_screen.fill(WHITE)

        draw_boardd(ORANGE)

        king.blit(display_screen, (0, 0))
        king2.blit(display_screen, (0, 0))
        '''
        #The player can choose the color OPTIONAL for himself
        draw_board(YELLOW)




        #Describes all fields in a chess likely notation
        describe_fields()

        #Blits all the Piece Classes on the display_screen
        gs.create_board()



        #Update the display
        '''
        pygame.display.update()

if __name__ == "__main__":
    main()






