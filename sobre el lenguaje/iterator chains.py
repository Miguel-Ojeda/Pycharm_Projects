# Leer después de iterators, generators, generator expressions

# Podemos combinar varios iterators... para formar una especie de data processing pipeline!!

# Por ejemplo tenemos este generador que genera, consecutivamente, los números del 1 al 8
def integers():
    for i in range(1, 9):
        yield i

# Ahora , por ejemplo, podríamos hacer
'''
generator = integers()
for i in generator:
    print(i)

list(integers())  --> [1, 2, 3, 4, 5, 6, 7, 8]
'''

# veamos como encadenar varios de estos generadores, para que el resultado
# de uno sea a su vez la entrada para que otro actúe, etc...

# Ahora tenemos otro generador...
def squared(seq):
    for i in seq:
        yield i * i

# Podemos encadenar ambos, primero generamos la secuencia del 1 al 8, y luego elevamos al cuadrado
# todo sin crear ningún objeto, con generadores...
chain = squared(integers())
# >>> list(chain)  --> [1, 4, 9, 16, 25, 36, 49, 64]

# Agreguemos otro eslabón
def negated(seq):
    for i in seq:
        yield -i

chain = negated(squared(integers()))
# >>> list(chain)  --> [-1, -4, -9, -16, -25, -36, -49, -64]
# Lo bueno, es que en chain todo se va generando un elemento a la vez!!
# el integer genera un número, por ejemplo el 3... este número pasa a squared... se genera el 9
# y luego pasa a negated y se genera el -9... y luego se genera otro número en integers,... etc


# Podemos compactar todo incluso un poco más, y se sigue entendiendo bastante bien...
integers = range(8)
squared = (i * i for i in integers)
negated = (-i for i in squared)
chain = negated(squared(integers()))
'''
The only downside to using generator expressions is that they can’t
be configured with function arguments, and you can’t reuse the same
generator expression multiple times in the same processing pipeline
'''