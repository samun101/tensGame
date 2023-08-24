import pygame
from BoardSetup import Board
from pygame.locals import *

def runGame(surface):
    clock = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 32)
    board = Board()
    bord = board.getBoard()
    seed = board.getSeed()
    running = True
    surface.fill((0, 155, 0))
    while running:
        vert = 50
        lat = 50
        for i in bord:
            for x in i:
                text = font.render(str(x), True, (0, 0, 0), (0, 155, 0))
                texRect = text.get_rect()
                texRect.center = (vert, lat)
                surface.blit(text, texRect)
                lat = lat + 50
            vert = vert+50
            lat = 50

        events = pygame.event.get()

        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

        text = font.render('seed: '+str(seed), True, (0, 0, 0), (0, 155, 0))
        texRect = text.get_rect()
        texRect.center = (600, 725)
        surface.blit(text, texRect)
        pygame.display.update()
        clock.tick(30)