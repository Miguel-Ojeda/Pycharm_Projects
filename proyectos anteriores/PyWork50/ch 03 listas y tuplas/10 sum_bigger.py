# Write a function, mysum_bigger_than, that works the same as mysum, except that
# it takes a first argument that precedes *args. That argument indicates the
# threshold for including an argument in the sum. Thus, calling mysum_bigger
# _than(10, 5, 20, 30, 6) would return 50—because 5 and 6 aren’t greater than
# 10. This function should similarly work with any type and assumes that all of the
# arguments are of the same type

def mysum_anything_bigger_than(thresold, *argv):
    # Si no hay nada, devolver None
    if not argv:
        return None
    resultado = None
    # Ahora buscamos algún elemento que sea mayor que el thresold....
    for item in argv:
        if item > thresold:
            # Si ya hay algo acumulado
            if resultado:
                resultado += item
            # Si no teníamos nada todavía...
            else:
                resultado = item
    return resultado


resultado = mysum_anything_bigger_than(3, 1, 2, 3, 4, 5)
print(resultado)

resultado = mysum_anything_bigger_than('dado', 'hola', 'como', 'estás', 'hoy' )
print(resultado)

resultado = mysum_anything_bigger_than([3, 5], [2, 5], [3, 7, 2.8, 'a'], [44, complex(2, -5), 'b'])
print(resultado)

resultado = mysum_anything_bigger_than((2, 3, 4), (1, 2, 4), (4, '2.5'), (14, 12))
print(resultado)