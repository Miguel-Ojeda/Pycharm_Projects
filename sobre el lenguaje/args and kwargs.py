# book of python tricks, capítulo de las funciones...
# *args and **kwargs
# *args se usa para la lista de parámetros opcionales, y
# **kwargs para el diccionario con los keyword arguments...
# el uso de estas palabras, permiten a la función usar parámetros opcionales...

def foo(required, *args, **kwargs):
    print(32 * '-')
    print('Required: ', required)
    if args:
        print('Tupla con opcionales: ', args)
    if kwargs:
        print('Diccionario de keyword arguments: ', kwargs)

# si hubiera argumentos adicionales, los recogerá como una tupla
# si hubiera keyword arguments, los recogerá como diccionario...

foo('hello')
foo('hello', 1, 2, 3, 4)
foo('hello', 1, 2, 3, 4, key1='hola', key2=3.14, key3=(1, 2, 5))


# por supuesto, podemos pasar estos argumentos opcionales, o incluso modificarlos y pasarlos a otra función .....
def foo2(x, *args, **kwargs):
    '''Añadimos y modificamos parámetros opcionales y keywords'''
    print(32*'*')
    kwargs['name'] = 'Alice'   # modificamos los keywords args....
    kwargs['funcion']= foo2.__name__
    kwargs['doc']= foo2.__doc__
    if kwargs['key1']:
        kwargs['key1']= 'Adiós'    # si existe el parámetro 'key1', lo modificamos....
    new_args = args + ('extra', )  # añadimos otro elemento a la tupla con los argumentos opcionales...
    foo(x, *new_args, **kwargs) # redirigimos a otra función....

foo('hello', 1, 2, 3, 4, key1='hola', key2=3.14, key3=(1, 2, 5))
foo2('hello', 1, 2, 3, 4, key1='hola', key2=3.14, key3=(1, 2, 5))
