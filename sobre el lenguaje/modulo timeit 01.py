# Podemos usar el módulo timeit para medir lo que tarda en ejecutarse código

import timeit  # Measure execution time of small code snippets¶

# https://docs.python.org/3/library/timeit.html
'''
It has both a Command-Line Interface as well as a callable one.
Ejemplos de uso en CLI
python3 -m timeit '"-".join(str(n) for n in range(100))'
10000 loops, best of 5: 30.2 usec per loop

python3 -m timeit '"-".join(map(str, range(100)))'
0.23702679807320237
'''
'''
Python Interface
timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)
timeit.repeat(stmt='pass', setup='pass', timer=<default timer>, repeat=5, number=1000000, globals=None)
timeit.default_timer()
....
'''
# Muchísimas opciones tiene el código...
# Veamos lo básico....
nombre = 'Miguel'
apellido_1 = 'García'
apellido_2 = 'Morales'
edad = 37

# timeit.timeit("""cadena = 'Mi nombre es %s %s %s y tengo % años' % nombre apellido_1 apellido_2 edad
# """)
# Queremos comparar la velocidad para generar cadenas con 3 métodos...
cadena_1 = 'Mi nombre es %s %s %s y tengo %s años' % (nombre, apellido_1, apellido_2, edad)
cadena_2 = 'Mi nombre es {0} {1} {2} y tengo {3} años'.format(nombre, apellido_1, apellido_2, edad)
cadena_3 = f'Mi nombre es {nombre} {apellido_1} {apellido_2} y tengo {edad} años.'

print(cadena_1)
print(cadena_2)
print(cadena_3)

# Hagamos el timing....
tiempo = timeit.timeit("""
nombre = 'Miguel'
apellido_1 = 'García'
apellido_2 = 'Morales'
edad = 37
cadena_1 = 'Mi nombre es %s %s %s y tengo %s años' % (nombre, apellido_1, apellido_2, edad)
""",
number=10_000)
print('El tiempo con cadena_1 es', tiempo)  # 0.006058500031940639

tiempo = timeit.timeit("""
nombre = 'Miguel'
apellido_1 = 'García'
apellido_2 = 'Morales'
edad = 37
cadena_2 = 'Mi nombre es {0} {1} {2} y tengo {3} años'.format(nombre, apellido_1, apellido_2, edad)
""",
number=10_000)
print('El tiempo con cadena_2 es', tiempo)  # 0.008520699921064079


tiempo = timeit.timeit("""
nombre = 'Miguel'
apellido_1 = 'García'
apellido_2 = 'Morales'
edad = 37
cadena_3 = f'Mi nombre es {nombre} {apellido_1} {apellido_2} y tengo {edad} años.'
""",
number=10_000)
print('El tiempo con cadena_3 es', tiempo)  # 0.003251899965107441

# Otra opción, para no poner las variables dentro del código de timeit, es decir que use el global namespace...
# Veamos los ejemplos anteriores sin tener que asignar las variables (que falsea los resultados, pq las asignamos
# 10000 veces realmente, y no nos interesaría medir eso...
tiempo = timeit.timeit("cadena_1 = 'Mi nombre es %s %s %s y tengo %s años' % (nombre, apellido_1, apellido_2, edad)",
                       globals=globals(), number=10_000)
print(f'El tiempo de cadena_1 con globals activado es {tiempo}')

tiempo = timeit.timeit(
    "cadena_2 = 'Mi nombre es {0} {1} {2} y tengo {3} años'.format(nombre, apellido_1, apellido_2, edad)",
    globals=globals(), number=10_000)
print(f'El tiempo de cadena_2 con globals activado es {tiempo}')

tiempo = timeit.timeit("cadena_3 = f'Mi nombre es {nombre} {apellido_1} {apellido_2} y tengo {edad} años.'",
                       globals=globals(), number=10_000)
print(f'El tiempo de cadena_3 con globals activado es {tiempo}')



# Otro ejemplo comparando búsquedas en listas y en diccionarios
import random


def busca_en_100_valores_lista():
    lista = [random.randint(1, 1000) for i in range(1000)]
    # Ahora buscamos 10000 números a ver si están dentro
    for i in range(10_000):
        esta = i in lista


def busca_en_100_valores_diccionario():
    diccionario = {random.randint(1, 1000): 'HOLA' for i in range(1000)}
    # Ahora buscamos 10000 números a ver si están dentro
    for i in range(10_000):
        esta = i in diccionario

# Si queremos utilizar nuestras funciones, con el argumento setup le decimos que las importe de donde sea...

tiempo_busqueda_lista = timeit.timeit("busca_en_100_valores_lista()",
                                      setup="from __main__ import busca_en_100_valores_lista",
                                      number=10)
print('El tiempo de búsqueda en listas es', tiempo_busqueda_lista)  # 1.3574161999858916


tiempo_busqueda_diccioanario = timeit.timeit("busca_en_100_valores_diccionario()",
                                            setup="from __main__ import busca_en_100_valores_diccionario",
                                            number=10)
print('El tiempo de búsquedas en diccioanrios es', tiempo_busqueda_diccioanario)  # 0.01762189995497465

'''
Hay muchísimas utilidades y opciones en este módulo
Vale la pena verlo y trabajarlo con calma
'''
