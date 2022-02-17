"""
Write a module providing a function that, given a string, returns a dict indicating
how many characters provide a True result to each of the following functions:

    str.isdigit, str.isalpha, and str.isspace.

The keys should be isdigit, isalpha, and isspace.
"""

def string_stats_v0(cadena):
    stats = {}
    stats['isdigit'] = sum([caracter.isdigit()
                            for caracter in cadena])
    stats['isalpha'] = sum([caracter.isalpha()
                            for caracter in cadena])
    stats['isspace'] = sum([caracter.isspace()
                            for caracter in cadena])
    return stats


# Lo mismo, pero un poco más corto con gen expressions
def string_stats_v1(cadena):
    return {'isdigit': sum(caracter.isdigit() for caracter in cadena),
            'isalpha': sum(caracter.isalpha() for caracter in cadena),
            'isspace': sum(caracter.isspace() for caracter in cadena)
            }


# Después de ver lo de Reuven, lo hacer mejor, pq itera una sola vez!!!!!!
# Utiliza un truco, la función getattr: getattr(a, b) es lo mismo que a.b
# De todas formas, creo que es más clara mi versión, la v1
def string_stats_v2(cadena):
    output = dict(isdigit=0, isalpha=0, isspace=0)
    # Observar que hemos creado un diccionario donde las claves
    # nos van a servir también para invocar funciones!!! utilizando getattr
    for letra in cadena:
        for metodo in output:
            output[metodo] += getattr(letra, metodo)()

    return output


if __name__ == '__main__':
    resultado = string_stats_v2('hola como')
    print(resultado)
    resultado = string_stats_v2('hola 1, 2, 3  áb')
    print(resultado)
    resultado = string_stats_v2('12 2323 1abeiou adf')
    print(resultado)