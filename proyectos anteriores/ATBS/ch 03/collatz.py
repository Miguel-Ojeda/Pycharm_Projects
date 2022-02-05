

def collatz(n):
    if n % 2 == 0:
        print(n // 2)
        return n // 2
    else:
        _ = 3 * n + 1
        print(_)
        return _

# Blucle infinito...
while True:
    # Obtenemos el número...
    while True:
        entrada = input('Introduce un número entero no nulo para la secuencia Collatz (x para salir) --> ')
        if entrada == 'x':
            print('Hasta la próxima...')
        try:
            numero = int(entrada)
            # si tenemos éxito  (porque ha introducido un número!!)
            # salimos del bucle que pregunta el número
            break
        except ValueError:
            print('Debes introducir un número entero!!!')

    if numero == 0:
        print('Debes introducir un número no nulo')
        continue

    print(numero)
    while True:
        if numero == 1:
            break
        else:
            numero = collatz(numero)

