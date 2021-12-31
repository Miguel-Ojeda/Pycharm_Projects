# desempaquetado de listas, tuplas, ... operador * Ejemplo *lista
# desempaquetado de diccionarios ... operador  ** Ejemplo **diccionario

x = [1, 2, 3, 4]  # Lista, el desempaquetado da 1, 2, 3, 4
y = range(1, 5)   # rango, el desempaquetado da 1, 2, 3, 4
z = (1, 2, 3, 4)  # Tupla, el des.....

print(x, type(x), *x, '\n', y, type(y), *y, '\n', z, type(z), *z)

x = ['a', 'b', 'c']
# print(*x) daría error, porque es el equivalente a escribir print(a, b, c)
print(*x)

dict = {'edad': 41, 'peso': 83, 'altura': 1.60, 'profesión': 'arquitecto'}
print(dict, type(dict))
# print(**dict) da error, porque es como si hiciéramos print(edad=41, peso=83, ...)
# realmente **dict produce edad=41, peso=83, altura=1.60

def print_vector(x, y, z):
    print('<%s, %s, %s>' % (x, y, z))  # % (tupla de argumentos)

print_vector(1, 2, 6)

# pero que pasa si tenemos un vector ya???
v1 = (1, 2, 6)
v2 = [2, 3, 5]
v3 = range(1, 4)
# primera opción, cutre
print_vector(v1[0], v1[1], v1[2])

# opciones modernas...
# desempaquetar las estructuras, para que a la función se le pasen las 3 componentes!!!
print_vector(*v1)
print_vector(*v2)
print_vector(*v3)

# incluso serviría con diccionarios!!!
dict_vec = {'y': 0, 'z': 1, 'x': 9}
print_vector(**dict_vec)
# es equivalente a print_vector(x=9, y=0, z=1) , ordena los keyword arguments por orden alfabético...

# con esto obtenemos las key... en el orden en el que las hemos pasado
print_vector(*dict_vec)


# unión de listas
lista1 = ['a', 'b', 5, 2.77]
lista2 = [1, 'hola', 5]
lista3 = [(0,4), 'bb', 14]

lista_unida = [*lista1, *lista2, *lista3]
print(lista_unida)

# unión de diccionarios es igual
dict_vec = {'y': 0, 'z': 1, 'x': 9}
dic_otro = {'nombre': 'Eustaquio', 'tupla': (2, 4, 6), 'ID': 4365428, 'password': '2Kwj-POS'}

dic_unido = {**dict_vec, **dic_otro}
print(dic_unido)

# si a un diccionario sólo aplicamos el operador * obtenemos sus keys...
# podemos obtener, por ejemplo, una lista con todas las keys... así...
lista = [*dict_vec, *dic_otro]
print(lista)

# si queremos una tupla, pues igual
tupla = (*dict_vec, *dic_otro)
print(tupla)
