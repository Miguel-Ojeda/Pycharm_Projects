# book of python tricks, capítulo de las funciones...
import functools


# a decorator is a callable that takes a callable as input and returns another callable.
def null_decorator(func):
    print('\n\n.........decorando...   null_decorator\n\n')
    return func

# En vez de hacerlo así podemos "modificarla" sin afectar a la función....
# añadiendo @nombre_del_decorado antes...
@null_decorator
def greet():
    return 'Hola'

# esto realmente es syntatic sugar, es equivalente a hacer --> greet = null_decorator(greet)
# así, cuando hacemos greet() realmente estamos haciendo null_decorator(greet)()

greet()

# otro decorador útil....
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = 'Decorador uppercase...    ' + original_result.upper() + '     ...............'
        return modified_result
    return wrapper

def fun_1():
    return 'hola que tal como estás'

@uppercase
def fun_2():
    return 'hola que tal como estás'

retorno_1 = fun_1()
print(retorno_1)
retorno_2 = fun_2()
print(retorno_2)

def strong_decorator(func):
    def wrapper():
        return '<strong>'+func()+'</strong>'
    return wrapper

def emphasis_decorator(func):
    def wrapper():
        return '<em>'+func()+'</em>'
    return  wrapper

@strong_decorator
@emphasis_decorator
def greet2():
    return 'Hola'

# Se pueden apilar las decoraciones!! se aplican desde la inferior hasta la superior... hacia arriba..
# en este caso, primero se aplica enfasis y luego strong...
retorno = greet2()
print(retorno)

# observar que lo que estamos haciendo realmente es...
# greet2 = strong_decorator(emphasis_decorator(greet2))
# esto significa que realmente al llamar a greet2 se llaman realmente 3 funciones....

# como decorar funciones con argumentos???? *args, **kwargs

def trace(func):
    def wrapper(*args, **kwargs):
        '''Traza funciones...'''
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')
        return original_result
    return wrapper

@trace
def suma(x, y, z):
    '''suma 3 números'''
    return x + y + z

print(suma(3, 5, 7))
print(suma('a30', 'v5', 'c7c0'))

# cuidado, la función suma realmente es trace(suma)
# así que ya otros aspectos no será válidos...
print(suma.__name__)   # no dará name... sino wrapper
print(suma.__doc__)   # no nos dirá que sirva para sumar... sino la docu de la función wrapper!!

# para solucionar esto podemos añadir una decoración al wrapper!!!
# habrá que hacer un import functools
# y decorar al wrapper con el decorador ... >> @functools.wraps(func)
# Así ya funcionará ok
# esto lo que hace es, sobre la marcha, copia los metadatos de la función decorada al wrapper invocado...

# La función trace quedaría entonces... agregando los metadatos de la función decorada...
def trace_ok(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        '''Traza funciones...'''
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')
        return original_result
    return wrapper

@trace_ok
def suma2(x, y, z):
    '''suma 3 números'''
    return x + y + z

print(suma2(3, 4, 6))
print('Suma2: name: ', suma2.__name__)
print('Suma2: doc: ', suma2.__doc__)
#
# As a best practice, I’d recommend that you use functools.wraps in
# all of the decorators you write yourself. It doesn’t take much time and
# it will save you (and others) debugging headaches down the road.