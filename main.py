import pygame


pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
