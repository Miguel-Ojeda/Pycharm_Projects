# 'with' sirve para crear un 'contexto' de forma que al salir de ese contexto, se ejecuten automáticamente
# alguna secuencia... Esto ayuda a simplificar patrones comunes en el manejo necesario de algunos recursos
# El ejemplo clásico:
with open('hello.txt', 'w') as f:
    f.write('hello, world!')
# Observar que no hace falta poner f.close()
# Lo hace automáticamente al salir del contexto!! (porque está programado, claro!!)

# Esto es realmente equivalente a:
f = open('hello.txt', 'w')
try:
    f.write('hello, world')
finally:
    f.close()

# Observar que la implementación ...
f = open('hello.txt', 'w')
f.write('hello, world')
f.close()
# es incompleta ya que, si por lo que fuera, ocurriera una excepción
# durante f.write,() se quedaría abierto el fichero...

# Con el uso del with es más sencillo; asegura que, para los distintos recursos,
# adquirir y liberarlos sea muy sencillo... tan sólo hay que programar el with
# para nuestros recursos!! (de manera similar a como ya está hecho para los ficheros)

# Otro ejemplo de utilidad del with lo vemos en lo siguiente...
import threading
some_lock = threading.Lock()

# Implementación defectuosa:
some_lock.acquire()
try:
    # Do something...
    pass

finally:
    some_lock.release()

# La opción óptima, que hace uso del with sería...
with some_lock:
    # Do something...
    pass

# En los dos casos que hemos visto (fichero, threading), el uso del with nos permite abstraernos
# de la lógica concreta que lleva el hacer un uso adecuado del recurso... dejamos la labor
# a los programadores del recurso, que ya lo han implementado con el with!!!!
# Ellos ya han implementado el with con los try... finally... adecuados...

# todo_ esto facilita mucho la implementación y claridad del código nuestro, ya que no tenemos
# que recordar limpiar o liberar el recurso al final, etc...

# Cómo hacer para implementar esta gestión con nuestros propios objetos con el 'with' ??


# Opción 1: Writing a class-based context manager
# Deberemos implementar para el objeto un 'context manager', o sea, un protocolo (interface)
# que debe seguir el objeto para poder usarse con el with...
# Básicamente, debemos imploementar para el objeto los métodos  __enter__ y __exit__

# Veamos un ejemplo definiendo una clase Managed_file
# (que realmente no es nada, tan solo un manejador de fichero)
class ManagedFile:
    def __init__(self, name):
        self.name = name

    # Lo que hará el objeto al entrar en el contexto con el with....
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    # Lo que hará el objeto al salir del contexto...
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Ejemplo de uso...
with ManagedFile('hello.txt') as f:
    f.write('hello, world!')
    f.write('bye now')

# Con este objeto, no tenemos ni que hacer un open, ni que hacer el close!!
# Se hacen automáticamente el entrar o salir del context...
# Además, es a prueba de excepciones... pq si ocurre alguna excepción
# automáticamente se saldrá del contexto y, por tanto, se liberará el recurso

# Opción 2 para implementar el with...
# The contextlib utility module in the standard library !!!
# provides a few more abstractions built on top of the basic context manager protocol.
# This can make your life a little easier if your use cases match what’s offered by contextlib.
# Ejemplo:
# Ver ejemplo en el libro Python tricks The book (es un ejemplo que usa generators y no lo entiendo)