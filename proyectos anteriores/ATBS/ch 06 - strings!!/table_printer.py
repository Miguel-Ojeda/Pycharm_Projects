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
        max_sublista = 5 + max([len(item) for item in sublista])
        max_len_sublistas.append(max_sublista)

    num_items_sublista = len(lista[0])  # todas las sublistas tienen mimsmo número de ítems...

    for j in range(num_items_sublista):
        linea = []
        for i in range(len(lista)):
            linea.append(lista[i][j].rjust(max_len_sublistas[i]))
        print(''.join(linea))


tableData = [['apples', 'oranges', 'Blue cherries', 'banana'],
             ['Alicia', 'Bob Esponja', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'Mary Goose Louis'],
             ]

# print(table_printer(tableData))

table_printer(tableData)