import pygame
pygame.init()

display = pygame.display.set_mode((800,800))


clock = pygame.time.Clock()

king = pygame.image.load("White_King.png")
king2 = pygame.image.load("Black_King.png")


running = True
while running:
    # Set FPS
    clock.tick(60)

    # Check the events from the user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit the game
            running = False
        if event.type == pygame.KEYDOWN:
            # Undo a move
            if event.key == pygame.K_LEFT:
                pass

            if event.key == pygame.K_p:
                pass
        # Reset the Game State if wanted, else continue
        king.blit(display, (0,0))
        king2.blit(display, (0,0))
