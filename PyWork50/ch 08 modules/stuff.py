"""
De la página 147 de Python Workouts

Not all names from a module will be imported with import *.

Names starting with _ (underscore) will be ignored.

Moreover, if the module defines a list of strings named __all__,
only names specified in the module will be loaded with import *.

However, from X import Y will always work, regardless of whether __all__ is defined.
"""
# este es el ejercicio 37 ext 03
"""
Define a module stuff with three variables—a, b, and c—and two functions—
foo and bar.

Define __all__ such that from stuff import * will cause a, c, and
bar to be imported, but not b and foo.
"""

a = {1, 2, 6, 8}
b = [2, 3, 8, 14]
c = 'ABCEDARIO'

def foo():
    return 'FOO'

def bar():
    return 'BAR'


__all__ = ['a', 'c', 'foo']