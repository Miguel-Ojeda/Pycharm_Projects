# 0 Plantilla genérica para un programa que utilice pygame....
# añadimos el dibujo de una bola
# hacemos que responda a click y que se coloca aleatoriamente...
# y ahora.... en esta evolución del programa introducimos eventos de teclado, .
# el objetivo es meter la bola (colisionar) con un target...
# The user’s goal is to move the ball image so that it overlaps with the target image


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
# esto nos limita donde colocar la esquina superior izquierda para que, al colocar la bola, quede dentro de la ventana
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

# definimos el rectángulo target... al que tenemos que llevar la bola....
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120 # realmente se trata de un cuadrado la zona target!!!
N_PIXELS_TO_MOVE = 3  # los píxeles que desplazaremos la bola en cada movimiento de las teclas...

# 3 iniciamos el entorno de pygame
pygame.init()   # inicializamos las estructuras
# creamos una ventana (surface) para poder dibujar, recibir entradas..
window = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()   # creamos un objeto de la clase Clock, nos va a servir para limitar veolicidad juego...

# 4 - Load assets: image(s), sound(s), etc.
ballImage = pygame.image.load("images/ball.png")
targetImage = pygame.image.load("images/target.jpg")


# 5 - Initialize variables
ball_x = random.randrange(MAX_WIDTH)
ball_y = random.randrange(MAX_HEIGHT)
# definimos un objeto tipo rectángulo (definido en pygame) , con el lugar donde va a estar la imagen...
# va a servir para saber si hacemos click en la bola
# el objeto tipo rectángulo es x, y, dx, dy , donde (x,y) son las coordenadas de la esquina superior izquierda...
# ball_rect = pygame.Rect(ball_x,ball_y, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)   # esto era para v0....
target_rect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)


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

        # miramos si ha hecho click (realmente miramos el mouse_up, que, lógicmanete, ha venido después del down...
        if event.type == pygame.MOUSEBUTTONUP:    # hemos hecho clic en la bola¿¿¿???
            # en este caso, event.pos va a ser la tupla con la posición...
            # podríamos hacer, si quisiéramos:  mouse_x, mouse_y = event.pos
            # y luego hacer cálculos para ver si hemos hecho click en la imagen...
            # pero no nos hace falta: utilizaremos una función de pygame que detecta colisiones, utilizando
            # la posición del ratón y el rectángulo que queremos chequear...
            # o sea, dado un rectángulo, nos dice si la posición indicado está dentro o fuera....
            # <someRectangle>.collidepoint(<someXYLocation>)
            # esto lo anulo... pq era para la v0... ahora estamos con el teclado....
            # print("haciendo click")
            # if ball_rect.collidepoint(event.pos):
            #     print("hemos colisionado")
            #     # cambiamos la posición de la bola..
            #     ball_x = random.randrange(MAX_WIDTH)
            #     ball_y = random.randrange(MAX_HEIGHT)
            #     # y actualizamos el rectángulo que describe la posición de la bola...
            #     ball_rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
            pass
        '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_x -= N_PIXELS_TO_MOVE
            elif event.key == pygame.K_RIGHT:
                ball_x += N_PIXELS_TO_MOVE
            elif event.key == pygame.K_UP:
                ball_y -= N_PIXELS_TO_MOVE
            elif event.key == pygame.K_DOWN:
                ball_y += N_PIXELS_TO_MOVE
            elif event.key == pygame.K_q:
                sys.exit()   # aprovecho el código para poder tb. salir con la letra 'q'
            '''
    # 8 acciones a realizar en cada "frame"...
    # gestionaremos movimiento continuo... capturando qué teclas están apretadas....
    # pasamos el código de la zona de eventos (zona 7) a la 8.... pq ya no estamos chequeando eventos...
    key_pressed = pygame.key.get_pressed()   # nos devuelve una tupla de 0s y 1s (1 indicará tecla apretada...)

    if key_pressed[pygame.K_LEFT]:   # pongo if, y no elif... para que puede chequear varias
        ball_x -= N_PIXELS_TO_MOVE   # teclas simultáneas y, por ejemjplo, porder ir en diagonal...
    if key_pressed[pygame.K_RIGHT]:
        ball_x += N_PIXELS_TO_MOVE
    if key_pressed[pygame.K_UP]:
        ball_y -= N_PIXELS_TO_MOVE
    if key_pressed[pygame.K_DOWN]:
        ball_y += N_PIXELS_TO_MOVE
    if key_pressed[pygame.K_q]:
        sys.exit()

    # en este caso nos toca ver si estamos colisionando la pelota con el target...
    ball_rect = pygame.Rect(ball_x, ball_y, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    # antes vimos un método para ver si un punto está dentro de un rectángulo (colisiona)
    # ahora aplicaremos otro método para ver si dos rectángulos colisionan....
    # < booleanVariable > = < rect1 >.colliderect( < rect2 >)
    if ball_rect.colliderect(target_rect):
        print("Ehy.... la bola está colisionando con el target!! Genial, sigue así!!!")

    # 9 borramos la ventana, antes de volver a redibujar nada...
    # realmente habría q  dibujar el fondo, antes de volver a dibujar los elementos
    window.fill(BLACK)

    # 10 volvemos a "dibujar en la ventana (memoria)" de nuevo los elementos...
    # draw ball at position 100 across (x) and 200 down (y)
    window.blit(targetImage, (TARGET_X, TARGET_Y))  # el target... que está inmóvil siempre....
    window.blit(ballImage, (ball_x, ball_y))    # damos las coordenadas de la esquina superior izquierda...
    # print(TARGET_X, TARGET_Y)



    # 11 mostramos la pantalla  (AHORA ES CUANDO SE MUESTRA REALMENTE LO QUE ESTÁ GRABADO EN LA VENTANA
    # Obs. que no le indicamos a pygame la ventana, él ya sabe las que ha creado y las muestra
    pygame.display.update()

    # 12 ralentizamos, para que el programa no esté siempre activo... nos damos un respiro...
    clock.tick(FRAMES_PER_SECOND)   # o sea, esperamos un tick de reloj...









