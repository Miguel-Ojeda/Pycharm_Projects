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
# aButton = SimpleButton(window, (200, 300), 'images/buttonUp.png', 'images/buttonDown.png')
button_A = SimpleButton(window, (25, 30), 'images/buttonAUp.png', 'images/buttonADown.png')
button_B = SimpleButton(window, (150, 30), 'images/buttonBUp.png', 'images/buttonBDown.png')
button_C = SimpleButton(window, (275, 30), 'images/buttonCUp.png', 'images/buttonCDown.png')

# 6 blucle infinito...
while True:
    # 7 manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if button_A.handle_events(event):
            print("El usuario ha clicado el botón A")
        elif button_B.handle_events(event):
            print("El usuario ha clicado el botón B")
        elif button_C.handle_events(event):
            print("El usuario ha clicado el botón C")

    # 8 acciones a realizar en cada frame

    # 9 borrar
    window.fill(BLACK)

    # 10 volvemos a "dibujar en la ventana (memoria)" de nuevo los elementos...
    button_A.draw()
    button_B.draw()
    button_C.draw()

    # 11 mostramos la pantalla (AHORA ES CUANDO SE MUESTRA REALMENTE LO QUE ESTÁ GRABADO EN LA VENTANA)
    # Obs. que no le indicamos a pygame la ventana, él ya sabe las que ha creado y las muestra
    pygame.display.update()

    # 12 ralentizamos, para que el programa no esté siempre activo... nos damos un respiro...
    clock.tick(FRAMES_PER_SECOND)  # o sea, esperamos un tick de reloj...


