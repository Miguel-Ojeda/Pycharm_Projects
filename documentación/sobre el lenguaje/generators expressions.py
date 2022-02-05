'''
Leer antes lo de generadores!!!
'''

# Para hacer todavía más sencillo todo, tenemos las generator expressions
# con una sintaxis muy parecida a las list comprehensions, seremos capaces de crear objetos
# iteradores en una sola línea de código


#podemos resumir todo este código para crear y usar un generador...
def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value
iterator = bounded_repeater('Hello', 3)

# En una sola línea de código equivalente!!! con generator expressions
iterator = ('Hello' for i in range(3))
#probésmoslo...
for x in iterator:
    print(x)
# Resultado --> Hello, Hello, Hello

# Similitud entre listas y generator expressions
listcomp = ['Hello' for i in range(3)]
genexpr = ('Hello' for i in range(3))

# Lo de las listas, realmente está creando una lista de 3 ítems
# en cambio el generador no construye ninguna lista!!, simplemente genera los valores 'in time', como un
# iterador o un generador...

# para acceder a los valores del generador tengo que hacer next, o meterlo en un for...
#
# Eso sí, podremos crear una lista desde el generador... simplemente se ejecutaría el next automáticamente
# las veces necesarias e iría creando el objeto lista...
lista = list(genexpr)


'''Sintaxis de los generator expressions
genexpr = (expression for item in collection)

Esto es equivalente a...
def generator():
    for item in collection:
        yield expression
'''

# Por supuesto, como en los list y dict comprehensions, podemos añadir filtros a nuestra generator expressions
even_squares = (x * x for x in range(10) if x % 2 == 0)

'''Así, la sintaxis de los gen expressions queda
genexpr = (expression for item in collection if condition)

que es equivalente al generator
def generator():
    for item in collection:
        if condition:
            yield expression
            
que a su vez es muchísimo más corto que el iterator equivalente!!
'''

# Podemos, y normalmente utilizaremos, inline generator expresions
for x in ('Bom dia' for i in range(3)):
    print(x)

'''
There’s another syntactic trick you can use to make your generator expressions more beautiful.
The parentheses surrounding a generator expression can be dropped if the generator expression
is used as the single argument to a function:

sum((x * 2 for x in range(10)))   
-->
sum(x * 2 for x in range(10))
'''

