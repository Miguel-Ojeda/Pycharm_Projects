"""
Now that you’ve written a function to create passwords, write create_password_checker,
which checks that a given password meets the IT staff’s acceptability criteria.

In other words, create a function with four parameters:
min_uppercase, min_lowercase, min_punctuation, and min_digits.

These represent the minimum number of uppercase letters, lowercase letters, punctuations,
and digits for an acceptable password.

The output from create_password_checker is a function that takes a potential password (string) as its input and
returns a Boolean value indicating whether the string is an acceptable password.
"""
import string

'''
O sea, podríamos hacer esto con una función sola... pero para practicar se nos pide que creemos una función
create_password_checker que nos devuelva funciones especializadas, que verifiquen si los criterios con los que
fueron creadas se cumplen...
'''


def create_password_checker(min_uppercase, min_lowercase, min_punctuation, min_digits):
    """devuelve una función (clousure) que verifica si la cadena que se le pasa
    cumple con los criterios con los que se creó la clousure"""

    def password_checker(cadena: str):
        # Aquí contabilizaremos cuántas veces ocurre cada grupo de caracteres....
        diccionario = {string.ascii_lowercase: 0, string.ascii_uppercase: 0,
                       string.punctuation: 0, string.digits: 0}

        for caracter in cadena:
            for grupo_caracteres in diccionario:
                if caracter in grupo_caracteres:
                    diccionario[grupo_caracteres] += 1

        # O sea, hemos contabilizado para cada carácter cuantas veces se verifica...
        # print(diccionario)

        if diccionario[string.ascii_lowercase] < min_lowercase:
            return False
        elif diccionario[string.ascii_uppercase] < min_uppercase:
            return False
        elif diccionario[string.punctuation] < min_punctuation:
            return False
        elif diccionario[string.digits] < min_digits:
            return False
        else:
            return True

    return password_checker


# Solución de Reuven... tb es original y muy buena, además casi mejor pq da información adicional del fallo
def create_password_checker_Reuven(min_uppercase, min_lowercase, min_punctuation, min_digits):
    uppercase_set = set(string.ascii_uppercase)
    lowercase_set = set(string.ascii_lowercase)
    punctuation_set = set(string.punctuation)
    digits_set = set(string.digits)

    def check_password(password):

        if len([one_character
                for one_character in password
                if one_character in uppercase_set]) < min_uppercase:
            print(f'Not enough uppercase letters; min is {min_uppercase}')
            return False
        elif len([one_character
                  for one_character in password
                  if one_character in lowercase_set]) < min_lowercase:
            print(f'Not enough lowercase letters; min is {min_lowercase}')
            return False
        elif len([one_character
                  for one_character in password
                  if one_character in punctuation_set]) < min_punctuation:
            print(f'Not enough punctuation; min is {min_punctuation}')
            return False
        elif len([one_character
                  for one_character in password
                  if one_character in digits_set]) < min_digits:
            print(f'Not enough digits; min is {min_digits}')
            return False
        else:
            return True
    return check_password


# password checker que comprueba que al menos hay 1 carácter en cada uno de los cuatro grupos
password_checker_1 = create_password_checker(min_uppercase=1, min_digits=1, min_lowercase=1, min_punctuation=1)
resultado = password_checker_1('aBc23,.56')
print(resultado)
resultado = password_checker_1('aBc,.')
print(resultado)

# password checker que comprueba que al menos hay 2 caracteres en cada uno de los cuatro grupos
password_checker_2 = create_password_checker(min_uppercase=2, min_digits=2, min_lowercase=2, min_punctuation=2)
resultado = password_checker_2('aBc23,.56')
print(resultado)
resultado = password_checker_2('aBc,.12B')
print(resultado)

# password checker que comprueba que al menos hay 4 lowercase, y 1 de los demás
password_checker_3 = create_password_checker(min_uppercase=1, min_digits=1, min_lowercase=4, min_punctuation=1)
resultado = password_checker_3('aBc2e3,.56')
print(resultado)
resultado = password_checker_3('azBc,.1e')
print(resultado)
