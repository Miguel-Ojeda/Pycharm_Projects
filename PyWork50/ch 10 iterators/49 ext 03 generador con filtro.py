"""
Write a generator function that takes two elements: an iterable and a function.
With each iteration, the function is invoked on the current element.
If the result is True, then the element is returned as is.
Otherwise, the next element is tested, until the function returns True.
Alternative: implement this as a regular function that returns a generator expression.
"""
import string

def generador_filtro(iterable, filtro):
    for item in iterable:
        if filtro(item):
            yield item


# funciones auxiliares
def es_impar(entero):
    return entero % 2


def es_par(entero):
    return not es_impar(entero)


secuencia_1 = [1, 2, 5, 9, 10, 12, 13]
print('secuencia1')

for i in generador_filtro(secuencia_1, es_par):
    print(i)
'''
2
10
12'''
for i in generador_filtro(secuencia_1, es_impar):
    print(i)
'''
1
5
9
13
'''

secuencia_2 = 'abcDEf1256'
print('secuencia2')

for i in generador_filtro(secuencia_2, str.isupper):
    print(i)
'''
D
E
'''
for i in generador_filtro(secuencia_2, str.isalpha):
    print(i)
'''
a
b
c
D
E
f
'''
for i in generador_filtro(secuencia_2, str.isnumeric):
    print(i)
'''
1
2
5
6
'''
print('secuencia3')
secuencia_3 = ['#123', '1254', 'abcde', '12aabcd', '.,-.,-', '#adfdjd']
for i in generador_filtro(secuencia_3, str.isalpha):
    print(i)
# abcde
for i in generador_filtro(secuencia_3, str.isdigit):
    print(i)
# 1254
for i in generador_filtro(secuencia_3, str.isalnum):
    print(i)
'''
1254
abcde
12aabcd
'''