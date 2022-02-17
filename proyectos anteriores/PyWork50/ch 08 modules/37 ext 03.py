"""
Define a module stuff with three variables—a, b, and c—and two functions—
foo and bar.

Define __all__ such that from stuff import * will cause a, c, and
bar to be imported, but not b and foo.
"""

# Pues nada, lo hago en el fichero stuff.py
# Ya está definido... ahora probemos si lo he conseguido...

from stuff import *

print(a)
try:
    print(b)
except NameError as err:
    print(err)

print(c)
foo()
try:
    bar()
except NameError as err:
    print(err)

# El resultado es el esperado...
'''
{8, 1, 2, 6}
name 'b' is not defined  <-----------------------
ABCEDARIO
name 'bar' is not defined  <-----------------------
'''

