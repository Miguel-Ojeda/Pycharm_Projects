# Write a function that partly emulates the built-in zip function
# Taking any number of iterables and returning a list of tuples.
# Each tuple will contain one element from each of the iterables passed to the function.
# Thus, if I call myzip([10, 20,30], 'abc'), the result will be [(10, 'a'), (20,
# 'b'), (30, 'c')].

# You can return a list (not an iterator) and can assume that all
# of the iterables are of the same length.

# O sea, devuelve una lista de tuplas... en la primera tupla estará el primer elemento de cada iterable...
# en la segunda tupla, pues el segundo, etc

def myzip(*args):
    """ Número variable de argumentos
    Cada argumento es iterable
    Todos los iterables son de la misma longitud
    Debemos retorna una lista de tuplas,
    tantas tuplas como elementos tengas los iterables
    cada tupla está formada por los elementos que ocupan el orden-i de cada iterable
    """
    # Cuántos items tiene cada iterable? COmo todos tienen la misma longitud
    # por ejemplo mmiramos el primer iterable
    n_items_por_iterable = len(args[0])

    tuplas = []
    for i in range(n_items_por_iterable):
        tupla = tuple(arg[i] for arg in args)
        tuplas.append(tupla)

    return tuplas


print(myzip([10, 20, 30], 'abc'))
# >>> [(10, 'a'), (20, 'b'), (30, 'c')]

print(myzip([10, 20, 30, 40], 'abcd', ('primero', 'segundo', 'tercero', 'cuarto')))






