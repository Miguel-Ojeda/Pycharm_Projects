# Python Workouts tema 7

'''Las list comprehensions son un método muy potente, que prácticamente deja obsoleto
a lo que antes hacíamos con las funcioines map y filter...'''

lista = [x * x
         for x in range(10)
         if x % 2 == 0]
print(lista)
'''Antes hacíamos esto con la función map, a la que luego aplicamos un filtro... sería'''

'''La función map aplica una función a un iterable...
(bueno, creo que se puede aplicar a varios iterables!!!)
Por ejemplo, si la función a aplicar tomara dos argumentos, pues habría que darle
dos iterables, para que aplica la función con un ítem de cada secuencia!!!
Ver ejemplo al final...'''
words = 'this is a bunch of words'.split()  # tenemos un iterable
x = map(len, words)  # aplicamos el mapeo que aplica la función len al iterable
# El resultado x es un <map object at 0x000002A5C1CA7700> pero podemos convertirlo en lista para verlo
print(list(x))
# >>> [4, 2, 1, 5, 2, 5]
print(sum(x))  # 19, suma las longitudes de cada palabra de la frase

# Importante, observar que el mapeo siempre tendrá el mismo número de ítems que la secuencia original
# ya que la función se aplica a cada ítem, no hay forma de filtrar!!!

# observar que la función que pasamos a map, sólo toma un argumento, y se le va pasando cada ítem....
# el resultado de evaluar la función en cada ítem es el objeto map resultante, que podremos convertir en lista

# Además, tb tenemos la función filter... tb. toma dos argumentos... una función y un iterable
# la función filter se aplica a cada elemento; la salida de la función filter nos dirá si en el resultado
# final está el ítem, o si es filtrado...
# Si filter(ítem) == True, pues entonces el elemento va a estar en el resultado final... y si es False, pues no...
# Ejemplo:
words = 'this is a bunch of words'.split()
print(words)
# >>> ['this', 'is', 'a', 'bunch', 'of', 'words']
# Si queremos filtrar este lista (iterable) para quedarnos sólo con las de longitud mayor que 4
# podríamos hacer...
def len_gt_4(word):
    return len(word) > 4

# Ahora filtramos para quedarnos con las palabras de longitud mayor que 4
filtrado = filter(len_gt_4, words)
print(type(filtrado))
# Nos retorna una clase filtro
# Que podemos ver como lista...
print(list(filtrado))
# >>> ['bunch', 'words']

'''
The combination of map and filter means that you can take an iterable, filter its elements,
then apply a function to each of its elements. This turns out to be extremely useful
and explains why map and filter have been around for so long—about 50 years, in fact.
'''

'''De todas formas, actualmente podemos conseguir lo mismo con las list comprehensions...
mientras que a los filtros y mapeos les pasamos funciones, a las comprehensions les pasaremos
simplemente expresiones.'''

'''cómo conseguir lo equivalente a 
lista = [x * x
         for x in range(10)
         if x % 2 == 0]
con filtros y map??'''

# Habría que definir la función para el mapeo y para el filtro...
# o utilziar una si ya existiera... en un lambda...
# creo que no existe la de cuadrados... así que la defino....


def f2(x):
    return x ** 2

def pares(x):
    return x % 2 == 0

filtrado = filter(pares, range(10))
mapeado = map(f2, filtrado)
print(list(mapeado))
# >>> [0, 4, 16, 36, 64]

# Claro, podemos resumirlo!!
mapeado = map(f2, filter(pares, range(10)))
print(list(mapeado))

# Lógicamente, las list comprehensions son mucho más sencillas, en un sólo paso hacemos todo
# incluímos las expresiones, y las condiciones, sin necesidad de crear funciones aparte...!!

# Además, podemos hacer cosas a veces con map y filter que es difícil con las comprehensions...
import operator
letters = 'abcd'
numbers = range(1,5)
x = map(operator.mul, letters, numbers)
# En este caso map aplica la función mul y coge un ítem de letters y otro de numbers...
# print(list(x))  # ['a', 'bb', 'ccc', 'dddd']
# observar que tengo que quitar el print anterior, print(list(x)) pq como x es un iterable
# si lo imprimo ya se queda exhausto y entonces la siguiente línea, print(' '.join(x)) no imprime NADA!!
print(' '.join(x))
# >>> a bb ccc dddd

# Conseguir lo anterior con comprehensions puede ser complicado!!!!
# Como tengo que iterar, a la vez, en letra y número tengo que crear
# una nueva secuencia que los combine con zip
import operator
letters = 'abcd'
numbers = range(1, 5)
resultado = ' '.join(operator.mul(letra, numero) for numero, letra in zip(letters, numbers))
print(resultado)
# >>> a bb ccc dddd

# En cambio, con map, si le pasamos dos secuencias, itera a la vez por cada una de ellas
# cogiendo un ítem de cada secuencia, y aplicando la función que hemos pasado...
# Lo mismo si tuviéramos más secuencias... muchas veces es más sencillo
# de entender y programar entonces con map

