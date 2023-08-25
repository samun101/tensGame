import pygame
import pygame_textinput
from pygame.locals import *

def sets(surface):
    qs = ['base number', 'time limit (seconds)', 'RNG seed', 'board width', 'board height']
    textinput = pygame_textinput.TextInputVisualizer()
    font = pygame.font.Font('freesansbold.ttf',32)
    a = [10] * len(qs)
    running = True
    q = 0
    while running:
        text = font.render(qs[q], True, (0, 0, 0), (0, 155, 0))
        texRect = text.get_rect()
        texRect.center = (375, 250)
        surface.fill((0, 155, 0))
        events = pygame.event.get()
        textinput.update(events)
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    inp = textinput.value
                    if inp:
                        a[q] = int(inp)
                    else:
                        a[q] = 10
                    print(a)
                    textinput = pygame_textinput.TextInputVisualizer()
                    q += 1
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        surface.blit(text, texRect)
        if q >= len(a):
            running = False
            return a
        # Blit its surface onto the screen
        surface.blit(textinput.surface, (350, 300))

        pygame.display.update()
