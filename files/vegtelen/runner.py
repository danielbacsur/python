import os
import pygame


def path(file): return os.path.join(os.path.dirname(__file__), file)


def scale(obj): return pygame.transform.smoothscale(obj, (screen.get_size()[
    0], obj.get_size()[1] * screen.get_size()[0] / obj.get_size()[0]))


pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480
SPEED = 0.25

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption('Pygame Scene')

# Load the background image
sziklaa = pygame.image.load(path('szikla.png'))

# Set the speed at which the background will scroll
background_speed = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # print(pygame.time.get_ticks())

    screen.fill(0)

    for i in range(2):
        for n in range(2):
            for k in [2, 1, 0]:
                szikla = scale(sziklaa)
                szikla.fill((48-k*12, 48-k*12, 48-k*12), special_flags=pygame.BLEND_MULT)
                screen.blit(
                    szikla if i else pygame.transform.rotate(szikla, 180),
                    (
                        pygame.time.get_ticks() / 1000 * 0.25 * screen.get_width() % screen.get_width() - screen.get_width() * n,
                        screen.get_height()-szikla.get_height() - k * 40 if i else k * 40
                    )
                )
    # screen.blit(szikla, (pygame.time.get_ticks() / 1000 * 0.25 * screen.get_width() % screen.get_width() - screen.get_width(), screen.get_height()-szikla.get_height()))

    pygame.display.update()
