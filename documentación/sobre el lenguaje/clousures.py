"""
Clousures...

Son funciones interiores, definidas, en tiempo de ejecución desde una función padre, que las genera
utilizando argumentos, etc... y nos la devuelve para poder utilizarlas posteriormente...

son funciones creadas dinámicamente, y que recuerdan los valores de las variables con las que se creó...

Ejemplo...
def foo(x):
    def bar(y):
        return x * y
    return bar

La función bar es una clousure... se crea dinámicamente cuando el código ejecuta la función foo

Por ejemplo...
f = foo(10) crea una función (clousure) que lo que hace es multiplicar el número que se le pasa (y) por 10.
Así print(f(20)) nos retorna 200

La clousure creada, f que es foo(10) es un objeto función que 'recuerda' (pq tiene en su código) que se creó
con el 10...
"""