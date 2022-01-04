# Conway game of life
import random
import time

MAX_WIDTH = 120
MAX_HEIGHT = 40
# ALIVE_CHAR = 'O'
ALIVE_CHAR = '█'
# ALIVE_CHAR = '■'
# DEAD_CHAR = '□'
DEAD_CHAR = ' '
SETUP_RANDOM = 0
SETUP_ALL_DEAD = 1
SETUP_ALL_LIVE= 2

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
    def __init__(self, width=60, height=40, setup=SETUP_RANDOM):
        self.weight = min(MAX_WIDTH, width)
        self.height = min(MAX_HEIGHT, height)

        # SETUP... 3 modos... aleatorio, todo_ muerto, todo_ vivo....
        if setup == SETUP_ALL_LIVE:
            self.cells = [[ALIVE_CHAR for y in range(self.height)] for x in range(self.weight)]
            return

        # Si no pues rellenamos todo_ con DEAD_CHAR
        self.cells = [[DEAD_CHAR for y in range(self.height)] for x in range(self.weight)]
        # si el setup es todos muertos, ya hemos terminado
        if setup == SETUP_ALL_DEAD:
            return
        # Si no, hemos de elegir al azar, pero como ya existen todas las listas,
        # es más sencillo que con el primer dunder init, no hace falta utilizar append ni nada
        for x in range(self.weight):
            for y in range(self.height):
                if random.choice((0, 1)):
                    self.cells[x][y] = ALIVE_CHAR
                else:
                    self.cells[x][y] = DEAD_CHAR

    def display(self):
        print('\n\n\n\n')
        for y in range(self.height):
            cadena = ''
            for x in range(self.weight):
                cadena += self.cells[x][y]
            print(cadena)


    def update(self):
        old_cells = self.cells.copy()
        for x in range(self.weight):
            for y in range(self.height):
                vecinos_vivos = 0
                # Contamos los vecinos vivos...
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        if i == j == 0:
                            continue   # No contamos a él mismo
                        elif (x + i) in (-1, self.weight) or (y + j) in (-1, self.height):
                            continue    # ¡Están fuera del tablero!!!
                        elif old_cells[x + i][y + j] == ALIVE_CHAR:
                            vecinos_vivos += 1
                # si tiene 3 vecinos vivos, va a estar vivo en la siguiente actualización
                if vecinos_vivos == 3:
                    self.cells[x][y] = ALIVE_CHAR
                # Si tiene 2 vecinos y actualmente está vivo, también va a estar vivo en la siguiente actualización
                elif vecinos_vivos == 2 and old_cells[x][y] == ALIVE_CHAR:
                    self.cells[x][y] = ALIVE_CHAR
                else:
                    self.cells[x][y] = DEAD_CHAR



if __name__ == '__main__':
    automata = Automata(20, 10, setup=SETUP_RANDOM)
    while True:
        automata.display()
        automata.update()
        time.sleep(1)

