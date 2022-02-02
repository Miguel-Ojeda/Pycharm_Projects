# Libro Python tricks... 6.4 Beautiful Iterators

'''
¿Por qué sirve esto?? qué es el iterador'???
numbers = [1, 2, 3]
for n in numbers:
    print(n)
'''

# Los objetos que soportan __iter__ y __next__ se podrán utilizar de esta forma
'''
Creemos un objeto que soporte estoo... siplemente tiene que soportar el método iter, que nos tienen que devolver 
un método iterador... y luego el método iterador debe soportar __next__
Lo normal será que el iterador esté dentro de la propia clase del objeto...
'''

# Para ver que son dos cosas distintas, que soporte __iter__ y __next__ vamos a empezar con un ejemplo
# en el que el iterador está fuera de la clase del objeto (esto NO ES LO NORMAL)
class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        """ Esto crea un iterador, que es simplemente un objeto que soporta el método next
        Lógicamente, al iniciarse el iterador hará lo que sea necesaria para grabar los datos del objeto
        que lo inició, etc. Pero la implementación del iterador, en este ejemplo, va en otro objeto  """
        return Repeater_Iterator(self)


# En este caso, cuando se invoca __iter__ se devuelve el iterador inicializado con el objeto con el que se creé
# debe ser una clase que soporte el método next, Por ejemplo...
class Repeater_Iterator:
    def __init__(self, source):
        # Grabamos el valor con el que se inició el iterador dede la clase Repeater...
        self.source = source

    def __nex__(self):
        return self.source.value
        # Siempre hace lo mismo, repite infinitamente el valor que tiene guardado!!


# Prueba
'''
repeater = Repeater('Hello')
for i in repeater:
    print(i)
# Repetirá infinitamente 'Hello', tendremos que abortar...
'''


'''
Realmente, el código anterior es syntactic sugar, que realmente se traduce a esto...
repeater = Repeater('Hello')
iterator = repeater.__iter__()   # se crea un iterador concreto para NUESTRO objeto repeater
while True:
    item = iterator.__next__()  # se llama al iterador de nuestro objeto para que nos dé el siguiente ítem...
    print(item)

¿Cómo, si se pone un while True, se para esto?
Porque cuando no quedaran ítems se provocaría una excepción,,, ya lo veremos al final...
'''


''' O sea lo que ocurre es que:
AL llamar al in <nuestro_objeto> automáticamente se llama al método __iter__ de nuestro objeto
y se obtiene un objeto iterador para utilizar
Ese objeto iterador se utiliza las veces necesarias... llamando cada vez a __next__ 
Bueno, También podemos usar lo anterior con las builtin funciones iter(objeto), next(iterador)
que son equivalentes a objeto.__iter__()  y a iterador.__next__() respectivamente!!!
iter(objeto)  --> aplica el méotodo __iter__ a nuestro objeto para genera el iterador..., 
next(iterador) --> aplica el método __netx__ al iterador... es lo mismo'''

'''Escrito más sencillo, la anterior ejecución sería...
repeater = Repeater('Hello')
iterator = iter(repeater)
next(iterator), next(iterator), etc.........
'''

# Observar, como dijimos, que lo más fácil es que el método next esté implementado por el propio objeto
# Así, es todo mucho más fácil, porque el método __iter__ devuelve simplemente el mismo objeto...
# y el método next está en la misma clase... no hacen falta dos objetos!!!!

# La versión del anterior iterador con el méotod next... quedaría

class Repeater_2:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self    # El propio objeto va a ser el iterador, ya que va a implementar el méotod next!!!

    def __next__(self):
        return self.value      # Como antes, retornamos el valor que tenemos, infinitamente!!!

'''
# Hagamos la prueba... recordar que habrá que abortar...
repeater_2 = Repeater_2('Hola 2')
for i in repeater_2:
    print(i)
# Lógiamente, bucle sin fin!!
'''

# O sea, lo normal, o más fácil, es que el iterador sea el propio objeto que implemente el método next
# pero no es obligatorio, como hemos visto antes...

# Cómo hacemos si no queremos iterar para siempre!!
# El iterador, cuando esté exhausto ya, debe hacer saltar una excepción StopIteration, utilizando raise
# En este momento, cuando al llamar al iterador se produzca la excepción, ya sabe el for que se ha acabado...

# Podemos comprobarlo nosotros, en modo interactivo con este código para iterar en una lista
'''
lista = [1, 2, 3]
iterador = iter(lista)
type(iterador)  --> <class 'list_iterator'>
next(iterador)  --> 1
next(iterador)  --> 2
next(iterador)  --> 3
next(iterador)  --> StopIteration
'''

# Vamos a crear un objeto muy sencillo con un iterador supercutre, igual que antes, que repite siempre
# lo mismo, pero ahora lo repite el número de veces que le digamos al iniciar el objeto

class Repeater_limitado:
    def __init__(self, value, max_repeats=10):   # por defecto, se repite 10 veces si no especificamos
        self.value = value
        self.max_repeats = max_repeats
        self.repeticiones = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.repeticiones >= self.max_repeats:
            raise StopIteration
        self.repeticiones += 1
        return self.value


repeater_limitado = Repeater_limitado('Mi mensaje', 15)
for i in repeater_limitado:
    print(i)



# -------------------------------------------

# Veamos otro ejemplo con un objeto lista, o secuencia... que va para alante y luego para atrás, indefinidamente
# es un ejemplo ilustrativo, no está pulido...
class Secuencia_Rebote:
    def __init__(self, secuencia):
        self.secuencia = secuencia
        self._ascendente = True
        self._indice_actual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.secuencia) == 1:
            return self.secuencia[0]
        retorno = self.secuencia[self._indice_actual]
        if self._indice_actual == len(self.secuencia) - 1:
            self._indice_actual -= 1
            self._ascendente = False
        elif self._indice_actual == 0:
            self._indice_actual = 1
            self._ascendente = True
        elif self._ascendente:
            self._indice_actual +=1
        else:
            self._indice_actual -= 1

        return retorno


secuencia_rebote = Secuencia_Rebote([1, 2, 5, 7, 14, 13, 6])
for i in secuencia_rebote:
    print(i )
 # Resultado : 1 2 5 7 14 13 6 13 14 7 5 2 1 2 5 7 14 13 6 13 14 7 5 2 1 ...