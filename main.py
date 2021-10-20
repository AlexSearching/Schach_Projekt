import pygame
from sys import exit
from lucamain import sayinghello

pygame.init()

WHITE = (255,255,255)

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("My game")

# classes for sprites
class test2_surface(pygame.sprite.Sprite):
    def __init__(self, width, height, posix, posiy):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()


    def update(self):
        self.rect.center = (posix, posiy)

posix = 100
posiy = 100

# sprite groups
sprites_group = pygame.sprite.Group()
sprites_group.add(test2_surface(100,100,posix,posiy))




# surfaces
test_surface = pygame.Surface((100,100))
test_surface.fill((255,255,255))
text_surface = pygame.font.Font(None, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        posix -= 0.5
    if keys_pressed[pygame.K_RIGHT]:
        posiy += 0.5


    screen.blit(test_surface, (0,0))
    sprites_group.draw(screen)
    sprites_group.update()

    pygame.display.update()

