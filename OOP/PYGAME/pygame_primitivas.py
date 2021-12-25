# 0 Plantilla genérica para un programa que utilice pygame....

# 1 importamos los paquetes que vamos a utilizar
import sys
import pygame
# import pygame.color
import random
from pygame.locals import *
# importa constantes...

# 2 definimos constantes....
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)  # tupla
FRAMES_PER_SECOND = 30  # es el límite máximo al que correrá, limitado por un reloj....



# 3 iniciamos el entorno de pygame
pygame.init()   # inicializamos las estructuras
# creamos una ventana (surface) para poder dibujar, recibir entradas..
window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()   # creamos un objeto de la clase Clock, nos va a servir para limitar velocidad juego...

# 4 - Load assets: image(s), sound(s), etc.

# 5 - Initialize variables


# 6 - Loop forever: estos programas, están dirigidos por eventos. Básicamente es un bucle infinito
# dentro del bucle:
# 7: mirar eventos,
# 8 acciones en cada frame,
# 9 volver a colocar el fondo,
# 10 redibujar elementos actualizados
# 11 mostrar ventana
# 12 pausar el programa hasta que toque con el reloj...

# 6 Bucle infinito
while True:

    # 7 Comprobamos los eventos que han sucedido, y damos respuesta a los mismos
    for event in pygame.event.get():
        # el usuario aprieta el botón de cerrar la ventana
        if event.type == pygame.QUIT:
            pygame.quit()   # borra y libera las estructuras....
            sys.exit()  # se termina el programa

    # 8 acciones a realizar en cada "frame"...


    # 9 borramos la ventana, antes de volver a redibujar nada...
    # realmente habría que dibujar el fondo, antes de volver a dibujar los elementos
    window.fill(GRAY)

    # 10 volvemos a "dibujar en la ventana (memoria)" de nuevo los elementos...
    pygame.draw.line(window, RED, (20, 20), (60, 20), 4)
    pygame.draw.line(window, RED, (0, 0), (WINDOW_WIDTH, WINDOW_HEIGHT), 4)

    pygame.draw.circle(window, RED, (250, 200), 80, 6)  # 6 pixel
    pygame.draw.circle(window, RED, (500, 200), 80, 0)  # edgefilled
    pygame.draw.aaline(window, RED, (0, WINDOW_HEIGHT), (WINDOW_WIDTH, 0), 1)

    # 11 mostramos la pantalla (AHORA ES CUANDO SE MUESTRA REALMENTE LO QUE ESTÁ GRABADO EN LA VENTANA)
    # Obs. que no le indicamos a pygame la ventana, él ya sabe las que ha creado y las muestra
    pygame.display.update()

    # 12 ralentizamos, para que el programa no esté siempre activo... nos damos un respiro...
    clock.tick(FRAMES_PER_SECOND)   # o sea, esperamos un tick de reloj...
