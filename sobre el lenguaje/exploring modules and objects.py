'''
8.1 del libro Python Tricks
'''
import pprint

'''
Para saber lo que hay en un módulo podemos utilizar el REPL y el comando dir()
Por ejemplo, qué hay en el módulo datetime??

import datetime
dir(datetime)

Lo podemos hacer en el REPL, es lo más fácil, también se puede en un script, claro
'''

import datetime
lista = dir(datetime)
print(lista)
'''
['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
'__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
'''

# Esto nos sirve para explorar cualquier objeto, por ejemplo si queremos inspeccionar cómo es la clase datetime.date
lista = dir(datetime.date)
print(lista)
'''
['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', , 
'__gt__', '__hash__', '__init__', ...
'''

class Ejemplo:
    """
    Esto es una clase de ejemplo q bla bla bla
    """
    clas_constant = 'CLASE EJEMPLO'
    def __init__(self, value):
        self.value = value
        self.value2 = value * 2
        self.value3 = value ** 2

    def get_total(self):
        return self.value * self.value2 + self.value3


lista = dir(Ejemplo)
print(lista)
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'clas_constant', 'get_total']
'''
# Vemos que casi todo son cosas que incluye Python... las nuestras son nuestro __init__ y los dos ítems del final
# Lo otro lo hereda cualquier clase que definamos, y podemos definirlo nosotros para sobrecargar operadores, etc...
print(Ejemplo.__dict__)

# Si queremos buscar info con dir, pero filtrando los resultados, podemos hacerlo fácilmente....
# Por ejemplo, buscar la información de datetime, como al principio, pero sólo aquella información
# que contenga la palabra date...

lista = [info for info in dir(datetime) if 'date' in info.lower()]
# o lista = [_ for _ in dir(datetime) if 'date' in _.lower()]
print(lista)  # --> ['date', 'datetime', 'datetime_CAPI']

# Además, también podemos usar help, lo mejor, como decimos, en el REPL
info = help(datetime)
print(info)
'''
Help on module datetime:

NAME
    datetime - Fast implementation of the datetime type.

MODULE REFERENCE
    https://docs.python.org/3.10/library/datetime.html
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete .....
    .....
    .....
'''

# Por supuesto, esto es aplicable a cualquier objeto incluido en el módulo, o en mi propio programa
# si incluye doc strings...
print(help(datetime.date))
'''
Help on class date in module datetime:

class date(builtins.object)
 |  date(year, month, day) --> date object
 |  
 |  Methods defined here:
 |  
 ........
 ........
 '''

print(help(datetime.date.fromtimestamp))
'''
Help on built-in function fromtimestamp:

fromtimestamp(timestamp, /) method of builtins.type instance
    Create a date from a POSIX timestamp.
    
    The timestamp is a number, e.g. created via time.time(), that is interpreted
    as local time.
'''

print(help(Ejemplo))
'''
Help on class Ejemplo in module __main__:

class Ejemplo(builtins.object)
 |  Ejemplo(value)
 |  
 |  Esto es una clase de ejemplo q bla bla bla
 |  
 |  Methods defined here:
 |  
 |  __init__(self, value)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  get_total(self)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  clas_constant = 'CLASE EJEMPLO'

None
'''