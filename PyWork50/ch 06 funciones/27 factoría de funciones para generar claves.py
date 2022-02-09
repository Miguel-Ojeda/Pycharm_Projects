"""
In this exercise, we’re going to create factory for password-generation functions.

That is, I might need to generate a large number of passwords, all of which use the same set of characters. (You know
how it is. Some applications require a mix of capital letters, lowercase letters, numbers, and symbols; whereas
others require that you only use letters; and still others allow both letters and digits.)

You’ll thus call the  function create_password _generator with a string.
That string will return a FUNCTION, which itself takes an integer argument.

Calling this function will return a password of the specified length, using the string from which it was
created; for example

alpha_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')
print(alpha_password(5)) # efeaa
print(alpha_password(10)) # cacdacbada
print(symbol_password(5)) # %#@%@
print(symbol_password(10)) # @!%%$%$%%#
"""

"""'''
O sea, tenemos que definir una función que funcione como factoría para crear dinámicamente funciones (clousures)
que sirvan  para generar claves aleatorias con los requisitos que le digamos...


Por ejemplo, necesitamos crear varias claves numéricas... pues utilizando nuestra función generadora crearemos una
función nueva especializada en crear claves numéricas...

A nuestra factoría debemos darle una string que va a indicar los caracteres que debe utilziar la función devuelta para
crear las claves...
Además, las funcioiones creadas tan sólo tienen un argumento, int, que va a indicar la longitud de las clave
que queremos crear...
"""

import random
import string


def create_password_generator(cadena):
    # Definimos nuestra clousure
    def generador(y):
        clave = random.choices(cadena, k=y)
        return ''.join(clave)

    # Ahora la retornamos
    return generador


# Creemos una función generadora de claves numéricas!!!!
generador_clave_numerica = create_password_generator(string.digits)
clave_1 = generador_clave_numerica(10)
clave_2 = generador_clave_numerica(12)
print(clave_1)
print(clave_2)

# Ahora Creemos una función generadora de claves con símbolos de puntuación!!!!!!
generador_clave_simbolos_puntuacion = create_password_generator(string.punctuation)
clave_1 = generador_clave_simbolos_puntuacion(10)
clave_2 = generador_clave_simbolos_puntuacion(10)
print(clave_1)
print(clave_2)

# Creemos una función generador de claves con símbolos alfanuméricos minúsculas
generador_clave_alfanumerica = create_password_generator(string.digits + string.ascii_lowercase)
clave_1 = generador_clave_alfanumerica(10)
clave_2 = generador_clave_alfanumerica(10)
print(clave_1)
print(clave_2)

# Ahora igual pero añadimos algunos caracteres más
# Creemos una función generador de claves con símbolos alfanuméricos minúsculas
generador_clave_alfanumerica_ext = create_password_generator(string.digits + string.ascii_lowercase + '-.,_:*')
clave_1 = generador_clave_alfanumerica_ext(10)
clave_2 = generador_clave_alfanumerica_ext(10)
print(clave_1)
print(clave_2)



