'''Redefine MyEnumerate as a generator function, rather than as a class'''

def MyEnumerate_v1(iterable, inicio=0):
    for i in range(len(iterable)):
        yield (i + inicio, iterable[i])

def MyEnumerate_v2(iterable, inicio=0):
    indice = inicio
    for data in iterable:
        yield (indice, data)
        indice += 1

lista = [1, 2, 3]
secuencia = 'abcde fgh ijkl'

# Ufff, parece muchísimo más sencillo definir la función generador
# que seguir todo_ el proceso de los iteradores!!

for i in MyEnumerate_v1(lista, 5):
    print(i)

for i in MyEnumerate_v2(secuencia, 3):
    print(i)