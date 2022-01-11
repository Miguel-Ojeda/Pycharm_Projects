# Write a function, firstlast, that takes
# a sequence (string, list, or tuple) and
# returns the first and last elements of that sequence,
# in a two-element sequence of the same type.
# So firstlast('abc') will return the string ac,
# while firstlast([1,2,3,4]) will return the list [1,4] and
# firstlast((1, 2, 3, 4)) will return the tupla (1, 4)

# O sea debe devolvernos un objeto del mismo tipo (string, tupla o lista) con el primero y el último
# ¿Cómo hacer para que la implementación sea la misma independientemente del objeto pasado como argumento??

# USANDO SLICES!! nos devuelve objeto del mismo tipo!!!!
# y utilizando el oeprador + que está sobrecargado para este tipo de objetos...

def first_last(secuencia):    # secuencia podría ser string, list o tuple

    # objeto con el primero elemento!!
    # CUidado, no es el elemento en sí, sino el objeto del mismo tipo!!
    objeto_con_primer_elemento = secuencia[:1]  # ES UN OBJETO!! que incluye tan sólo el primer elemento!!
    objeto_con_el_ultimo_elemjento = secuencia[-1:]
    return objeto_con_primer_elemento + objeto_con_el_ultimo_elemjento

    # Podríamos haberlo redactado en una línea, evidentemente
    # return secuencia[-1:] + secuencia[-1:]

# LLamaomos a la función con una cadena
secuencia = "La secuencia es una cadena"
print(first_last(secuencia))
# >>> La

# LLamamos a la función con una lista
secuencia = [0.1, 2, 3, 4, 'abc']
print(first_last(secuencia))
# >>> [0.1, 'abc']

# Llamamos a la función con una tupla
secuencia = ([3.7, '2', 'tupla'], 2.5, 'abecedaario')
print(first_last(secuencia))
# >>> ([3.7, '2', 'tupla'], 'abecedaario')


