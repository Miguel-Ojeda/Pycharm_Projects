# 0 Plantilla genérica para un programa que utilice pygame....

# 1 importamos los paquetes que vamos a utilizar
import sys
import pygame
from life import *
from pygame.locals import *   # importa constantes...

# 2 definimos constantes....
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)  # tupla
FRAMES_PER_SECOND = 1  # es el límite máximo al que correrá, limitado por un reloj....

# 3 iniciamos el entorno de pygame
pygame.init()   # inicializamos las estructuras
# creamos una ventana (surface) para poder dibujar, recibir entradas..
window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()   # creamos un objeto de la clase Clock, nos va a servir para limitar velocidad juego...

# 4 - Load assets: image(s), sound(s), etc.

# 5 - Initialize variables
automata = Automata(20, 20, setup=SETUP_RANDOM, window=window, world_type=WORLD_ROLLED)

# 6 - Loop forever: estos programas, están dirigidos por eventos. Básicamente es un bucle infinito
# dentro del bucle:
# 7: mirar eventos,
# 8 acciones en cada frame,
# 9 volver a colocar el fondo,
# 10 redibujar elementos actualizados
# 11 mostrar ventana
# 12 pausar el programa hasta que toque con el reloj...

# Empezamos dibujando el autómata...
# automata.crear_test_1(10, 10)
# automata.crear_honey_farm(6, 10)
# automata.crear_glider(1, 1)
# automata.crear_mini_t_invertida(9, 10)
automata.display()
key_pressed = False
# 6 Bucle infinito
# Ahora cada vez que apretemos una tecla se actualizará el autómata...
while True:
    # 7 Comprobamos los eventos que han sucedido, y damos respuesta a los mismos
    for event in pygame.event.get():
        # el usuario aprieta el botón de cerrar la ventana
        if event.type == pygame.QUIT:
            pygame.quit()   # borra y libera las estructuras....
            sys.exit()  # se termina el programa

        # miramos si ha hecho clic, realmente miramos el mouse_up, que, lógicamente, ha venido después del down...
        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:   # or key_pressed:
            # Aquí ocurre todo_!!!
            automata.update()
            automata.display()
            # pygame.time.wait(500) # esperamos medio segundo
            # key_pressed = True
        elif event.type == pygame.KEYUP:
            key_pressed = False
        elif key_pressed:
            automata.update()
            automata.display()




        # clock.tick(FRAMES_PER_SECOND)  # o sea, esperamos un tick de reloj...
        # pygame.time.wait(500)  # en cada ronda esperamos medio segundo

    # 8 acciones a realizar en cada "frame"...

    # 9 borramos la ventana, antes de volver a redibujar nada...
    # realmente habría que dibujar el fondo, antes de volver a dibujar los elementos
    # window.fill(BLACK)

    # 10 volvemos a "dibujar en la ventana (memoria)" de nuevo los elementos...
    # # draw ball at position 100 across (x) and 200 down (y)
    # window.blit(ballImage, (ball_x, ball_y))    # damos las coordenadas de la esquina superior izquierda...

    # 11 mostramos la pantalla (AHORA ES CUANDO SE MUESTRA REALMENTE LO QUE ESTÁ GRABADO EN LA VENTANA)
    # Obs. que no le indicamos a pygame la ventana, él ya sabe las que ha creado y las muestra
    # pygame.display.update()

    # 12 ralentizamos, para que el programa no esté siempre activo... nos damos un respiro...
    # clock.tick(FRAMES_PER_SECOND)   # o sea, esperamos un tick de reloj...