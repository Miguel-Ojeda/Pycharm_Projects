texto = 'Hola cómo estás'
# Slices...
print(texto[1:4])  # Produce 'ola'

# Si omitimos el primero o el último, se presupone que es desde el principio, o hasta el final, respectivamente
spam = ['cat', 'dog', 'rat', 'eel']
# No se crea ningún objeto, eggs apunta al mismo objeto al que apunta spam
eggs = spam

# Comprobemos que sólo hay un objeto...
if spam is eggs:
    print('Sólo hay un objeto')

# Otra forma de comparary ver que es un objeto, es obteniendo los ids de los objetos a los que apuntan las variables
print(id(spam), ' :', id(eggs))

eggs1 = spam[0:2]  # se crea una lista con los elementos del intervalo (sin incluir el último)
eggs2 = spam[1:]  # a partir del segundo elemento
eggs3 = spam[:3]

print(eggs1, eggs2, eggs3)

# Ojo... [:] significa todo_ y lo que hace es crear un duplicado!!!
eggs = spam[:]
if spam is eggs:
    print('Sólo hay un objeto')
else:
    print('SOn objetos distintos')

# Más claro (pythonic):
eggs = spam.copy()