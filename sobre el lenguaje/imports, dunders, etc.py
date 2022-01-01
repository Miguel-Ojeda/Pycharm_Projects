# 1 sobre el leading underscore.... _xxxxx
# es simplemente una forma de decir que el método o atributo es simplemente una
# convención que indica que no se debería acceder a esa función o atributo
# pero se puede!!!!

# Ejemplo:
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23

    def _method(self):
        print(self.foo, self._bar)

    def external(self):
        print('Exernal')

    def _internal(self):
        print('Internal')

t = Test()
# Observar que podemos hacer todo
try:
    print(t.foo)
    print(t._bar)
    t.external()
    t._internal()
except:   # Para cualquier error...
    print('Uff, algo falló')

# Importante, si importamos con un from xxxx import *
# No nos importará ni las variables ni los métodos que empiecen por _
# unless the module defines an __all__ list that overrides this behavior9
# Ejemplo de __all__ podría ser __all__ = ["echo", "surround", "reverse"]
# DE TODAS FORMAS, NO ES ACONSEJABLE UTILIZAR *
# mejor utilizar from xxxx import yyy, zzz, ...
# Veamos el error!!

from imports_aux import *  # método no recomendado, además no se importan elementos con inicio _
t = Test_2()

print(t.x)
print(t.y)
print(t._z)
t.externo()
t._interno()

# Cuidado, acabo de comprobar que SÍ SE IMPORTAN TAMBIÉN!!! igual esto a cambiado en el nuevo intérprete...

# 2 single trailing _
# se usa cuando queremos utilizar como nombre de variable una palabra reservada por Python...
# Podemos evitar fácilmente el conflicto añadiendo al final el _
# Ejemplo:
# La siguiente línea daría error en la definición... ¡No podemos poner a un parámetro el nombre class!!
# def make_object(name, class):
# Cómo lo podemos arreglar?? poniendo otro nombre, evidentemente, pero lo más sencillo sería con el _
def make_object(name, class_):
    return class_(name)

class perro:
    def __init__(self, name):
        self.name = name

    def saluda(self):
        print(f'Hola, soy un perro .... Me llamo {self.name}')

class gato:
    def __init__(self, name):
        self.name = name

    def saluda(self):
        print(f'Hola, soy un gato .... Me llamo {self.name}')

animal_1 = make_object('timi', perro )
animal_1.saluda()
animal_2 = make_object('ginni', gato)
animal_2.saluda()


# 3 Double leading underscore (dunder) __
# causa que el intérprete haga name mangling... o sea, cambie (de forma transparente)
# el nombre a _<nombre_de_la_clase>__..
# se hace pq al crear clases derivadas, no se generan conflictos con las subclases...
# Ejemplo
class Test_3:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 'Baz en Test 3'


t = Test_3()
# Veamos los atributos del objeto con la built-in function dir()
print (dir(t))
# Observamos que el atributo realmente se llama _Test_3__baz
# Esto se hace para proteger a esta variable para que no sea sobreescrita cuando se genera
# una subclase, sino que siga existiendo la variable __baz de la original, además de la derivada tb.
# Por supuesto, desde dentro de la clase podremos acceder sin problemas a la variable, pero desde fuera....
# print(t.__baz)  DARÍA ERROR
# Pero sí que podemos acceder desde fuera al valor si queremos, simplemente...
print(t._Test_3__baz)
# >>> 35

# ¿QUé pasa cuando creamos una clase derivada?
# Pues se mantendrá el __baz original y se creará tb otro __baz derivado...
# Ejemplo:
class Extended_test(Test_3):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'Bazzz en Extended'

# Lo que pasa es que ahora tendremos...
# __baz original: que tras el name mangling se llama _Test_3__baz
# __baz de Extended_test que ahora se llama _Extended_test__baz
t = Extended_test()
print(dir(t))
print(t._Test_3__baz)
print(t._Extended_test__baz)

# 4 Double leading and trailing underscores....    __XXXX__
# Aquí no se aplica ya el name mangling!!!
# y se puede acceder sin ningún problema!!!
# Normalmente, se utilizan con nombre reservados
# Ejemplos: __init__, __call__ (para hacer un objeto callable), __str__, __eq__ , etc...
# Mejor no usarlos inventados, por si acaso hay alguna colisión cuando evolucione Python....
# Mejor utilizar los que ya hay ...

# 5 single underscore    _
# Indica una variable temporal e insignificante, a la que ni siquiera nos apetece nobmrar...
for _ in range(32):
    print('Hello World')

# Se suelen utilizar tb para el desempaquetado, cuando no nos interesean algunos valores
# ni nos molestamos en darle nombre...
# Ejemplo tenemos una tupla que representa a un coche, y nos intereesa el color y el cuentakilómetros (primer y último)
car = ('red', 'auto', 12, 3812.4)
color, _, _, mileage = car
print(f'El color es {color} y {mileage} kilómetros')
# Además es interesante porque tb guarda el último valor retornado por el INTÉRPRETE
# >>> 24 + 4
# >>> _ será 28
# También para crear en el intérprete objetos sobre la marcha, sin interesarnos el nombre...
# >>> list()
# []
# >>> _.append(1)
# >>> _.append(2)
# >>> _.append(3)
# >>> _
# [1, 2, 3]
