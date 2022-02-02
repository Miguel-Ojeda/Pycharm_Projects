"""
Esto va después de leer lo de iterators...
The book of Python tricks... 6.5 Generators Are Simplified Iterators
Son simplemente una forma más sencilla de implementar los iteradores, para poder utilizar en un for, ...
Partamos del iterador cutre que creamos en el documento iterators 01
"""


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


# Lo mismo, hecho con un generador quedaría así... pasando de la clase pasando de una clase para el iterador
# a una función para el generador....
def repeater(value):
    while True:
        yield value

# El generador se parece a una función, pero en vez de return se utiliza yield para arrojar el valor que toca...
# La diferencia es que aquí no partimos de un objeto aparte, sino que ya invocamos el generador...
# Probémoslo...
'''
for i in repeater('Hola'):
    print(i)
# Hola Hola Hola Hola Hola ... indefinido!! como antes pero muchísimo más sencillo de implementar
'''
'''
Cuidado, el generador parece una función, ¡¡PERO NO LO ES!!
Realmente, llamando a la función repeater('Hola') ni siquiera se ejecuta la función!!
Lo que ocurre es que se CREA Y SE DEVUELVE un objeto GENERADOR!!!
'''
print(repeater('Hola'))  # -->    <generator object repeater at 0x0000020CE66B9A80>

# El código de la función sólo se ejecuta donde iría el next(), tanto explícitamente como en el for como vimos
# en el documento de los iteradores...
objeto_generador = repeater('Hola')
print(next(objeto_generador))   # Hola
print(next(objeto_generador))   # Hola
print(next(objeto_generador))   # Hola

'''
Función normal:
--> when a return statement is invoked inside a function, it permanently passes control
back to the caller of the function.

Generador:
--> When a yield is invoked, it also passes control back to the caller of the function,
but it only does so temporarily!!!

Whereas a return statement disposes of a function’s local state, a  yield statement suspends the function
and retains its local state. In practical terms, this means local variables and the execution state of
the generator function are only stashed away temporarily and not thrown out completely.
Execution can be resumed at any time by calling next() on the generator:
'''

'''            ---------------     I M P O R T A N T E   -------------------
O sea, cuando salimos de una función normal, todo su entorno ya desaparece
En cambio, cuando salimos de un generador con yield y luego volvemos a entrar con el siguiente next, cuando toque,
el generador va a recuperar todo su local_scope como estaba antes, con todas las variables exactamente igual
que la vez anterior estaba!! O sea, tiene memoria del estado anterior!!!!
Al llamar a next() se retoma todo como cuando estaba antes!!!!
'''

# Para terminar generando ítems es más fácil, no hace falta generar ninguna excepción como con los iteradores...
# Simplmente, cuando el generador sale de su flujo normal de cualquier otro modo que un yield... en ese caso
# ya se supone que se ha quedado exhausto el generador!!!

# Por ejemplo, aquí tenemos un generador que repite 3 veces...
def three_times_generator(value):
    yield value
    yield value
    yield value

for i in three_times_generator('Hola'):
    print(i)
'''Resultado:
Hola  --> esto se produjo con el código del primer yield
Hola  --> la siguiente vez que se ejecutó el next del generador se siguió el código por donde iba, el segundo yield
Hola  --> ahora se termina con el tercer yield, y como ya el generador acaba pues ya no hay más ítems!!
'''

# Es mucho más sencillo escribir generadores...

# Vamos a escribir un generador rebote... que nos devuelve una secuencia de arriba a abajo,
# y vuelta al revés y ya termina

def rebote_generator(secuencia):
    for i in secuencia:
        yield i
    for i in reversed(secuencia[:-1]):
        yield i

for i in rebote_generator([1, 3, 2, 8, 6, 4, 9]):
    print(i)
# Resultado 1 3 2 8 6 4 9 4 6 8 2 3 1

# Realmente lo que se produce también es una excepción StopIteration, sucede todo automáticamente como con iteradores
generador = three_times_generator('Hola como estás')
print(next(generador))  # Hola como estás
print(next(generador))  # Hola como estás
print(next(generador))  # Hola como estás
print(next(generador))  # StopIteration


# Vamos a implmentar el iterador que repite lo mismo un máximo de veces, que vimos en el capítulo de iteradores
# pero como generador, de dos formas...
'''
Forma 1: (educativa, para ver lo que pasa)

def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return   # El return hace que al abandonar el flujo sin yield, ya se haya exhausto el generador, hemos acabado
        count += 1
        yield value
'''

'''Forma 2: resumida...
def bounded_repeater(value, max_repeats):
    for in in range(max_repeats):
        yield value
'''

# Todo es muchísimo más sencillo que con iteradores1!!  (la versión con iteradores era de 12 líneas , ahora 3!!)

