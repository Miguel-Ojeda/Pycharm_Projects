'''Los pasos son:
0 Por supuesto, iniciamos pygame (con pygame.init()) y obtenemos una ventana para trabajar con pygame.display.set_mode ....
1º Iniciamos el sistema de fuentes de pygame: pygame.font.init()
2º Obtenemos una fuente para usar: myfont = pygame.font.SysFont('Comic Sans MS', 30)
    También podríamos no ponder ninguna concreta, y utilizaría la por defecto...
    Si quisiéramos obtener una lista de las disponibles en el sistema...
    fonts = pygame.font.get_fonts()
    Podríamos ver cuántas hay: print(len(fonts))
    o imprimirlas...
    for f in fonts:
        print(f)

3º con la fuente, podemos invocar el método render que lo que nos hace es renderizar un texto, utilizando la fuente
    y devolvernos un objeto Surface con el resultado...
    textsurface = myfont.render('Some Text', False, (0, 0, 0))

4º 'Borrar la superficie de dibujo si fuera necesario... o lo que fuera... es opcional...'
    <window>.fill(background)
    O dibujamos un rectángulo previamente en el buffer en la zona... o lo que queramos...

5º Ahora dibujamos en el buffer la superficie con el renderizado....
    <window>.blit(textsurface, location)
    Por supuesto, cada vez que cambie el texto, tenemos que volver a renderizar para obtener la superficie actualizada

6º  Mostrar ya el buffer con nuestra imagen preparada...
    pygame.display.update()

'''

# Ejemplo completo... una cadena que se va actualizando...
import pygame
import pygame.locals
import pygame.font
import sys

# Constantes...
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
FRAMES_PER_SECOND = 30
contador = 0

# Iniciamos pygame, creamos / obtenemos  la superficie de nuestra ventana
pygame.init()
window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# Iniciamos el módulo de fuentes, y obtenemos una con la fuente por defecto
pygame.font.init()
fuente = pygame.font.SysFont(name='comicsans', size=32)

# Obtenemos un reloj
clock = pygame.time.Clock()

while True:
    # 6 Bucle infinito
    while True:

        # 7 Comprobamos los eventos que han sucedido, y damos respuesta a los mismos
        for event in pygame.event.get():
            # el usuario aprieta el botón de cerrar la ventana
            if event.type == pygame.QUIT:
                pygame.quit()  # borra y libera las estructuras....
                sys.exit()  # se termina el programa

            # miramos si ha hecho clic, realmente miramos el mouse_up, que, lógicamente, ha venido después del down...
            if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                contador += 1
                mensaje = f'Hola, el contador vale {contador}'
                # Renderizamos el texto
                text_surface = fuente.render(mensaje, True, (0, 255, 0))
                # Borramos la superficie
                window.fill((0, 0, 0))

                # Ponemos nuestra superficie texto en la mitad de altura del lado izquierdo
                rect_surface = text_surface.get_rect()
                rect_window = window.get_rect()
                # Donde colocamos el texto, abajo y en el centro
                # Para ello partimos de bajo al centro, y movemos un poquito para arriba e izq.
                # para que esté centrado
                location = (rect_window.centerx - rect_surface.width / 2, rect_window.bottom - rect_surface.height)
                window.blit(text_surface, location)

                # actualizamos la pantalla
                pygame.display.update()
                # dormimos un poco
                clock.tick(FRAMES_PER_SECOND)
