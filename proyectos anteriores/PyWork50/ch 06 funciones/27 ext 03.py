"""
Write a function, do_both, that takes two functions as arguments (f1 and f2) and
returns a single function, g. Invoking g(x) should return the same result as
invoking f2(f1(x)).

O sea, nos tien que retornar la función compuesta f2 f1
"""

def create_compuesta(func_1, func_2):
    def g(x):
        return func_2(func_1(x))

    return g


# Ejemplo
def f1(x):
    return x + 3

def f2(x):
    return 3 * x - 5

g = create_compuesta(f1, f2)

print(g(10))
# >>> 34
# Es correcto... f1(10) = 13; f2(13) = 39 -5 = 34