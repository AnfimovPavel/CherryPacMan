import pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 600, 600


def start_game(screen):
    text_start = ["Начать игру", "Настройки", "Выйти из игры"]
    font = pygame.font.SysFont("Georgia", 50)
    for i in range(3):
        text = font.render(text_start[i], 1, (50, 70, 0))
        text_x = 300 - text.get_width() // 2
        text_y = 150 + 150 * i - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        pygame.draw.rect(screen, (200, 150, 50), (text_x - 10, text_y - 10,
                                                  text_w + 20, text_h + 20))
        screen.blit(text, (text_x, text_y))


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("My Game")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 200))
        start_game(screen)
        pygame.display.flip()
    pygame.display.quit()


if __name__ == "__main__":
    main()
