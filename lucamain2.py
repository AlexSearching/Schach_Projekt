'''
This file is going to run the main code. Basically every function will be called from either lucapiece or lucaboard.
The main code therefore will be written as shortly as possible.
'''

#Import the libraries
import pygame
import math

#Import Classes and Functions
from lucaboard2 import Move
from lucaboard2 import GameState
from lucaboard2 import describe_fields
from lucaboard2 import draw_board
from lucapiece2 import wk
from lucapiece2 import bk

gs = GameState()

#Initialize pygame
pygame.init()

#Set Dimensions
WIDTH = 800
HEIGHT = 800

#Size of a square
SQUARE = WIDTH//8 or HEIGHT//8

#Set a display screen
DISPLAY_SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Luca de Pietro Chess Game")

#FPS
clock = pygame.time.Clock()

#RGB Colors
WHITE = (255, 255, 255)
OPTIONAL = (205, 141, 57)
RED = (255, 0, 0)
ORANGE = (255, 160, 0)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)

#Sounds
alert_sound = pygame.mixer.Sound("Chess_alert.wav") #Download from https://freesound.org/people/JustinBW/sounds/80921/

#Set Text for when the game is paused or over
font = pygame.font.SysFont("consolas",28)

Game_paused_text = font.render("Game paused: press c to continue or r to restart",True, (150,150,150))
Game_paused_rect = Game_paused_text.get_rect()
Game_paused_rect.midbottom = (WIDTH//2, HEIGHT//2)

Game_over_text_w = font.render("Game Over, White Won",True, (150,150,150))
Game_over_text_w_rect = Game_over_text_w.get_rect()
Game_over_text_w_rect.midbottom = (WIDTH//2, HEIGHT//2)

Game_over_text_b = font.render("Game Over, Black Won",True, (150,150,150))
Game_over_text_b_rect = Game_over_text_b.get_rect()
Game_over_text_b_rect.midbottom = (WIDTH//2, HEIGHT//2)

Restart_text = font.render("Press any Key to restart the game", True, (150,150,150))
Restart_rect = Restart_text.get_rect()
Restart_rect.midbottom = (WIDTH//2, HEIGHT//2 +40)

#Convert every mouse click into a rounded value, so that each click is defined by two natural numbers in range 0-7
def click_pos():
    x, y = pygame.mouse.get_pos()
    rounded_x = math.floor((x / 100)) #x for the x_coordinate
    rounded_y = math.floor((y / 100)) #y for the y_coordinate
    return rounded_x, rounded_y

'''
Here the main code will run. It will handle the users inputs and makes the game going.
'''

def main():
    clicked_square = () #Every click is stored in clicked_square as a tuple
    player_move_destination = []  #The clicked squares will be added into a list; two squares define a move
    play_soundW = True
    play_soundB = True
    running = True
    while running:
        # Set FPS
        clock.tick(60)

        #Check the events from the user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #Exit the game
                running = False
            if event.type == pygame.KEYDOWN:
                #Pause the game
                if event.key == pygame.K_p:
                    #Restart the game if wanted, else continue
                    game_paused = True
                    while game_paused:
                        DISPLAY_SCREEN.blit(Game_paused_text, Game_paused_rect)
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                # Player wants to play on
                                if event.key == pygame.K_c:
                                    game_paused = False
                                #Player wants to restart
                                if event.key == pygame.K_r:
                                    gs.restart_game()
                                    play_sound = True
                                    game_paused = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                #Store x as col, y as row
                x, y = click_pos()

                #If the same square is clicked twice, reset tuple and list
                if clicked_square == (x, y):
                    clicked_square = ()
                    player_move_destination = []
                else:
                    clicked_square = (x, y)
                    player_move_destination.append(clicked_square)
                    #gs.check_for_castling()

                '''
                The players clicks must be handled properly for a fluent game. Therefore the following if statements
                will execute the two functions check_for_nonesquare() and check_for_doubleclicks() to avoid unwanted 
                addition of clicks to the player_move_destination list.
                '''

                if len(player_move_destination) == 1:
                    #If a None square is clicked before a piece, it is not of interest
                    gs.check_for_nonesquare(clicked_square, player_move_destination)

                if len(player_move_destination) > 2:
                    #If move not in possible moves, do not append the click
                    gs.check_for_nonesquare(clicked_square, player_move_destination)

                if len(player_move_destination) >= 2:
                    #If pieces of the same colors are clicked, clear the list and append the click
                    gs.check_for_doubleclicks(clicked_square, player_move_destination)


                    if len(player_move_destination) == 2:
                        #Execute a move if possible
                        move = Move(player_move_destination[0], player_move_destination[1], gs.board)
                        gs.move_piece(move)

            #Always check if castling is possible
            gs.check_for_castling()
            #Look at all the possible moves for both pieces
            gs.threat_moves_black()
            gs.threat_moves_white()
            #Return the value True to self.WhiteInCheck/self.BlackInCheck in the King(Piece) Class if king in check
            gs.king_in_check()

            #If the black king is captured, restart the game if wanted; else quit
            while gs.GameOverB:
                #Blit all the texts
                DISPLAY_SCREEN.blit(Game_over_text_w, Game_over_text_w_rect)
                DISPLAY_SCREEN.blit(Restart_text, Restart_rect)
                #Update the display to let the user see
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        gs.GameOverB = False
                        gs.restart_game()
                    if event.type == pygame.QUIT:
                        running = False
                        gs.GameOverB = False

            #If the white king is captured, restart the game if wanted
            while gs.GameOverW:
                #Blit all the texts
                DISPLAY_SCREEN.blit(Game_over_text_b, Game_over_text_b_rect)
                DISPLAY_SCREEN.blit(Restart_text, Restart_rect)
                #Update the display to let the user see
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        gs.GameOverW = False
                        gs.restart_game()
                    if event.type == pygame.QUIT:
                        running = False
                        gs.GameOverW = False

        #Fill the screen white
        DISPLAY_SCREEN.fill((WHITE))

        #The player can choose the color of the squares for himself
        draw_board((ORANGE))

        #Blit the scaled images of the pieces on the display_screen
        gs.draw_pieces()

        #Check if the black king is in check
        if bk.BlackInCheck:
            #If the king is in check, alert the player
            if play_soundB:
                alert_sound.play()
                play_soundB = False
            #Get the black king's coordinates
            bx, by = gs.king_coordinates_black()
            #If the king's coordinates are in the possible moves of the enemy, alert the player by drawing him red
            gs.black_in_check(bx, by)
        #If the king is not in check, reset the Value of play_soundB
        if bk.BlackInCheck == False:
            play_soundB = True

        #Check if the white king is in check
        if wk.WhiteInCheck:
            # If the king is in check, alert the player
            if play_soundW:
                alert_sound.play()
                play_soundW = False
            #Get the black king's coordinates
            wx, wy = gs.king_coordinates_white()
            #If the king's coordinates are in the possible moves of the enemy, alert the player by drawing him red
            gs.white_in_check(wx,wy)
        #If the king is not in check, reset the Value of play_soundB
        if wk.WhiteInCheck == False:
            play_soundW = True

        #A None square will never be selected
        if len(player_move_destination) > 0:
            #Select a piece
            gs.select(player_move_destination, gs.board)

        #Describe all fields in a chess likely description
        describe_fields()

        #Update the display
        pygame.display.update()


if __name__ == "__main__":
    main()
