import pygame

pygame.init()

clock = pygame.time.Clock()

height = 500
width = 500

display_screen = pygame.display.set_mode((width,height))

king = pygame.image.load("White_King.png")
king = pygame.transform.scale(king, (100,100))
king2 = pygame.image.load("Black_King.png")
king2 = pygame.transform.scale(king2, (100,100))

circle_r = height//2
circle_c = (width//2, height//2)

line_start = circle_c
line_end = [width//2, 0]

line_rect = pygame.Rect((width//2),0,1,circle_r)

test_rect = pygame.Rect(300,100,200,300)

def draw():
    pygame.draw.circle(display_screen, (255, 155, 203), circle_c, circle_r)
    pygame.draw.line(display_screen, (255, 0, 0), line_start, line_end, 2)


'''
running = True
while running:
    clock.tick(50)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            
        display_screen.fill((255,255,255))

        display_screen.blit(king2, (0, 0))
        display_screen.blit(king, (0, 0))



        pygame.display.update()
'''

list = [x for x in range(8)]
print(list)