from tic_tac_toe import Tic_Tac_Toe_Game

partida = Tic_Tac_Toe_Game()

# print(partida.get_empty_cells())
while True:

    partida.print_board()
    partida.play_jugador()


