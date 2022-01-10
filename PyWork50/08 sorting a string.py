


def ordena_cadena(word: str):
    # Para ordenar la cadena alfabéticamente lo primero que haremos
    # será invocar la función sort sobre el iterable (en este caso la cadena)
    # esto nos devolverá una LISTA
    # luego habrá que unir todos los ítems...

    # ordenamos... para que ordena alfabéticamente, independientemente de las mayúsculas
    # le pasamos como función key el convertir a minúsculas... esto que hace que, en el iterable
    # utilice el resutlado de la función str.lower() para comparar cada ítem...
    items_ordenados = sorted(word, key=str.lower)
    # items_ordenados = sorted(word) si utilizo esto, cualquier mayúscula va antes, pq ordena por el ascii

    palabra_ordenada = ''.join(items_ordenados)
    return palabra_ordenada

print(ordena_cadena('AstrolabioZ'))


def ordena_alfabeticamente_palabras(cadena: str):
    # Sólo sirve para palabras separadas...
    lista_palabras = cadena.split(' ')
    lista_palabras_ordenadas = sorted(lista_palabras, key=str.lower)
    # Ahora volvemos a unir las palabras, ya separadas por coma...
    cadena_ordenada = ', '.join(lista_palabras_ordenadas)
    return cadena_ordenada

print(ordena_alfabeticamente_palabras('Tom Dick Harry'))


def longes_word(filename):
    output = ''
    for one_line in open(filename):
        for one_word in one_line.split():
            if not one_word.isalpha():
                continue
            if len(one_word) > len(output):
                output = one_word
    return output