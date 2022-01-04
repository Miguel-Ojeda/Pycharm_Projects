# Usa enumerate en lugar de range, o ...

# Unpythonic...
animals = ['cat', 'dog', 'moose']
for i in range(len(animals)):
    print(animals[i])

# Pythonic...
for animal in animals:
    print(animal)

# Unpythonic...
for i in range(len(animals)):
    print(i, animals[i])

# Pythonic
for index, animal in enumerate(animals):
    print(index, animal)

variable = 14
# Unpythonic...
if variable == True:
    print('Es cierto')

# Método Pythonic:
if variable:
    print('Es cierto')

# Unpythonic
# Podría fallar, (realmente raro) si se trata de una clase y han sobrecargado el operador == de una forma RARA
if variable == None:
    print('Objeto Nulo')

# Pythonic
if variable is None:        # La variable apunta al objeto None, ya que sólo existe un objeto NOne por programa!!!
    print('Objeto Nulo')

# Unpythonic Example
print('The file is in C:\\Users\\Al\\Desktop\\Info\\Archive\\Spam')

# Pythonic Example: usar raw-strings.... (desactivan el operador backslash como escape character....)
print(r'The file is in C:\Users\Al\Desktop\Info\Archive\Spam')

# copiar una lista a un nuevo objeto...
spam = ['cat', 'dog', 'rat', 'eel']
# Unpythonic
eggs = spam[:]
# Pythonic
eggs = spam.copy()  # Más claro, es el método preferido...

# Diccionarios
# Asegurarnos de que existe una key antes de acceder al diccionario...
# Si no hiciéramos nada se generaría una excepción!!!
# Unpythonic...
numberOfPets = {'dogs': 2}
if 'cats' in numberOfPets:  # Check if 'cats' exists as a key.
    print('I have', numberOfPets['cats'], 'cats.')
else:
    print('I have 0 cats.')

# Mucho mejor usar método get.... get(clave, valor a devolver si no existe clave)
# Pythonic Example
numberOfPets = {'dogs': 2}
print('I have', numberOfPets.get('cats', 0), 'cats.')

# Lo mismo para asignar valor por defecto cuando una clave no existe.....
# Imaginemos que queremos sumarle 10 a un valor....
# En el método Pythonic, antes de nada, habría que asegurarse que el valor ya existe...
# antes de usarlo!!! porque si no habría una excepción...
# o si no iniciarlo a 0...
# Unpythonic Example
numberOfPets = {'dogs': 2}
# Primero, si no existe la clave, hacemos que exista con el valor 0
if 'cats' not in numberOfPets:
    numberOfPets['cats'] = 0
# Ahora ya podemos sumarle 10 con seguridad de que no
numberOfPets['cats'] += 10

# Método Pythonic de hacer lo mismo... método sefdefault... (si la clave ya existe, no hace nada, no cambia el valor)
numberOfPets = {'dogs': 2}
numberOfPets.setdefault('cats', 0)  # Does nothing if 'cats' exists.
numberOfPets['cats'] += 10

# O asea, en vez de comprobar si un valor existe en un diccionario antes de usarlo...
# más cómodo y Pythonic usar el método setdefault

# Si esto lo hacemos muchas veces, para eliminar todas estas comprobaciones, es más cómodo
# importar el módulo collections y utilizar la clase defaultdic... es un diccionario
# para iniciar el objeto defaultdic habrá que decirle el tipo de dato a usar por defecto...
# y si no existe él ya hace todo_ lo correcto...
import collections
scores = collections.defaultdict(int)  # creamos un defaultdic que utiliza como por valor por defecto 0
# >>>scores
# defaultdict(<class 'int'>, {})
scores['Al'] += 1
# Observar que no hay necesidad de comprobar si existe la clave 'Al' en el diccionario
# ni con el método unpythonic ni con el pythonic... todo_ ocurre automáticamente ahora...

# Otro ejemplo con defaultdict... ahora poniendolo el tipo de dato por defecto list...
# esto implica que, si no existiera la clave... al utilizarla tendría el valor lista vacía.... []
import collections
booksReadBy = collections.defaultdict(list)
booksReadBy['Al'].append('Oryx and Crake')
booksReadBy['Al'].append('American Gods')
len(booksReadBy['Al'])  # 2
len(booksReadBy['Zophie']) # 0, ya que tiene una lista vacía!!!


# Operador ternario...
# Forma clásica de escribir el código...
# Pythonic way...
condition = True
if condition:
    message = 'Access granted'
else:
    message = 'Access denied'

# Podemos acortar el código con el Python’s “Ugly” Ternary Operator
valueIfTrue = 'Access granted'
valueIfFalse = 'Access denied'
condition = True
message = valueIfTrue if condition else valueIfFalse

# Es una sintaxis 'rara', la hicieron adrede así...
# Por qué la introdujeron (en Python 2.5) pese a que va en contra de... beautiful is better than ugly?
# Había mucha demanda por lo visto.. mejor, aunque más larga, la clásica!!!


# Comparación de valores entre rangos...
spam = 29
# Unpythonic...
if spam > 42 and spam < 99:
    print('El valor de spam es mayor que 42 y menor que 99')

# Pythonic...
if 42 < spam < 99:
    print('El valor de spam es mayor que 42 y menor que 99')

# Assignmente operator.... aisgnaciones múltiples a la vez...
# Pythonic...
spam = eggs = bacon = 'string'

# Comparar igualdad de varios valores... los podemos encadenar...
# Pythonic...
if spam == eggs == bacon == 'string':
    print('Todo es igual... vale ....')

# Comprobar si una variable toma una serie de valores...
# Unpythonic...
if spam == 'cat' or spam == 'dog' or spam == 'moose':
    pass

# Pythonic...   además es más rápido!!!!!
if spam in ('cat', 'dog', 'moose'):   # metemos los valores en una tupla!!!
    pass



