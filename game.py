import pygame
from BoardSetup import Board
from pygame.locals import *
import math
def runGame(surface, settingArray):
    clock = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 32)
    board = Board(settingArray)
    bord = board.getBoard()
    seed = board.getSeed()
    running = True

    pos = 0
    sel = False
    xSel = -1
    ySel = -1
    while running:
        surface.fill((0, 155, 0))
        back = pygame.Rect(35, 35, 665, 650)
        pygame.draw.rect(surface, (200, 200, 255), back)

        vert = 55
        lat = 55
        for i in bord:
            for x in i:
                text = font.render(str(x), True, (0, 0, 0), (200, 200, 255))
                texRect = text.get_rect()
                texRect.center = (vert, lat)
                surface.blit(text, texRect)
                lat = lat + (665/len(i))
            vert = vert+ (665/len(bord))
            lat = 55

        events = pygame.event.get()

        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                xSel = pos[0]
                ySel = pos[1]
                sel = True

            if event.type == pygame.MOUSEBUTTONUP:
                sel = False
                mpos = pygame.mouse.get_pos()
                board.clearBits(xSel,ySel,mpos[0],mpos[1],len(bord),len(bord[0]))
            elif event.type == QUIT:
                running = False

        text = font.render('seed: '+str(seed), True, (0, 0, 0), (0, 155, 0))
        texRect = text.get_rect()
        texRect.center = (600, 725)
        surface.blit(text, texRect)
        text = font.render('score: ' + str(board.getScore()), True, (0, 0, 0), (0, 155, 0))
        texRect = text.get_rect()
        texRect.center = (400, 725)
        surface.blit(text, texRect)
        if sel:
            mpos = pygame.mouse.get_pos()
            if mpos[0] > xSel:
                sx = xSel
            else:
                sx = mpos[0]
            if mpos[1] > ySel:
                sy = ySel
            else:
                sy = mpos[1]
            s = pygame.Surface((minS(mpos[0],xSel),minS(mpos[1],ySel)), pygame.SRCALPHA)  # per-pixel alpha
            s.fill((255, 255, 255, 128))  # notice the alpha value in the color
            surface.blit(s, (sx, sy))

        pygame.display.update()

        clock.tick(30)

def minS(x, y):
            if x >y:
                return x-y
            else:
                return y-x

#def eventCheck(events):