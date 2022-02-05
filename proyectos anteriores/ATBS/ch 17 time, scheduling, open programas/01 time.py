import time
import random
# time()
# returns the number of seconds since the Unix epoch:12 am on January 1, 1970, Coordinated Universal Time (UTC)
print(f'{time.time():.2f}')
# esto se llama epoch timestamp!!
# Podemos usarlo para profile the code... medir cuánta tardo una cierta parte en ejecutarse!!


def comprueba_numero_al_azar():
    lista = [random.randint(1, 1000) for i in range(100)]
    for i in range(100000):
        azar = random.randint(1, 1000)
        estar = azar in lista

def comprueba_numero_al_azar_dict():
    dict = {random.randint(1, 1000): 'HOLA' for i in range(100)}
    for i in range(100000):
        azar = random.randint(1, 1000)
        estar = azar in dict


start_time = time.time()
comprueba_numero_al_azar()
elapsed_time = time.time() - start_time
print(elapsed_time)

start_time = time.time()
comprueba_numero_al_azar_dict()
elapsed_time = time.time() - start_time
print(elapsed_time)

# También podemos usar ctime para ver el tiempo en formato "humano"
# es equivalente a time.asciitime()
print(time.ctime())  # ..> Sun Jan 30 19:40:41 2022

# time.sleep() duerme el programa (bloquándolo) durante los segundos que le digamos

# si queremos mostrar el tiempo con pocos decimales podemos usar la función round (redondeo)
now = time.time()
print(now)  # 1643571794.2505229
print(round(now, 2))  # 1643571794.25
