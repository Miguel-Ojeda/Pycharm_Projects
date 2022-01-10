# Write a function named printTable() that takes a list of lists of strings
# and displays it in a well-organized table with each column right-justified.
# Assume that all the inner lists will contain the same number of strings.
# For example, the value could look like this:

# tableData = [['apples', 'oranges', 'cherries', 'banana'],
# ['Alice', 'Bob', 'Carol', 'David'],
# ['dogs', 'cats', 'moose', 'goose']]

# Your printTable() function would print the following:
# apples    Alice   dogs
# oranges   Bob     cats
# cherries  Carol   moose
# banana    David   goose

def table_printer(lista):
    # IMPORTANTE: LISTA CONTIENE LISTAS; TODAS LAS SUBLISTAS SUPONEMOS DE IGUAL LONGITUD (SERÍAN LAS COLUMNAS)

    # Vamos a imprimir cada lista ocupando una columna... si hay 3 listas, pues habrán 3 columnas
    # El número de filas va a ser el numero de elementos de cada sublista...
    # Justificaremos los elementos de cada columna a la izquierda, cogiendo un máximo que sea
    # por ejemplo, 5 caracteres más que la palabra más larga...
    # Por tanto para cada columna (lista) miraremos sus elementos para ver la longitud más larga,
    # y le sumaremos un poco más, por ejemplo 5 caracteres

    max_len_sublistas = []
    for sublista in lista:
        max_len = 0
        for item in sublista:
            if len(item) > max_len:
                max_len = len(item)
        max_len += 5
        max_len_sublistas.append(max_len)

    for sublista in lista:
        for item in sublista:
            item.ljust()

    return max_len_sublistas



tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ]

print(table_printer(tableData))