# 1 imports...
import pygame
import pygame.locals
import pygwidgets
from constants import *
from balloon_manager import Balloon_Manager
import sys

# 2 constantes propias del programa principal
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
PANEL_HEIGHT = 60
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND = 30

# 3 iniciamos el entorno de pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.
score_display = pygwidgets.DisplayText(window, (10, USABLE_WINDOW_HEIGHT + 25),
                                       'Score: 0', textColor=BLACK, backgroundColor=None, width=140, fontSize=24)
status_display = pygwidgets.DisplayText(window, (180, USABLE_WINDOW_HEIGHT + 25), '',
                                        textColor=BLACK, backgroundColor=None, width=300, fontSize=24)
start_button = pygwidgets.TextButton(window, (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10), 'Start')

# 5 - Initialize variables
balloon_manager = Balloon_Manager(window, WINDOW_WIDTH, USABLE_WINDOW_HEIGHT)
playing = False  # wait until user clicks Start

# 6 - Loop forever: estos programas, están dirigidos por eventos.. básicamente es un bucle infinito
while True:
    # 7: mirar eventos,
    nPointsEarned = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if playing:
            balloon_manager.handle_event(event)
            score = balloon_manager.get_score()
            score_display.setValue('Score: ' + str(score))
        elif start_button.handleEvent(event):
            balloon_manager.start()
            score_display.setValue('Score: 0')
            playing = True
            start_button.disable()

    # 8 acciones en cada frame
    if playing:
        balloon_manager.update()
        count_popped = balloon_manager.get_count_popped()
        count_missed = balloon_manager.get_count_missed()
        status_display.setValue('Popped: ' + str(count_popped) + ' Missed: ' + str(count_missed) +
                                ' Out of: ' + str(N_BALLOONS))

        if (count_missed + count_popped) == N_BALLOONS:
            playing = False
            start_button.enable()

    # 9 volver a colocar el fondo,
    window.fill(BACKGROUND_COLOR)

    # 10 redibujar elementos actualizados
    if playing:
        balloon_manager.draw()

    pygame.draw.rect(window, GRAY, pygame.Rect(0,USABLE_WINDOW_HEIGHT, WINDOW_WIDTH, PANEL_HEIGHT))
    score_display.draw()
    status_display.draw()
    start_button.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait

