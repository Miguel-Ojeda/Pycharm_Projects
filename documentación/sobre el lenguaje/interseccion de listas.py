# El lenguaje no tiene ningún método para hallar la intersección de 2 listas...
# pero es muy fácil de hallarla
# https://www.geeksforgeeks.org/python-intersection-two-lists/

list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
list_3 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
list_4 = [9, 9, 74, 21, 45, 11, 63, 28, 26]

# Método 1: list comprehension...
# Intersección de lista 1 y 2
interseccion_1 = [item for item in list_1 if item in list_2]
print(interseccion_1)
# Observar que con esta implementación, el elemento 9 aparece repetido 2 veces...
# >>> [9, 10, 5, 4, 9]

# Método 2: crear sets, y luego utilizar el método intersección en los sets....
# Al crearse los sets, la ventaja que tiene es que ya no habrá elementos repetidos
# (puede que esto sea un problema, según lo que queramos hacer...)
set_1 = set(list_1)
set_2 = set(list_2)
print('Set 1:', set_1)
print('Set 2:', set_2)
# Para hallar la intersección utilizamos el operador &
print('Intersección:', set_1 & set_2)
# >>> Intersección: {9, 10, 4, 5}
# Si queremos podemos crear la lista también...
interseccion_1 = list(set_1 & set_2)
print(interseccion_1)
# >>> [9, 10, 4, 5]

# Método 3... usar el método intersection() de los sets...
# Hallamos la intersección de la lista 3 y la 4...
# El método funciona así: <set>.intersection(<lista_de_elementos>)
set_1 = set(list_3)
interseccion_2 = set_1.intersection(list_4)
print(interseccion_2)
# >>> {9, 26, 11, 28}
# Por supuesto, si queremos podemos convertir el set interseccion_2 a una lista...

# Método 5 es con filtros y funciones lambda, ... no lo entiendo!!


