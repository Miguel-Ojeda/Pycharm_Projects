# 1 imports...
import sys
import pygame
import pygwidgets
from card import Card
from deck import Deck
from game import Game

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
background = pygwidgets.Image(window, (0, 0), 'images/background.png')
newGameButton = pygwidgets.TextButton(window, (20, 530), 'New Game', width=100, height=45)
higherButton = pygwidgets.TextButton(window, (540, 520), 'Higher', width=120, height=55)
lowerButton = pygwidgets.TextButton(window, (340, 520), 'Lower', width=120, height=55)
quitButton = pygwidgets.TextButton(window, (880, 530), 'Quit', width=100, height=45)

# 5 Inicializar variables
mi_partida = Game(window)

# 6 - Loop forever: estos programas, están dirigidos por eventos. Básicamente es un bucle infinito
while True:
    # 7: mirar eventos,
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
           (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or \
            quitButton.handleEvent(event):
                pygame.quit()
                sys.exit()

        if newGameButton.handleEvent(event):
            mi_partida.reset()
            lowerButton.enable()
            higherButton.enable()

        if higherButton.handleEvent(event):
            gameOver = mi_partida.hitHigherOrLower(HIGHER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()

        if lowerButton.handleEvent(event):
            gameOver = mi_partida.hitHigherOrLower(LOWER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()
    # 8 acciones en cada frame,
    # 9 volver a colocar el fondo,
    background.draw()
    # 10 redibujar elementos actualizados
    mi_partida.draw()
    newGameButton.draw()
    higherButton.draw()
    lowerButton.draw()
    quitButton.draw()
    # 11 mostrar ventana
    pygame.display.update()
    # 12 pausar el programa hasta que toque con el reloj...
    clock.tick(FRAMES_PER_SECOND)