# Write a function that takes a list or tuple of numbers.
# Return a two-element LIST, containing (respectively)
# the sum of the even-indexed numbers and
# the sum of the odd-indexed numbers.
# So calling the function as
# even_odd_sums([10, 20, 30, 40, 50, 60]),
# you’ll get back [90, 120].

# Lo mismo se devuelve si enviamos una tupla, siempre nos devuelve una LISTA con las dos sumas!!!

def suma_indices_por_paridad(secuencia):
    # Secuencia es una secuencia numérica (lista o tupla)
    suma_impares = 0 # va a contener la suma de sec[0], sec[2], ...
    suma_pares = 0 # va a contener la suma de sec[1], ...
    for i in range(len(secuencia)):
        if i % 2 == 0:
            suma_impares += secuencia[i]
        else:
            suma_pares += secuencia[i]
    return([suma_impares, suma_pares])

secuencia = [10, 20, 30, 40, 50, 60]
print(suma_indices_por_paridad(secuencia))

secuencia = (10, 20, 30, 40, 50, 60)
print(suma_indices_por_paridad(secuencia))

