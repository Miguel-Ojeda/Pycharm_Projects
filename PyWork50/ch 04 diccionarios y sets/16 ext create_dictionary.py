'''
Write a function that takes any even number of arguments and returns a dict
based on them. The even-indexed arguments become the dict keys, while the
odd-numbered arguments become the dict values. Thus, calling the function
with the arguments ('a', 1, 'b', 2) will result in the dict {'a':1, 'b':2} being
returned.
'''

def create_diccionario(*args):
    diccioanario = {}
    if len(args) % 2:
        print('Error, número impar de argumentos...')
        return
    '''
    Mucho mejor lo que propone Reuven...
    if len(args) % 2:
        raise ValueError('Error, se necesita un número par de argumentos...')
    '''
    for i in range(0, len(args), 2):
        key = args[i]
        value = args[i + 1]
        diccioanario[key] = value
    '''Variación de Reuven... no utilizar nada de i, ni len, ni nada...
    while args:
        output[args[0]] = args[1]
        args = args[2:]
    '''
    return diccioanario


diccionario = create_diccionario(1, 2, 3, 4, 2, 6, 1, 'ab')
print(diccionario)
