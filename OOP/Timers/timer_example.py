# 1 imports
import pygame
from timer import Timer
import pygwidgets
import sys

# 2 definimos constantes....
BLACK = (0, 0, 0)
LIGHT_GRAY = (189, 189, 189)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)  # tupla
FRAMES_PER_SECOND = 30  # es el límite máximo al que correrá, limitado por un reloj....


# 3 iniciamos el entorno de pygame
pygame.init()
window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.
# background = pygwidgets.Image(window, (0, 0), 'images/background.png')
start_button = pygwidgets.TextButton(window, (20, 500), 'Start Timer')
pause_button = pygwidgets.TextButton(window, (150, 500), 'Pause Timer')

clicme_button = pygwidgets.TextButton(window, (300, 500), 'Click ME')
exit_button = pygwidgets.TextButton(window,(600, 500), 'Salir')
# lowerButton = pygwidgets.TextButton(window, (340, 520), 'Lower', width=120, height=55)
# quitButton = pygwidgets.TextButton(window, (880, 530), 'Quit', width=100, height=45)
mensaje_timer = pygwidgets.DisplayText(window, (200, 20), 'Timer sin activar', fontSize=32)
mensaje_click = pygwidgets.DisplayText(window, (200, 200), 'Botón sin clicar', fontSize=32)

# 5 Inicializar variables
mi_timer = Timer(7)
numero_de_clics = 0
# 6 - Loop forever: estos programas, están dirigidos por eventos. Básicamente es un bucle infinito
while True:
    # 7: mirar eventos,
    for event in pygame.event.get():
        # condiciones en las que salimos del programa...
        if event.type == pygame.QUIT or \
           (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or \
            (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or \
            exit_button.handleEvent(event):
                pygame.quit()
                sys.exit()

        if start_button.handleEvent(event):
            mi_timer.start()
            start_button.disable()

        if clicme_button.handleEvent(event):
            numero_de_clics += 1
            mensaje_click.setValue(f'Me haz clicado {numero_de_clics} veces')

        # if higherButton.handleEvent(event):
        #     gameOver = mi_partida.hitHigherOrLower(HIGHER)
        #     if gameOver:
        #         higherButton.disable()
        #         lowerButton.disable()
        #
        # if lowerButton.handleEvent(event):
        #     gameOver = mi_partida.hitHigherOrLower(LOWER)
        #     if gameOver:
        #         higherButton.disable()
        #         lowerButton.disable()
    # 8 acciones en cada frame,
    if mi_timer.ha_finalizado():
        print('El timer ha acabado')
        start_button.enable()
        mensaje_timer.setValue('El timer ha acabado')
    else:
        mensaje_timer.setValue(f'Transcurridos {int(mi_timer.get_time())} segundos')


    # 9 volver a colocar el fondo,
    window.fill(LIGHT_GRAY)
    # 10 redibujar elementos actualizados
    start_button.draw()
    clicme_button.draw()
    exit_button.draw()
    pause_button.draw()
    mensaje_timer.draw()
    mensaje_click.draw()
    # 11 mostrar ventana
    pygame.display.update()
    # 12 pausar el programa hasta que toque con el reloj...
    clock.tick(FRAMES_PER_SECOND)

