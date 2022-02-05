# Conway game of life
import copy
import random
import time
import pygame
import pygame.gfxdraw
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# MÁXIMAS DIMENSIONES PARA EL MUNDO DEL AUTÓMATA
MAX_WIDTH = 120
MAX_HEIGHT = 40

# TIPO DE MUNDO
WORLD_INFINITE = 1
# EL MUNDO ROLLED SIGNIFICA QUE LA FILA / COLUMNA primera son contiguas a las últimas
WORLD_ROLLED = 2

# CARÁCTERES QUE MARCAN SI LAS CÉLULAS ESTÁN VIVAS O MUERTAS
# ALIVE_CHAR = 'O'
ALIVE_CHAR = '█'
# ALIVE_CHAR = '■'
# DEAD_CHAR = '□'
# DEAD_CHAR = 'X'
DEAD_CHAR = ' '

# MODO DE INICIO DEL AUTÓMATA
SETUP_RANDOM = 0
SETUP_ALL_DEAD = 1
SETUP_ALL_LIVE= 2

# CÓMO DIBUJAMOS EL AUTÓMATA EN PYGAME
CELL_AS_SQUARE = 1
CELL_AS_CIRCLE = 2

class Automata:

    # El primer init que definí es más complejo, porque construye las listas poco a poco, con append...
    # def __init__(self, width=60, height=40, setup=SETUP_RANDOM):
    #     self.weight = min(MAX_WIDTH, width)
    #     self.height = min(MAX_HEIGHT, height)
    #
    #     # SETUP... 3 modos... aleatorio, todo_ muerto, todo vivo....
    #     self.cells = []
    #     for x in range(self.weight):
    #         nueva_columna = []
    #         for y in range(self.height):
    #             if setup == SETUP_RANDOM:
    #                 if random.choice((0, 1)):
    #                     nueva_columna.append(ALIVE_CHAR)
    #                 else:
    #                     nueva_columna.append(DEAD_CHAR)
    #             elif setup == SETUP_ALL_LIVE:
    #                 nueva_columna.append(ALIVE_CHAR)
    #             elif setup == SETUP_ALL_DEAD:
    #                 nueva_columna.append(DEAD_CHAR)
    #             else:
    #                 raise Exception('Valor de configuración no válido para el autómata')
    #         self.cells.append(nueva_columna)

    # Sin operaciones append... utilizo list comprehensions inicialmente
    def __init__(self, width=60, height=40, window: pygame.Surface = None,
                 setup=SETUP_RANDOM, world_type=WORLD_ROLLED):
        self.generacion = 1
        self.width = min(MAX_WIDTH, width)
        self.height = min(MAX_HEIGHT, height)
        self.world_type = world_type

        self.old_cells = []  # Esto lo utilizaremos en el proceso de actualización...

        self.window = window
        # Si creamos el autómata con una ventana para mostrar...
        if self.window:
            # Memorizo las dimensiones de la pantalla,
            # Me hacen falta para luego, al dibujar el texto...
            # Aunque por supeusto, podría obtenerlas sobre la marcha con window.get_rect y luego consultar...
            self.display_height = window.get_height()
            self.display_width = window.get_width()
            self.cell_size = min(self.display_width // self.width, self.display_height // self.height)
            # Como probablemente las proporciones no sean las adecuadas y sobre por algún lado
            # Al hacer el dibujo hay que centrar...
            self.margen_x = (self.display_width - (self.cell_size * self.width)) // 2
            self.margen_y = (self.display_height - (self.cell_size * self.height)) // 2
            # Iniciamos también el sistema de fuentes de pygame y guardamos algunas cosas útiles...
            pygame.font.init()
            # Con este objeto fuente, renderizaremos los mensajes de texto
            # para acompañar a la imagen....
            self.fuente = pygame.font.SysFont(name='comicsans', size=16)


        # SETUP... 3 modos... aleatorio, todo_ muerto, todo_ vivo....
        if setup == SETUP_ALL_LIVE:
            self.cells = [[ALIVE_CHAR for y in range(self.height)] for x in range(self.width)]
            return

        # Si no pues rellenamos todo_ con DEAD_CHAR
        self.cells = [[DEAD_CHAR for y in range(self.height)] for x in range(self.width)]
        # si el setup es todos muertos, ya hemos terminado
        if setup == SETUP_ALL_DEAD:
            return
        # Si no, hemos de elegir al azar, pero como ya existen todas las listas,
        # es más sencillo que con el primer dunder init, no hace falta utilizar append ni nada
        for x in range(self.width):
            for y in range(self.height):
                if random.choice((0, 1)):
                    self.cells[x][y] = ALIVE_CHAR
                else:
                    self.cells[x][y] = DEAD_CHAR

    def display(self):
        print(f'\n\n\nDibujando la generación {self.generacion} del Autómata...')
        if self.window:
            self.window_display(modo=CELL_AS_CIRCLE)
        else:
            self.terminal_display()
        # self.terminal_display()

    def terminal_display(self):
        for y in range(self.height):
            cadena = ''
            for x in range(self.width):
                cadena += self.cells[x][y]
            print(cadena)

    def window_display(self, modo=CELL_AS_SQUARE):
        # Definimos lo que es un cuadradito (una célula) del autómata
        color = (0, 255, 0)

        self.window.fill((0, 0, 0))   # Rellenamos el buffer con negro...
        # Obetenemos un cuadradito para poder dibujarlo luego....
        rect = pygame.Rect(0, 0, self.cell_size, self.cell_size)
        # En este rectángulo esta marcado
        top_y = 0
        for y in range(self.height):
            top_x = 0
            for x in range(self.width):
                if self.cells[x][y] == ALIVE_CHAR:
                    rect.x = self.margen_x + top_x
                    rect.y = self.margen_y + top_y
                    if modo == CELL_AS_SQUARE:
                        pygame.draw.rect(self.window, color, rect, 0)
                    elif modo == CELL_AS_CIRCLE:
                        # Versión previa... dibujo cutre porque es un círculo normal, con aliased...
                        # pygame.draw.circle(self.window, color, center=rect.center, radius=self.cell_size / 2 - 1)
                        # UTilizamos mejor las funcioens de fgxdraw que incluyen una circunferencia antialiased!!
                        # Primero dibujmos la circunferencia antialiased, y luego el círculo normal....
                        pygame.gfxdraw.aacircle(self.window, rect.center[0], rect.center[1],
                                                int(self.cell_size / 2) - 1, color)
                        pygame.gfxdraw.filled_circle(self.window, rect.center[0], rect.center[1],
                                                int(self.cell_size / 2) - 1, color)
                top_x += self.cell_size
            top_y += self.cell_size
        # Ahora dibujamos un mensaje de texto abajo del todo, centradito...
        mensaje = f'Game of life ---  Generación: {self.generacion}  ---   Para crear otra generación pulsa "g"'
        text_surface = self.fuente.render(mensaje, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = self.display_width / 2 - text_rect.width / 2
        text_rect.y = self.display_height - text_rect.height
        # location = (self.display_width / 2 - text_rect.width / 2,
        #             self.display_height - text_rect.height)
        # Primero dibujamos un rectángulo negro, como de fondo, por si hubiera algún cell para taparla
        # pygame.gfxdraw.rectangle(self.window, text_rect, (0, 0, 0))
        pygame.gfxdraw.box(self.window, text_rect, (0, 0, 0))
        # Ahora dibujamos el texto
        self.window.blit(text_surface, text_rect)
        pygame.display.update()

    def kill_all_cells(self):
        for y in range(self.height):
            for x in range(self.width):
                self.cells[x][y] = DEAD_CHAR

    def crear_test_1(self, top_x=0, top_y=0):
        # Es la figura de la página 296 de The New Turing Omnibus
        self.kill_all_cells()  # Borramos todo_ primero...
        test_1 = [[DEAD_CHAR, ALIVE_CHAR, ALIVE_CHAR],
                  [ALIVE_CHAR, ALIVE_CHAR, DEAD_CHAR],
                  [DEAD_CHAR, ALIVE_CHAR, DEAD_CHAR]]
        try:
            for i in range(3):
                for j in range(3):
                    self.cells[top_x + i][top_y + j] = test_1[i][j]
        except Exception:
            print('No he podido crear el objeto test_1')

    def crear_glider(self, top_x=0, top_y=0):
        # Es la figura de la columna dcha. de la página 298 de The New Turing Omnibus
        self.kill_all_cells()  # Borramos todo_ primero...
        glider = [[DEAD_CHAR, DEAD_CHAR, ALIVE_CHAR, DEAD_CHAR],
                  [ALIVE_CHAR, DEAD_CHAR, ALIVE_CHAR, DEAD_CHAR],
                  [DEAD_CHAR, ALIVE_CHAR, ALIVE_CHAR, DEAD_CHAR],
                  [DEAD_CHAR, DEAD_CHAR, DEAD_CHAR, DEAD_CHAR]]
        try:
            for i in range(4):
                for j in range(4):
                    self.cells[top_x + i][top_y + j] = glider[i][j]
        except Exception:
            print('No he podido crear el objeto Glider!!')

    def crear_mini_t_invertida(self, top_x=0, top_y=0):
        # Es la figura de la columna dcha. de la página 218 del wheels, life de Martin Gardner
        self.kill_all_cells()  # Borramos todo_ primero...
        mini_t_invertida = [[DEAD_CHAR, ALIVE_CHAR], [ALIVE_CHAR, ALIVE_CHAR], [DEAD_CHAR, ALIVE_CHAR]]
        try:
            for i in range(3):
                for j in range(2):
                    self.cells[top_x + i][top_y + j] = mini_t_invertida[i][j]
        except Exception:
            print('No he podido crear el objeto Glider!!')

    def crear_fila(self, top_x=0, top_y=0, size=7):
        # Es una fila de longitud size... ver pg 298 de The New Turing Omnibus...
        self.kill_all_cells()  # Borramos todo_ primero...
        try:
            for i in range(0, size):
                self.cells[top_x + i][top_y] = ALIVE_CHAR
        except Exception:
            print('No he podido crear el objeto fila')

    def crear_honey_farm(self, top_x=0, top_y=0):
        # Es una fila de longitud 7 ver pg 298 de The New Turing Omnibus...
        self.crear_fila(top_x, top_y, size=7)

    def crear_columna(self, top_x=0, top_y=0, size=7):
        # Es una columna de longitud size... ver pg 298 de The New Turing Omnibus...
        self.kill_all_cells()  # Borramos todo_ primero...
        try:
            for i in range(0, size):
                self.cells[top_x][top_y + i] = ALIVE_CHAR
        except Exception:
            print('No he podido crear el objeto columna')

    def update(self):
        self.generacion += 1

        # self.old_cells = self.cells.copy() NO SIRVE PQ GENERA UNA SHALLOW COPY!!!!
        self.old_cells = copy.deepcopy(self.cells)
        for x in range(self.width):
            for y in range(self.height):
                vecinos_vivos = self.vecinos_vivos(x, y)
                if vecinos_vivos == 3:
                    self.cells[x][y] = ALIVE_CHAR
                # Si tiene 2 vecinos y actualmente está vivo, también va a estar vivo en la siguiente generación
                elif vecinos_vivos == 2 and self.old_cells[x][y] == ALIVE_CHAR:
                    self.cells[x][y] = ALIVE_CHAR
                else:
                    self.cells[x][y] = DEAD_CHAR

    def vecinos_vivos(self, x, y):
        # Utilizamos para ello la copia con el estado previo (antes de actualizar)
        # almacenado en self.old_cells...
        # Esta función es llamada desde update... que lo primero que hace es
        # realizar una deepcopy del estado actual del autómata a old_cells...
        vecinos_vivos = 0
        # Contamos los vecinos vivos...
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i == j == 0:
                    continue  # No contamos como vecino a él mismo
                elif self.world_type == WORLD_INFINITE:
                    # Como el mundo es infinito.... hay que ver si estamos dentro o fuera del autómata...
                    # Si el vecino caer fuera del autómata .... continuar con otro vecino...
                    if (x + i) in (-1, self.width) or (y + j) in (-1, self.height):
                        continue
                    # Estamos dentro... hay que ver si el vecino está vivo...
                    elif self.old_cells[x + i][y + j] == ALIVE_CHAR:
                        vecinos_vivos += 1
                elif self.world_type == WORLD_ROLLED:
                    # Estamos un mundo 'enrrollado, plegado', en el que la primera y las
                    # últimas filas / columnas son adyacentes... para obtener las coordenadas
                    # hay que ver donde se cae cuando antes estaban fuera...
                    vecino_x = (x + i) % self.width
                    vecino_y = (y + j) % self.height
                    if self.old_cells[vecino_x][vecino_y] == ALIVE_CHAR:
                        vecinos_vivos += 1

        return vecinos_vivos


    def update_0(self):
        self.generacion += 1

        # self. = self.cells.copy() NO SIRVE PQ GENERA UNA SHALLOW COPY!!!!
        self.old_cells = copy.deepcopy(self.cells)
        for x in range(self.width):
            for y in range(self.height):
                vecinos_vivos = 0
                # Contamos los vecinos vivos...
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        if i == j == 0:
                            continue   # No contamos como vecino a él mismo
                        elif (x + i) in (-1, self.width) or (y + j) in (-1, self.height):
                            continue    # ¡Están fuera del tablero!!!
                        elif self.old_cells[x + i][y + j] == ALIVE_CHAR:
                            vecinos_vivos += 1
                # si tiene 3 vecinos vivos, va a estar vivo en la siguiente actualización
#                 # logging.debug(f'Posición {[x, y]}, Vecinos: {vecinos_vivos}, valor antiguo: {self.[x][y]}')
                if vecinos_vivos == 3:
#                     # logging.debug(f'Posición {[x, y]}, Vecinos 3')
                    self.cells[x][y] = ALIVE_CHAR
                # Si tiene 2 vecinos y actualmente está vivo, también va a estar vivo en la siguiente actualización
                elif vecinos_vivos == 2:
#                     # logging.debug(f'Posición {[x, y]}, Vecinos 2, valor actual: {self.[x][y]}')
                    if self.old_cells[x][y] == ALIVE_CHAR:
                        self.cells[x][y] = ALIVE_CHAR
#                         # logging.debug(f'Posición {[x, y]}, Vecinos 2, estaba vivo --> vivo')
                    elif self.old_cells[x][y] == DEAD_CHAR:
                        self.cells[x][y] = DEAD_CHAR
#                         # logging.debug(f'Posición {[x, y]}, Vecinos 2, estaba muerto --> muerto')
                else:
                    self.cells[x][y] = DEAD_CHAR




if __name__ == '__main__':
    automata = Automata(20, 10, setup=SETUP_RANDOM)
    while True:
        automata.display()
        automata.update()
        time.sleep(1)

