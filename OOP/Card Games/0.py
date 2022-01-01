# 1 imports...
import sys
import pygame
import pygwidgets
from card import Card

# 2 constantes
# 2 definimos constantes....
BLACK = (0, 0, 0)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)  # tupla
FRAMES_PER_SECOND = 30  # es el límite máximo al que correrá, limitado por un reloj....


# 3 iniciamos el entorno de pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.

# 5 - Initialize variables
carta = Card(window, '4', 'Clubs', 3)

# 6 - Loop forever: estos programas, están dirigidos por eventos. Básicamente es un bucle infinito
while True:
    # 7: mirar eventos,
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and carta.clicked(event.pos):
            carta.flip()

    # 8 acciones en cada frame,
    # 9 volver a colocar el fondo,
    window.fill(BLACK)
    # 10 redibujar elementos actualizados
    carta.draw()
    # 11 mostrar ventana
    pygame.display.update()
    # 12 pausar el programa hasta que toque con el reloj...
    clock.tick(FRAMES_PER_SECOND)
