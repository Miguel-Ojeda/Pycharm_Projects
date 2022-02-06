# también hay una opción para meter regex permitidas o bloquear regex...
# pero no lo voy a poner aquí...

# interesante ver ahora Custom Validation....
# inputCustom nos permite pasar una función con la que validaremos...

# La función que pasamos a inputCustom, como primer argumento, la tenemos que definir nosotros y debe cumplir:
# Acepta como único parámetro una string que habrá que (validar...)
# Debe invocar una excepción si la string falla la validación
# Returns None (or has no return statement) if inputCustom() should return the string unchanged
# Returns a non-None value if inputCustom() should return a different string from the one the user entered


# Por ejemplo, imagina que queremos pedirle que introduzca una serie de dígitos que sumen 10....
# vamos a crear nuestra propia función de validación... suman_diez

import pyinputplus as pyip
def suman_diez(numeros):   # realmente el parámetro numeros es una string...
    # lo primero, es coger cada digito, cada caracter, por separado...
    lista_numeros = list(numeros)  # será una lista, obtenida de la cadena... cada carácter va a ser un item...
    for i, digit in enumerate(lista_numeros):
        lista_numeros[i] = int(digit)
    if sum(lista_numeros) != 10:
        raise Exception('The digits must add up to 10, not %s.' % (sum(lista_numeros)))
    return int(numeros)  # Return an int form of numbers.