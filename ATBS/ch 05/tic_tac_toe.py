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

# TURNOS
TURNO_JUGADOR = 0
TURNO_ORDENADOR = 1



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

        # Ahora borramos todo el tablero para la nueva partida...
        self.board = [CHAR_VACIO for i in range(9)]

        # Cómo se llama el jugador...
        self.player_name = input('¿Cómo te llamas? --> ')
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
        eleccion = random.choice((TURNO_JUGADOR, TURNO_ORDENADOR))
        if eleccion == TURNO_JUGADOR:
            print(f'Empiezas tú... Adelante {self.player_name}')
            self.turno = TURNO_JUGADOR
        else:
            print('Empieza el ordenador... Buena suerte')
            self.turno = TURNO_ORDENADOR

    def print_board(self, elemento_a_imprimir='BOARD'):
        if elemento_a_imprimir == 'BOARD':
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



            # for casilla, contenido in enumerate(self.board):
            #     print(f'Casilla {casilla}: {contenido}')
            return

        # Tenemos que imprimir alguna fila, columna o diagonal....
        # El diccionario self.estructura[elemento_a_imprimir] tiene la tupla con las casillas a imprimir!!!
        # Antes de nada, comprobar que nos han dicho algo válido... claro, como row 1, etc...
        # bastaría poner self.estructura, pq el defecto son las keys....
        if elemento_a_imprimir not in self.estructura.keys():
            print(f'No puedo imprimir la estructura "{elemento_a_imprimir}",' 
                  f'porque no es una estrucura válida del juego Tic Tac Toe')
            print('Las estructuras válidas son: row 1, ... row 3, column 1, .... column 3, diagonal 1, diagonal 2')
            return

        print(f'Imrpimiendo estructura "{elemento_a_imprimir}"... ->', end=' ')
        for casilla in self.estructura[elemento_a_imprimir]:
            print(self.board[casilla], end=' ')
        print('\n')

    def play_next_move(self):
        if self.turno == TURNO_JUGADOR:
            self.play_jugador()
            self.turno = TURNO_ORDENADOR
        else:
            self.play_ordenador()
            self.turno = TURNO_JUGADOR

    def get_empty_cells(self):
        vacios = tuple(i for i in range(9) if self.board[i] == CHAR_VACIO)
        # también podría haber puesto directamente
        # vacios = [i for i in range(9) if self.board[i] == CHAR_VACIO]
        # No sé porqué, pero si pongo el paréntesis solo, no se genera una tupla, sino un generator...
        return vacios

    def get_player_move(self):
        while True:
            casilla = input(f'Es tu turno, {self.player_name}. ¿Qué casilla eliges? --> ')
            try:
                casilla = int(casilla)
                if 0 <= casilla <= 8:
                    return casilla
            except ValueError:  # Es una cadena pero no es posible la conversión a entero...
                pass
            # Tanto si ocurre una excepcción como si llegamos aquí pq el número no es del rango adecuado....
            print('Recuerda, debes introducir un número de casilla válido'
                  f'desde la 0 (la primera) hasta la 8 (la última)')

    def play_jugador(self):
        # obtenemos una tupla con las casillas vacías... o una lista... o lo que sea...
        casillas_vacias = self.get_empty_cells()
        while True:
            opcion_elegida = self.get_player_move()
            # Lo anterior simplemente obtiene un valor entre 0 y 8, no hace ninguna comprobación más...
            if opcion_elegida not in casillas_vacias:
                print('Haz elegido una casilla no válida, ya se encuentra ocupada!!')
                print(f'Las casillas vacías son: {casillas_vacias}')
                continue
            else:
                print(f'Bien, haz elegido la casilla "{opcion_elegida}"')
                self.board[opcion_elegida] = self.player_char
                return  # Y salimos tb. lógicamente, al hacer return... ya hemos movido!!

    def play_ordenador(self):
        pass

if __name__ == '__main__':
    juego = Tic_Tac_Toe_Game()
    juego.print_board()




