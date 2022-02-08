"""Write an anyjoin function that works similarly to str.join, except that the first
argument is a sequence of any types (not just of strings),
and the second argument is the “glue” that we put between elements, defaulting to " " (a space).
So anyjoin([1,2,3]) will return 1 2 3, and anyjoin('abc', pass:'**') will
return pass:a**b**c.
"""

def anyjoin(sequence, glue=' '):
    result = f'{sequence[0]}'
    for item in sequence[1:]:
        result += f'{glue}{item}'

    return result


def anyjoin_v2(sequence, glue=' '):
    """Como siempre, no vi la solución de Reuven, mucho mejor!!!
    Utiliza el método join!!!!
    simplemente, primero tiene que crear la secuencia de strings!!!"""
    return glue.join([str(item) for item in sequence])


resultado = anyjoin([1, 2, 3])
resultado = anyjoin([1, '2', '34', [5, 6, 'hola']], '**')
resultado = anyjoin_v2([1, '2', '34', [5, 6, 'hola']], '**')

print(resultado)

