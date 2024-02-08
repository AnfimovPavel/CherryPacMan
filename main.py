import sys

import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))

color = (200, 100, 100)
background.fill(pygame.Color(color))

manager = pygame_gui.UIManager((800, 600))

settings = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((325, 275), (150, 50)),
    text='Settings',
    manager=manager
)

play = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((325, 175), (150, 50)),
    text='Play',
    manager=manager
)

exit = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((325, 375), (150, 50)),
    text='Exit',
    manager=manager
)

clock = pygame.time.Clock()
running = True
while running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play:
                    print('play')
                elif event.ui_element == settings:
                    print(settings)
                elif event.ui_element == exit:
                    sys.exit()

        manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    pygame.display.update()
