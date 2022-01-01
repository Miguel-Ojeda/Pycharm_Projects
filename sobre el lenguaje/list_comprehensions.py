# genera la lista [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
list1 = [ 3*i for i in range(11)]

# ['+', '++', '+++', '++++', '+++++', '++++++', '+++++++', '++++++++', '+++++++++', '++++++++++']
list2 = ['+'*i for i in range(1,11)]

# [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
lista3 = [[5 * i + j for j in range(1, 6)] for i in range(3)]

# Los 10 primeros cuadrados...
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lista4 = [x**2 for x in range(1, 11)]

# Lo mismo podemos hacer con sets...
# Se pueden usar las comprehensions con condiciones tb!! para limitar o filtrar sus elementos...
# observar que los sets no están ordenados!!
# Produce el set {'4', '12', '16', '14', '6', '19', '8', '11', '1', '2', '17', '3', '9', '13', '18', '7'}
spam = {str(number) for number in range(21) if number % 5 != 0}

# podemos hacer dictionary comprehensions tb!!
# {'1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81, '10': 100}
spam = {str(number): number**2 for number in range(1, 11)}

# Podemos iterar, en vez de en rangos, en lo que queramos!!!
lista1 = [[0, 1, 2, 3], [4], [5, 6], [7, 8, 9]]

# ['[0, 1, 2, 3]', '[4]', '[5, 6]', '[7, 8, 9]']
lista2 = [str(i) for i in lista1]

# Si quisiéramos convertir en int cada subelemento, para obtener
# [['0', '1', '2', '3'], ['4'], ['5', '6'], ['7', '8', '9']]
# tendríamos que hacer...
lista3 = [[str(i) for i in sublist] for sublist in lista1]

# El peligro es que igual el código se hace oscuro... para conseguir lista3 sería más claro...
lista3 = []
for sublist in lista1:
    lista3.append([str(i) for i in sublist])

print(lista3)

# otro ejemplo
nestedList = [[0, 1, 2, 3], [4], [5, 6], [7, 8, 9]]
flatList = [num for sublist in nestedList for num in sublist]
print(flatList)

#Pero no se entiende bien!!
# Es mejor...
flatlist = []
for sublist in nestedList:
    for element in sublist:
        flatlist.append(element)

print(flatlist)