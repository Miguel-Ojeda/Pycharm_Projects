# Don’t write one function that finds the largest element of a string, another that
# does the same for a list, and a third that does the same for a tuple.
# Write just one function that works on all of them

def largest_item(secuencia):

    # Primero, si no tuvieramos nada (lista nula, cadena nula, etc) retornar None
    if not secuencia:
        return None

    # Tenemos algo, pues inicialmente ponemos como resultado el primer item...
    resultado = secuencia[0]

    for item in secuencia[1:]:
    # cogemos los items del resto de la secuencia
    # Lo bueno que Python es benévolo en los slices...
    # si no es válido el slice no canta error
    # sino simplemente terminaría el bucle!!!
    # o sea, que no hace falta comprobar ni siquiera si existe el ítem [1]
        if item > resultado:
            resultado = item

    return resultado


