# Next, we’ll build a location-based animation. This code will allow us to
# move an image diagonally and then have it appear to bounce off the edges
# of the window. This was a favorite technique of screensavers on old CRTbased
# monitors, to avoid burning in a static image.

# en esta nueva versión simularemos un movimiento de rebote...
# es lo mismo q pygame_2 pero con rect...
# ahora añadimos el sonido...

# Haremos lo mismo, pero con OOP

# 1 importamos los paquetes que vamos a utilizar
import sys
import pygame
import random
from pygame.locals import *   # importa constantes...

# 2 definimos constantes....
BLACK = (0, 0, 0)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)  # tupla
FRAMES_PER_SECOND = 30  # es el límite máximo al que correrá, limitado por un reloj....
# cosas de la bola....
BALL_WIDTH_HEIGHT = 100   # al ser la imagen cuadrada, es realmente el tamaño de la imagen....
N_PIXELS_PER_FRAME = 3


# 3 iniciamos el entorno de pygame
pygame.init()   # inicializamos las estructuras
# Creamos una ventana (surface) para poder dibujar, recibir entradas... y nos devuelve su valor ...
window = pygame.display.set_mode(WINDOW_SIZE)

clock = pygame.time.Clock()   # creamos un objeto de la clase Clock, nos va a servir para limitar veolicidad juego...

# 4 - Load assets: image(s), sound(s), etc.
ballImage = pygame.image.load("images/ball.png")

# 5 - Initialize variables
ball_rect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ball_rect.x = random.randrange(MAX_WIDTH)
ball_rect.y = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME



# 6 - Loop forever: estos programas, están dirigidos por eventos.. básicamente es un bucle infinito
# dentro del blucle:
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
        # el usuario apreta el botón de cerrar la ventana
        if event.type == pygame.QUIT:
            pygame.quit()   # borra y libera las estructuras....
            sys.exit()  # se termina el programa
        elif event.type == pygame.KEYDOWN and event.key== pygame.K_q:
            sys.exit()


    # 8 acciones a realizar en cada "frame"...
    if (ball_rect.x < 0) or (ball_rect.x >= MAX_WIDTH):
        xSpeed = -xSpeed  # reverse X direction
    if (ball_rect.y < 0) or (ball_rect.y >= MAX_HEIGHT):
        ySpeed = -ySpeed  # reverse Y direction

    ball_rect.x += xSpeed
    ball_rect.y += ySpeed

    # 9 borramos la ventana, antes de volver a redibujar nada...
    # realmente habría q  dibujar el fondo, antes de volver a dibujar los elementos
    window.fill(BLACK)


    # 10 volvemos a "dibujar en la ventana (memoria)" de nuevo los elementos...
    window.blit(ballImage, ball_rect)    # damos las coordenadas de la esquina superior izquierda...

    # 11 mostramos la pantalla  (AHORA ES CUANDO SE MUESTRA REALMENTE LO QUE ESTÁ GRABADO EN LA VENTANA
    # Obs. que no le indicamos a pygame la ventana, él ya sabe las que ha creado y las muestra
    pygame.display.update()

    # 12 ralentizamos, para que el programa no esté siempre activo... nos damos un respiro...
    clock.tick(FRAMES_PER_SECOND)   # o sea, esperamos un tick de reloj...









