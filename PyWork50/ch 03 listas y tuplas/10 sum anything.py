# This challenge asks you to redefine the mysum function we defined in chapter 1,
# such that it can take any number of arguments. The arguments must all be of the
# same type and know how to respond to the + operator. (Thus, the function should
# work with numbers, strings, lists, and tuples, but not with sets and dicts.)

# Resultado buscado...
# mysum('abc', 'def') ---> 'abcdef'
# mysum([1,2,3], [4,5,6]) -->  [1,2,3,4,5,6].
# mysum((1,2,3), (4,5,6), (7, 8, 9, 10)) -->  (1,2,3,4,5,6, 7, 8, 9, 10)

# Of course, it should also still return the integer 6 if we invoke mysum(1,2,3).

# Función mysum original... sólo sirve con argumentos numéricos
# (o con iterables utilizando el operador splat *)
# Ejercicio 02.py
# def mysum(*argv):
#     total = 0
#     for item in argv:
#         total += item
#     return total


def mysum_anything(*argv):
    # Si no hay nada, devolver None
    if not argv:
        return None
    resultado = argv[0]
    # Recordar que los slices no dan error si nos pasamos, simplemente saldría del bucle...
    for item in argv[1:]:
        # 'Sumamos' el siguiente elemento (la suma va a depender del objeto, claro)
        resultado += item
    return resultado


resultado = mysum_anything(1, 2, 3, 4, 5)
print(resultado)

resultado = mysum_anything('hola','como', 'estás', 'hoy' )
print(resultado)

resultado = mysum_anything([2, 5], [3, 7, 2.8, 'a'], [-2.4, complex(2, -5), 'b'])
print(resultado)

resultado = mysum_anything((1, 2, 4), (4, '2.5'), ('abc', 12))
print(resultado)

resultado = mysum_anything([[1, 2, 3], 2], [1, 2, ('a', 'b', 'c')])
print(resultado)