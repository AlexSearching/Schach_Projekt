'''
This file is going to run the main code. Basically every function will be called from either lucapiece or lucaboard.
The length of the main code therefore will be written as shortly as possible.
'''

import pygame
import math
from lucaboard2 import draw_board
from lucaboard2 import GameState
from lucaboard2 import describe_fields
from lucaboard2 import Move
from lucapiece2 import bb

gs = GameState()




pygame.init()

#Set Dimensions
WIDTH = 800
HEIGHT = 800

SQUARE = WIDTH//8

DISPLAY_SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Chess Game")




#FPS
clock = pygame.time.Clock()



#Set colors
WHITE = (255,255,255)
OPTIONAL = (255,192,203)
RED = (255,0,0)
ORANGE = (255, 160,0)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)


#Convert every mouse click into a rounded value, so that each click is defined by two natural numbers in range 0-7
def click_pos():
    x, y = pygame.mouse.get_pos()
    rounded_x = math.floor((x / 100))
    rounded_y = math.floor((y / 100))
    return rounded_x, rounded_y


'''
Here the main code will run. It will handle the users inputs and makes the Game going.
'''
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
                gs.return_move()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = click_pos()


                if clicked_square == (x,y):
                    clicked_square = ()
                    player_move_destination = []
                else:
                    clicked_square = (x,y)
                    player_move_destination.append(clicked_square)

                if len(player_move_destination) == 1:
                    gs.check_for_nonesquare(clicked_square, player_move_destination)


                if len(player_move_destination) > 2:
                    gs.check_for_nonesquare(clicked_square, player_move_destination)


                if len(player_move_destination) >= 2:
                    gs.check_for_doubleclicks(clicked_square,player_move_destination)

                    if len(player_move_destination) ==2 :
                        move = Move(player_move_destination[0],player_move_destination[1],gs.board)
                        if gs.whiteToMove:
                            gs.move_white(move)
                        else:
                            gs.move_black(move)




                print(player_move_destination)
                print(len(player_move_destination))



        #Fill the screen white
        DISPLAY_SCREEN.fill((WHITE))

        #The player can choose the color of the squares for himself
        draw_board(GREY)

        gs.draw_pieces()

        if len(player_move_destination) > 0:
            gs.select(clicked_square,gs.board)



        describe_fields()



        #Update the display
        pygame.display.update()

if __name__ == "__main__":
    main()






