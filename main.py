import pygame

from pygame.locals import *
from Settings import sets
from game import runGame

settingArray = [10] * 5

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()


def buttonSet(surface,msg,x,y,w,h,ic,ac,act):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(surface, ac,(x,y,w,h))

        if click[0] == True:
            if act == 1:
                global settingArray
                settingArray = sets(surface)
            if act == 0:
                runGame(surface, settingArray)
    else:
        pygame.draw.rect(surface, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    surface.blit(textSurf, textRect)

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((750, 750))

    running = True

    while running:
        events = pygame.event.get()
        surface.fill((0, 155, 0))
        buttonSet(surface, "start game", 20, 30, 500, 300, (0, 0, 150), (150, 0, 0), 0)
        buttonSet(surface, "settings", 20, 350, 500, 50, (0, 0, 150), (150, 0, 0),1)
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

        pygame.display.update()
        clock.tick(30)

