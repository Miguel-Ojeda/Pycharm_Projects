# Imports
import random

# CONSTANTES...
import time

CHAR_O = 'O'
CHAR_X = 'X'
CHAR_VACIO = ' '
# Caracteres para construir el board...
# U+2500 línea horizontal fina ─
CHAR_LH = '─'
# U 2502 línea vertical │
CHAR_LV = '│'
# U + 250C esquina superior izquierda ┌
CHAR_ESI = '┌'
# U + 2510 esquina superior derecha ┐
CHAR_ESD = '┐'
# U + 2514 esquina inferior iz └
CHAR_EII = '└'
# U + 2518 esquina inferior derecha ┘
CHAR_EID = '┘'
# U + 251C línea vertical y a la derecha ├
CHAR_LVD = '├'
# U + 2524 línea vertical y a la izquierda ┤
CHAR_LVI = '┤'
# U 252C T   ┬
CHAR_T = '┬'
# U 2534 T invertida: ┴
CHAR_T_INV = '┴'
# U 2536 cruz ┼
CHAR_CRUZ = '┼'

class Tic_Tac_Toe_Game:
    def __init__(self):
        # El tablero es simplemente una lista de 9 items, cuyo contenido está inicialmente vacío
        # Inicialmente ponemos los valores del 0 al 9 para mostrar al jugador el tablero en las instrucciones iniciales
        self.board = ['' for i in range(9)]
        self.board = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # Usaremos un diccioanrio para tener identificadas las casillas de filas, columnas, diagonales, etc...
        self.estructura = {'row 1': (0, 1, 2), 'row 2': (3, 4, 5), 'row 3': (6, 7, 8),
                           'column 1': (0, 3, 6), 'column 2': (1, 4, 7), 'column 3': (2, 5, 8),
                           'diagonal 1': (0, 4, 8), 'diagonal 2': (2, 4, 6)}

        # Presentación del Juego...
        print('Bienvenido al juego del Tic Tac Toe (tres en raya)')
        print('Para jugar, simplemente debes elegir una casilla libre a la que mover...')
        print('La numeración de las casillas es la siguiente...')
        self.print_board()

        # Cómo se llama el jugador...
        self.player_name = input('¿Cómo te llamas? --> ')

        # Otras variables que nos harán falta; las inicializaremos en iniciar_partida....
        self.empty_cells = self.ultima_jugada = self.computer_char = self.player_char = self.turno_jugador = None

    def iniciar_partida(self):
        # Borramos el tablero para la nueva partida...
        self.board = [CHAR_VACIO for i in range(9)]

        # Configuramos como disponibles actualmente todas las celdas
        self.empty_cells = [i for i in range(9)]

        # Elegimos ahora las piezas y se sortea el turno...
        while True:
            eleccion = input(f'¿Con qué piezas prefieres jugar, {self.player_name}?  {CHAR_O} ... {CHAR_X} ---> ')
            eleccion = eleccion.upper()
            if eleccion not in (CHAR_O, CHAR_X):
                print(f'Lo siento, {self.player_name}, "{eleccion}" no es una opción válida... Inténtalo de nuevo')
                continue
            else:
                if eleccion == CHAR_X:
                    self.player_char = CHAR_X
                    self.computer_char = CHAR_O
                else:
                    self.player_char = CHAR_O
                    self.computer_char = CHAR_X
                break

        print(f'{self.player_name}, juegas con {self.player_char}. El ordenador jugará con {self.computer_char}.')
        print('Hagamos el sorteo para ver quién empieza primero...')
        time.sleep(2)
        self.turno_jugador = random.choice((True, False))


        if self.turno_jugador:
            print(f'Empiezas tú... Adelante {self.player_name}')
        else:
            print('Empieza el ordenador... Buena suerte')

    def print_board(self):
        size = 3
        # Imprimimos el borde superior del board...
        print(CHAR_ESI + size * CHAR_LH + CHAR_T + size * CHAR_LH + CHAR_T + size * CHAR_LH + CHAR_ESD)
        # Imprimimos los valores de la primera fila del tablero
        print(CHAR_LV + ' ' + self.board[0] + ' ' +
              CHAR_LV + ' ' + self.board[1] + ' ' +
              CHAR_LV + ' ' + self.board[2] + ' ' + CHAR_LV)
        # imprimimos el separador para la segunda fila
        print(CHAR_LVD + size * CHAR_LH + CHAR_CRUZ + size * CHAR_LH + CHAR_CRUZ + size * CHAR_LH + CHAR_LVI)
        # Imprimimos los valores de la segunda fila del tablero
        print(CHAR_LV + ' ' + self.board[3] + ' ' +
              CHAR_LV + ' ' + self.board[4] + ' ' +
              CHAR_LV + ' ' + self.board[5] + ' ' + CHAR_LV)
        # imprimimos el separador para la tercera fila
        print(CHAR_LVD + size * CHAR_LH + CHAR_CRUZ + size * CHAR_LH + CHAR_CRUZ + size * CHAR_LH + CHAR_LVI)
        # Imprimimos los valores de la tercera fila del tablero
        print(CHAR_LV + ' ' + self.board[6] + ' ' +
              CHAR_LV + ' ' + self.board[7] + ' ' +
              CHAR_LV + ' ' + self.board[8] + ' ' + CHAR_LV)
        # Imprimimos el borde inferior del tablero...
        print(CHAR_EII + size * CHAR_LH + CHAR_T_INV + size * CHAR_LH + CHAR_T_INV + size * CHAR_LH + CHAR_EID)

    def print_estructuras(self):
        # Imprimmimos información sobre filas, columnas, etc
        # Para debugging realmente....
        print('Información por estructuras de tablero...')
        for key, values_tupla in self.estructura.items():
            print(f'{key}:', end=' ')
            for item in values_tupla:
                caracter = self.board[item]
                # Para que se vea mejor, si está vacío ponemos un guión
                if caracter == CHAR_VACIO:
                    caracter = '-'
                print(caracter, end=' ')
            print()

    def get_player_move(self):
        while True:
            casilla = input(f'Es tu turno, {self.player_name}. ¿Qué casilla eliges? --> ')
            try:
                casilla = int(casilla)
                if 0 <= casilla <= 8:
                    return casilla
            except ValueError:  # Es una cadena pero no es posible la conversión a entero...
                pass
            # Tanto si ocurre una excepción como si llegamos aquí pq el número no es del rango adecuado....
            print('Recuerda, debes introducir un número de casilla válido '
                  f'desde la 0 (la primera) hasta la 8 (la última)')

    def cambiar_turno(self):
        self.turno_jugador = not self.turno_jugador

    def play_jugador(self):
        # obtenemos una tupla con las casillas vacías... o una lista... o lo que sea...
        while True:
            opcion_elegida = self.get_player_move()
            # Lo anterior simplemente obtiene un valor entre 0 y 8, no hace ninguna comprobación más...
            if opcion_elegida not in self.empty_cells:
                print('Haz elegido una casilla no válida, ya se encuentra ocupada!!')
                print(f'Las casillas vacías son: {self.empty_cells}')
                continue
            else:
                break
        # Actualizamos el juego...
        print(f'Bien, haz elegido la casilla "{opcion_elegida}"')
        self.board[opcion_elegida] = self.player_char
        self.empty_cells.remove(opcion_elegida)
        self.ultima_jugada = opcion_elegida

    def play_ordenador(self):
        '''Queremos que tenga AI
        Criterios para mover serían...:
        1. Si puede ganar, que mueva ahí
        2. Si puede evitar que ganemos, pues que lo evite...
        3. Elegir al azar con prioridad: centro, centro lados, esquinas'''
        # De momento, simplemente elegimos una casilla al azar...
        print('Le toca mover al ordenador...')
        time.sleep(1.5)
        # Actualizamos el juego...
        opcion_elegida = random.choice(self.empty_cells)
        print(f'El ordenador ha elegido la casilla "{opcion_elegida}"')
        self.board[opcion_elegida] = self.computer_char
        self.empty_cells.remove(opcion_elegida)
        self.ultima_jugada = opcion_elegida

    def is_winner_last_move(self):
        # Primero cogemos el carácter del último movimiento
        character = self.board[self.ultima_jugada]

        for casillas in self.estructura.values():
            # Recorremos las estructuras, viendo si la casilla en cuestión está...
            # Si la casilla jugada no pertenece a la fila, col o lo que sea, pues sigue.. pq no hace falta comprobar
            if self.ultima_jugada not in casillas:
                continue
            # Obtenemos una lista con los contenidos de la estructura
            contenido_casillas = [self.board[i] for i in casillas]
            # Si las 3 casillas tienen el carácter buscado, retornamos True....
            if contenido_casillas.count(character) == 3:
                return True

        # SI hemos llegado hasta aquí, es que no es jugada ganadora!!!
        return False

    def is_board_full(self):
        # Si está full, y nadie ha ganada, significa que será empate!!
        if self.empty_cells == []:
            return True
        else:
            return False

    # Obs.... no hace falta definir la función es empate... simplemente ya sabemos si alguien ha ganado...
    # Y si al hacer un movimiento nadie ha ganado, y el tablero está lleno, pues ya estaría...

if __name__ == '__main__':
    juego = Tic_Tac_Toe_Game()
    juego.print_board()
