# Conway game of life
import copy
import random
import time
import pygame
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

MAX_WIDTH = 120
MAX_HEIGHT = 40
# ALIVE_CHAR = 'O'
ALIVE_CHAR = '█'
# ALIVE_CHAR = '■'
# DEAD_CHAR = '□'
DEAD_CHAR = 'X'
SETUP_RANDOM = 0
SETUP_ALL_DEAD = 1
SETUP_ALL_LIVE= 2
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
    def __init__(self, width=60, height=40, window:pygame.Surface=None, setup=SETUP_RANDOM):
        self.generacion = 1
        self.width = min(MAX_WIDTH, width)
        self.height = min(MAX_HEIGHT, height)

        self.window = window
        # Si creamos el autómata con una ventana para mostrar...
        if self.window:
            display_height = window.get_height()
            display_width = window.get_width()
            self.cell_size = min(display_width // self.width, display_height // self.height)
            # Como probablemente las proporciones no sean las adecuadas y sobre por algún lado
            # Al hacer el dibujo hay que centrar...
            self.margen_x = (display_width - (self.cell_size * self.width)) // 2
            self.margen_y = (display_height - (self.cell_size * self.height)) // 2

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
                        pygame.draw.circle(self.window, color, center=rect.center, radius=self.cell_size/2 - 1)
                top_x += self.cell_size
            top_y += self.cell_size
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

        # old_cells = self.cells.copy() NO SIRVE PQ GENERA UNA SHALLOW COPY!!!!
        old_cells = copy.deepcopy(self.cells)
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
                        elif old_cells[x + i][y + j] == ALIVE_CHAR:
                            vecinos_vivos += 1
                # si tiene 3 vecinos vivos, va a estar vivo en la siguiente actualización
#                 # logging.debug(f'Posición {[x, y]}, Vecinos: {vecinos_vivos}, valor antiguo: {old_cells[x][y]}')
                if vecinos_vivos == 3:
#                     # logging.debug(f'Posición {[x, y]}, Vecinos 3')
                    self.cells[x][y] = ALIVE_CHAR
                # Si tiene 2 vecinos y actualmente está vivo, también va a estar vivo en la siguiente actualización
                elif vecinos_vivos == 2:
#                     # logging.debug(f'Posición {[x, y]}, Vecinos 2, valor actual: {old_cells[x][y]}')
                    if old_cells[x][y] == ALIVE_CHAR:
                        self.cells[x][y] = ALIVE_CHAR
#                         # logging.debug(f'Posición {[x, y]}, Vecinos 2, estaba vivo --> vivo')
                    elif old_cells == DEAD_CHAR:
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

