# 1 importamos...
import pygame
import sys
from pygame.locals import *
from simple_button import SimpleButton
# 2 definimos constantes....
pygame.init()
clock = pygame.time.Clock()
TAMAÑO_X = 800
TAMAÑO_Y = 600
BLACK = (0, 0, 0)
FRAMES_PER_SECOND = 30

# 3 iniciamos el entorno pygame
window = pygame.display.set_mode((TAMAÑO_X, TAMAÑO_Y))



# 4 - Load assets: image(s), sound(s), etc.

# 5 # 5 - Initialize variables
aButton = SimpleButton(window, (200, 300), 'images/buttonUp.png', 'images/buttonDown.png')

# 6 blucle infinito...
while True:
    # 7 manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if aButton.handle_events(event):
            print("El usuario ha clicado un botón")

    # 8 acciones a realizar en cada frame

    # 9 borrar
    window.fill(BLACK)

    # 10 volvemos a "dibujar en la ventana (memoria)" de nuevo los elementos...
    aButton.draw()

    # 11 mostramos la pantalla (AHORA ES CUANDO SE MUESTRA REALMENTE LO QUE ESTÁ GRABADO EN LA VENTANA)
    # Obs. que no le indicamos a pygame la ventana, él ya sabe las que ha creado y las muestra
    pygame.display.update()

    # 12 ralentizamos, para que el programa no esté siempre activo... nos damos un respiro...
    clock.tick(FRAMES_PER_SECOND)  # o sea, esperamos un tick de reloj...


