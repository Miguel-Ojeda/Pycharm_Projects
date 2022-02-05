import timeit

# Podemos usar ; para separar las líneas de código!!

# Cuánto se tarda en intercambiar el valor de dos variables??

# cuánto tarda el código para intercambiar dos variables con el truco del XOR  number=1_000_000
tiempo = timeit.timeit('a, b = 42, 101; a = a ^ b; b = a ^ b; a = a ^ b')
print(tiempo) # 0.15106000000378117

# Lo mismo escrito como código con triples comillas
tiempo = timeit.timeit("""a, b = 42, 101
a = a ^ b
b = a ^ b
a = a ^ b""")
print(tiempo)

# Y el intercambio sin ningún truco¿¿
tiempo = timeit.timeit('a, b = 42, 101; temp = a; a = b; b = temp')
print(tiempo)
# 0.038358199992217124 !!! muchísimos menos sin ningún truco, y mucho más legible!!!

# Y con la asignación múltiple??
tiempo = timeit.timeit('a, b = 42, 101; a, b = b, a')
print(tiempo)
# Pues tarda similar... a veces un poco menos incluso!!

# El argumento setup sólo corre una vez...
# Cuánto se tardan en generar 10 millones de números del 1 al 100
# observar que en el setup le metemos lo que queremos que sólo se ejecute una vez!!!
# tiempo = timeit.timeit('random.randint(1, 100)', setup='import random', number=10_000_000)
# print('Generación de 10 millones de numeros al azar entre 1 y 100 -->', tiempo)
# 7.034984400001122 segundos!!! 6'5 segundos... depende!!
# Observar que la libería random sólo se importa una vez, pq está en el parámetro setup

# Por defecto, el código que estamos midiendo no tiene acceso a las variables ni a las funciones del resto del programa
# Si queremos acceder a las variables globales, utilizar globals = global()
var_global = 5
# tiempo = timeit.timeit('random.randint(1, 100) + var_global', setup='import random', number=10_000_000)
# --> NameError: name 'var_blobal' is not defined
tiempo = timeit.timeit('random.randint(1, 100) + var_global', setup='import random',
                       globals=globals(), number=100)
print(tiempo)

def f():
    return 5

# tiempo = timeit.timeit('f()', setup='import random', number=100)
# La función f es desconocida!!!   ---> NameError: name 'f' is not defined

tiempo = timeit.timeit('f()', setup='import random', globals=globals())
print('Función f', tiempo)
# Ahora, con globals, ya es conocida...
# Función f 0.08683270000619814


# Otra opción era haberla importado!!
tiempo = timeit.timeit('f()', setup='from __main__ import f')
print('F importada', tiempo)
# F importada 0.08137419997365214
