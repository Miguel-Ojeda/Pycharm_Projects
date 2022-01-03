import random
import time

# constantes
jugadas = {'p': 'Piedra', 'a': 'Papel', 't': 'Tijera'}
# Resultados
EMPATE = 'Empate'
GANA_1 = 'Ganas tú'
GANA_2 = 'Gana el ordenador'
# Diccionario con el resultado del enfrentamiento...
# Cada combinación es la jugada del primer jugador y la del segudo
# Ejemplo: 'pa' indica que el primer jugador a jugado p (piedra) y el segundo a (papel)
# El resultado puede ser: empate, o True (gana el primero) o False (gana el segundo)
resultados = {'pp': EMPATE, 'pa': GANA_2, 'pt': GANA_1,
              'ap': GANA_1, 'aa': EMPATE, 'at': GANA_2,
              'tp': GANA_2, 'ta': GANA_1, 'tt': EMPATE}

# Inicializamos las variables de la partida
partidas_ganadas = 0
partidas_perdidas = 0
partidas_empatadas = 0
partidas_jugadas = 0

def display_info_partidas():
    print(60 * '-')
    print(f'Partidas jugadas: {partidas_jugadas} \tGanadas: {partidas_ganadas} '
          f'\t Perdidas: {partidas_perdidas} \t Empates: {partidas_empatadas}')
    print(60 * '-')


print("Bienvenido al juego de piedra, papel, tijera...")

while True:
    display_info_partidas()
    while True:
        jugada_persona = input('¿Cuál es tu elección? \t(p)iedra \tp(a)pel \t(t)ijera \t(s)alir  ---->  ')
        # input("¿Qué juegas? \t(p)iedra \tp(a)pel \t(t)ijera \t(s)alir  ----> ")
        if jugada_persona in ('p', 'a', 't', 's'):
            break
    if jugada_persona == 's':
        print('Adiós, hasta pronto...')
        break
    print(f'Bien, ya has elegido tu jugada: {jugadas[jugada_persona]}')
    print('Veamos ahora que elige el ordenador...  --> ', end='')
    time.sleep(2)
    jugada_ordenador = random.choice(('p', 'a', 't'))
    print(f'{jugadas[jugada_ordenador]}')
    print(f'Jugador: {jugadas[jugada_persona]} \tVS \tOrdenador: {jugadas[jugada_ordenador]}')
    combinacion = jugada_persona + jugada_ordenador
    print(combinacion)
    resultado = resultados[combinacion]
    print(f'El resultado es .... {resultado}')
    if resultado == EMPATE:
        partidas_empatadas += 1
    elif resultado == GANA_1:
        partidas_ganadas += 1
    else:
        partidas_perdidas += 1
    partidas_jugadas += 1

print('FIN DE JUEGO')