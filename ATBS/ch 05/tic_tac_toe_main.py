from tic_tac_toe import *

partida = Tic_Tac_Toe_Game()
nueva_partida = True
# print(partida.get_empty_cells())
while True:

    if nueva_partida:
        partida.iniciar_partida()
        nueva_partida = False

    partida.print_board()
    # print('Jugadas ganadoras... ', partida.get_winner_cells())
    # partida.print_estructuras()

    if partida.turno_jugador:
        partida.play_jugador()
    else:
        partida.play_ordenador()

    if partida.is_winner_last_move():
        if partida.turno_jugador:
            print(f'Felicidades, has ganado, {partida.player_name}')
        else:
            print(f'Ufff. has perdido, {partida.player_name}')
        partida.print_board()
        nueva_partida = True

    # Habrá empate si nadie ha ganado, pero el tablero está ya lleno!!
    elif partida.is_board_full():
        print('La partida ha terminado, ha habido un empate')
        partida.print_board()
        nueva_partida = True

    partida.cambiar_turno()


