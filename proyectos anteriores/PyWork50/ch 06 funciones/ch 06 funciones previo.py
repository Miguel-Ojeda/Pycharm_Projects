# Previo con cosas interesantes de funciones!!!

def display_info_funcion(f):
    """
    Muestra información respecto a una función....
    https: // docs.python.org / 3 / library / inspect.html
    Hay más campos todavía!!!
    """
    print('Code:', f.__code__.co_code)  # string of raw compiled bytecode
    print('Name:', f.__code__.co_name)  # name with which this code object was defined
    print('Argcount:', f.__code__.co_argcount) # number of arguments (not including keyword only arguments, * or ** args)
    print('Varnames (arg. y local var)', f.__code__.co_varnames)  # tuple of names of arguments and local variables
    print('Names (solo local var)', f.__code__.co_names)  # tuple of names of local variables
    print('Freevars (clousures)', f.__code__.co_freevars)  # tuple of names of free variables (referenced via a function’s closure)
    print('Number keyw args', f.__code__.co_kwonlyargcount)  # number of keyword only arguments (not including ** arg)
    print('Constantes usadas', f.__code__.co_consts)  # tuple of constants used in the bytecode
    print('Tamaño del stack', f.__code__.co_stacksize)  # virtual machine stack space required


def f(var1, var2):
    print('Mi constante', var1 - var2)
    variable_local = 'Constante 2'


def f2(var1, var2, *args):
    print(f'Los dos variables posicionales son: "{var1}" y "{var2}"')
    print('también tenemos una tupla de argumentos adicionales')
    print('Aquí están desempaquetados ', *args)
    print('Aquí están sin desempaquetar', args)



f2('Hola es la var 1', 'esta es la segunda variable',
   'primer elemento args', 'segundo elemento args', 'tercer elemento args')


display_info_funcion(f2)
# display_info_funcion(f)


def f3(var1, var2, *args, **kwargs):
    print(f'Los dos variables posicionales son: "{var1}" y "{var2}"')
    print('también tenemos una tupla de argumentos adicionales')
    print('Aquí están desempaquetados ', *args)
    print('Aquí están sin desempaquetar', args)
    print('También tenemos keyword arguments')
    print('Sin desempaquetar:', f'{kwargs}')

f3('var 1', 'var2', 'primer args', 'segundo args', 'tercer args',
   key1='Valkey1', key2='Valkey2', key3='Valkey3')
display_info_funcion(f3)


