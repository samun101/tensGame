import pygame
import pygame_textinput
from pygame.locals import *

def sets(surface):
    textinput = pygame_textinput.TextInputVisualizer()
    font = pygame.font.Font('freesansbold.ttf',32)
    text = font.render('testing text',True,(0,0,0),(0,155,0))
    texRect = text.get_rect()
    texRect.center = (500,250)
    running = True
    while running:
        surface.fill((0, 155, 0))
        events = pygame.event.get()
        textinput.update(events)
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        surface.blit(text, texRect)
        # Blit its surface onto the screen
        surface.blit(textinput.surface, (500, 300))

        pygame.display.update()
