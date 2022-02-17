"""
Write a “factorial” function that takes any number of numeric arguments and
returns the result of multiplying them all by one another.
"""
def mi_factorial(*args):
    output = 1
    # Si no damos ningún número, también retorna 1,
    # si fuera un problema se podría cambiar...
    for number in args:
        output *= number
    return output


resultado = mi_factorial(2, 3, 6, 10, 1.5, 24)
print(resultado)