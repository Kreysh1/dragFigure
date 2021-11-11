# Python v3.9.7
# Setup Python --------------------------------------------------------- #
from os import truncate
import pygame, sys
from pygame import image
from pygame.draw import circle, rect
from pygame.gfxdraw import *

# Setup pygame/window -------------------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Drag Figure')
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
screenRect = screen.get_rect()

font = pygame.font.SysFont(None, 25)

click = False

def draw_text(text, font, color, surface, position, alignment="topleft"):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()

    # Tops
    if alignment == "topleft":
        textrect.topleft = position
    elif alignment == "topright":
        textrect.topright = position
    # Bottoms
    elif alignment == "bottomleft":
        textrect.bottomleft = position
    elif alignment == "bottomright":
        textrect.bottomright = position
    # Mids
    elif alignment == "midtop":
        textrect.midtop = position
    elif alignment == "midleft":
        textrect.midleft = position
    elif alignment == "midright":
        textrect.midright = position
    elif alignment == "midbottom":
        textrect.midbottom = position
    # Center
    elif alignment == "center":
        textrect.center = position

    surface.blit(textobj, textrect)

# Load Images ------------------------------------------------------- #
gameImage_0 = pygame.image.load("button_game_0.png").convert()
gameImage_1 = pygame.image.load("button_game_1.png").convert()
optionsImage_0 = pygame.image.load("button_options_0.png").convert()
optionsImage_1 = pygame.image.load("button_options_1.png").convert()
exitImage_0 = pygame.image.load("button_exit_0.png").convert()
exitImage_1 = pygame.image.load("button_exit_1.png").convert()

# Get Rects ---------------------------------------------------------- #
buttonGame_0 = pygame.Rect((50, 100), (gameImage_0.get_size()))
buttonGame_1 = pygame.Rect((50, 100), (gameImage_1.get_size()))
buttonOptions_0 = pygame.Rect((50, 200), (optionsImage_0.get_size()))
buttonOptions_1 = pygame.Rect((50, 200), (optionsImage_1.get_size()))
buttonExit_0 = pygame.Rect((50, 200), (exitImage_0.get_size()))
buttonExit_1 = pygame.Rect((50, 200), (exitImage_1.get_size()))

def main_menu():
    while True:

        screen.fill((0,0,0))
        #pygame.draw.rect(screen, (255, 0, 0, 0.5), (0, 0, WIDTH, 50 ))
        #pygame.gfxdraw.box(screen, pygame.Rect(0, 0, WIDTH, HEIGHT ), (0,200,0,100))
        draw_text('Menú Principal', font, (255, 255, 255), screen, (WIDTH/2, 15), alignment="midtop")

        mouseX, mouseY = pygame.mouse.get_pos()

        #button_1 = screen.blit(gameImage, gameImageRect)
        #button_2 = screen.blit(optionsImage, optionsImageRect)
        if buttonGame_0.collidepoint((mouseX, mouseY)):
            screen.blit(gameImage_1, buttonGame_1)
            if click:
                game()
        else:
            screen.blit(gameImage_0, buttonGame_0)
        if buttonOptions_0.collidepoint((mouseX, mouseY)):
            screen.blit(optionsImage_1, buttonOptions_1)
            if click:
                options()
        else:
            screen.blit(optionsImage_0, buttonOptions_0)
        #pygame.draw.rect(screen, (255, 0, 0), button_1)
        #pygame.draw.rect(screen, (255, 0, 0), button_2)
        #screen.blit(gameImage_0, buttonGame_0)
        #screen.blit(optionsImage_0, buttonOptions_0)
        
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)

def game():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('Juego', font, (255, 255, 255), screen, (WIDTH/2, 15), alignment="midtop")
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)

def options():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text('Opciones', font, (255, 255, 255), screen, (WIDTH/2, 15), alignment="midtop")
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