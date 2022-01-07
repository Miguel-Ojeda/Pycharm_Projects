# Recordar que el splat operator * nos permite pasar como argumentos los items de un objeto iterable
# (lista, tupla, set...) mientras que ** nos permite pasar key-value pairs de un diccionario como keyword args...

args = ['cat', 'dog', 'moose']
print(args)
# >>> ['cat', 'dog', 'moose']

print(*args)  # equivalente a print('cat', 'dog', 'moose')
# >>> cat dog moose

# Veamos un ejemplo para crear una función variádica (variadic fucntion).
# Un ejemplo de función variádica es print(), admite un número variable de argumentos...
# Creemos una función suma que admite un número arbitrario de parámetros
def mi_suma(*args):
    # *args indica que va a recibir una lista de items...
    # la función tiene acceso a el objeto iterable realmente, lo que se le pasa realmente es un objeto iterable
    suma = 0
    for valor in args:
        suma += valor
    return suma

print(mi_suma(2, 3, 4, 5, 6, 7, 8, 1, 9))
# print(mi_suma(1, 2, 3, [4, 5, 6]))  DA ERROR!!! porque la función intenta sumar un número a una lista!!
print(mi_suma(1, 2, 3, *[4, 5, 6])) # ESTO SÍ QUE FUNCIONA, lógicmanete, porque desempaqueta la lista....


# Otro ejemplo:
def mi_print(mensaje_inicial, *args):
    # simplemente pongo mensaje_inicial para mostrar que pueden haber otros parámetros antes
    print(mensaje_inicial)
    print(f'El número de argumentos es de:  {len(args)}')
    for index, item in enumerate(args):
        print(f'ELemento {index} ----> {item}')

mi_print('Hola', 1, 2, 5, '98909', [1, 2, 3, 4, 5])
mi_print('Hola', 1, 2, 5, *[i**2 for i in range(1, 5)], *['hola', 'cómo','estás'])

# Funciones variádicas con **
def mi_print_2(*args, **kwargs):
    print(f'Hay {len(args)} argumentos normales y {len(kwargs)} keyword argumentos ')
    print('Los argumentos variables son:')
    for index, item in enumerate(args):
        print(f'ELemento {index} ----> {item}')
    print('Los argumentos keyword son:')
    for key, value in kwargs.items():
        print(f'Clave: {key}, Valor: {value}')

mi_print_2(1, 2, '5', key1='Hola', key2=5)


