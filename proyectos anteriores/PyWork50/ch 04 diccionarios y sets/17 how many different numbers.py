"""
Write a function, called how_many_different_numbers, that
takes a single list of integers and returns the number of different integers it contains.
"""


def how_many_different_numbers(lista):
    conjunto = set(lista)
    return len(conjunto)


def how_many_different_numbers_v2(lista):
    # Esta vez hago yo la función, sin utilizar el constructor del Set con las listas
    conjunto = set()
    '''Mejor utilizar con los sets en este caso el método update...
    que mete en el conjunto los valores del iterable
    for item in lista:
        conjunto.add(item)
    '''
    conjunto.update(lista)
    return len(conjunto)


def how_many_different_numbers_v3(lista):
    ''' Esta versión es otra posibilidad, que utiliza el operador splat *
    Recordar que * despliega el iterable, mostrando sus elementos...
    Entonces si lista = [1, 2, 3, 4, 1, 2], pues *lista es 1, 2, 3, 4, 1, 2
    conjunto = {*lista} es lo mismo que decir conjunto = {1, 2, 3, 4, 1, 2}

    O sea, conjunto = {*lista} es realmente lo mismo que conjunto = set(lista)
    Lo malo es que quizás pierde claridad el código...!!!
    Creo que es muchísimo más claro utilizar ---->
    conjunto = set(lista_numeros) en vez de conjunto = {*lista_numeros}
    '''
    conjunto = {*lista}
    return len(conjunto)
    # O simplemente una línea... return len({*lista})



numbers = [1, 2, 3, 1, 2, 3, 4, 1, 7, 3, 10, 1, 1, 3, 4, 1, 7]
print(how_many_different_numbers_v3(numbers))
