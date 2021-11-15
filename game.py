# Python v3.9.7
# Setup Python --------------------------------------------------------- #
from os import truncate
import pygame, sys
from pygame import image
from pygame.draw import circle, rect
from pygame.gfxdraw import box
import drawFigure as df

# Setup pygame/window -------------------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
pygame.display.set_caption('Drag Figure')
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

resolutions = pygame.display.list_modes()
#fullscreen = False

# Load Images ------------------------------------------------------- #
gameImage_0 = pygame.image.load("sprites/button_game_0.png").convert()
gameImage_1 = pygame.image.load("sprites/button_game_1.png").convert()
optionsImage_0 = pygame.image.load("sprites/button_options_0.png").convert()
optionsImage_1 = pygame.image.load("sprites/button_options_1.png").convert()
exitImage_0 = pygame.image.load("sprites/button_exit_0.png").convert()
exitImage_1 = pygame.image.load("sprites/button_exit_1.png").convert()

# Create button instancies ----------------------------------------------------------------------- #
start_button = df.Button(50, 100, 1, gameImage_0, gameImage_1)
options_button = df.Button(50, 200, 1, optionsImage_0, optionsImage_1)
exit_button = df.Button(50, 300, 1, exitImage_0, exitImage_1)


# Main Menu Module ---------------------------------------------------------- #
def main_menu():
    while True:

        # Background ------------------------------------------------------------------------------ #
        screen.fill((0,0,0))

        # Draws ------------------------------------------------------------------------------ #
        df.drawtext('Menú Principal', (255, 255, 255), 25, screen, screen.get_width()/2, 15, alignment="midtop")

        start_button.draw(screen)
        options_button.draw(screen)
        exit_button.draw(screen)

        # Logic ------------------------------------------------------------------------------ #
        if start_button.clicked:
            game()
        if options_button.clicked:
            options()
        if exit_button.clicked:
            pygame.quit()
            sys.exit()

        # Events -------------------------------------------------- #
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == VIDEORESIZE:
            #     screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        mainClock.tick(60)

# In-Game Module ---------------------------------------------------------- #
def game():
    running = True
    score = 0
    while running:
        score = score + 1

        # Background ------------------------------------------------------------------------------ #
        screen.fill((0,0,0))

        # Draws ------------------------------------------------------------------------------ #
        df.drawtext('Juego', (255, 255, 255), 25, screen, screen.get_width()/2, 15, alignment="midtop")

        df.drawtext('Puntos: ' + str(score), (255, 255, 255), 25, screen, 15, 15)
   
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    df.save("C:\\tmp\\score.txt", str(score))
        pygame.display.update()
        mainClock.tick(60)

# Options Module ---------------------------------------------------------- #
def options():
    running = True
    while running:
         # Background ------------------------------------------------------------------------------ #
        screen.fill((0,0,0))

        # Draws ------------------------------------------------------------------------------ #
        df.drawtext('Opciones', (255, 255, 255), 25, screen, screen.get_width()/2, 15, alignment="midtop")

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)

main_menu()