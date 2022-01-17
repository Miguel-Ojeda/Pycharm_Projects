# Es un módulo que nos facilita la escritura y recuperación de variables de nuestros programas
# por ejemplo, podemos guardar algunas variables al salir del programa y recuperarlas al entrar
# No hay operaciones distintas para entrada ni para salida...
# se accede simplemente como si fuera un diccionario.... donde la variable a guardar sería la clave

# IMPORTANTE: sólo utilizar shelves que confiemos
# Warning Because the shelve module is backed by pickle, it is insecure to load a shelf
# from an untrusted source. Like with pickle, loading a shelf can execute arbitrary code.

# https://docs.python.org/3/library/shelve.html
# A “shelf” is a persistent, dictionary-like object. the values (not the keys!) in a shelf
# can be essentially arbitrary Python objects — anything that the pickle module can handle.
# This includes most class instances, recursive data types, and objects containing
# lots of shared sub-objects. The keys are ordinary strings.

# Para usarlo debemos primero abrir (o crear, si no existiera el estante, con open)
# Y al final cerrarlo, claro...

import shelve
# Con esto creamos (o abrimos, si no existiera) el 'estante' para nuestras variables
# Se abre para todo_, tanto lectura como escritura, ....
shelf_file = shelve.open('my_data')

# Tenemos variables que queremos guardar en el estante para usarlos luego cuando sea...
lista = [1, 2, '3', ['a', 'b']]
diccionario = {1: [1, 2, 3], 'profesion': 'fontanero'}

# Para guardar variables en el estante, simplemente las asignamos, como si el shelf fuera un diccioanrio
# Elegiremos como clave lo que queramos, pero es más fácil si lo llamamos como la variable que queremos guardar
shelf_file['lista'] = lista
shelf_file['diccionario'] = diccionario

# Cerramos cuando ya está todo_ hecho...
# Es mejor que esto se haga con WITH, así nos ahorramos problemas
shelf_file.close()

# YA ESTÁ, se nos crean varios ficheros (shelf_file.bak, shelf_file.data, shelf_file.dir) con
# todo_ lo necesario para volver a poder acceder al estante y recuperar o seguir guardando los datos


# Hagamos ahora la recuperación de las variables... esto lo podríamos hacer cuando queramos
# en otra ejecución del programa otro día, o de cualquier otro módulo...
# Lo haremos mejor con with !!!
with shelve.open('my_data') as shelf_file:
    lista_recuperada = shelf_file['lista']
    diccionio_recuperado = shelf_file['diccionario']
# shelf_file.close()  NO ES NECESARIO, se hace automáticamente al salir del contexto!!!

print(lista_recuperada, lista == lista_recuperada)
print(diccionio_recuperado, diccionario == diccionio_recuperado)






