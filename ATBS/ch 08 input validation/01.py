# importamos el módulo con la validación de datos (Al Sweigart)
# import pyinputplus


# Alguna de las funciones que contiene... (contiene muchos más!!!)

# inputStr() Is like the built-in input() function but has the general PyInputPlus features.
# You can also pass a custom validation function to it.

# inputNum() Ensures the user enters a number and returns an int or # float, depending
# on if the number has a decimal point in it

# inputInt(), inputFloat()

# inputChoice() Ensures the user enters one of the provided choices

# inputMenu() Is similar to inputChoice(), but provides a menu with numbered or lettered options

# inputDatetime() Ensures the user enters a date and time

# inputYesNo() Ensures the user enters a “yes” or “no” response

# inputBool() Is similar to inputYesNo(), but takes a “True” or “False” response and returns a Boolean value

# inputEmail() Ensures the user enters a valid email address

# inputFilepath() Ensures the user enters a valid file path and filename,
# and can optionally check that a file with that name exists

# inputPassword() Is like the built-in input(), but displays * characters as the user types
# so that passwords, or other sensitive information, aren’t displayed on the screen

# Ejemplo de uso
import pyinputplus

# Pedimos que entre un número... automáticamente, si no es válido, le seguirá repreguntando...
numero = pyinputplus.inputNum('Por favor introducn un número: ')

print('EL número que introdujiste fue', numero)

# Algunas opciones que podemos pasar como parámetros para validar números con
# inputNum, inputInt e inputFloat serían -----> min, max, greateThan, lessThan
# Ejemplo para pedir un número entero, y que sea menor que 10, validando todo_ sería...
numero = pyinputplus.inputInt('Introudce un entero menor que 10: ', lessThan=10)
print(numero)
# Aquí es correcto cualquier cosa <10 , por ejemplo, -14

# Pero lo anterior valida como correcto el menos 3... si queremos que sea del 1 al 10 sería...
numero = pyinputplus.inputInt('Introduce un entero del 1 al 10: ', min=1, max=10)
print(numero)


# Si queremos habilitar que no entren nada, sino simplemente apreten return, lo podemos hacer con blank...
numero = pyinputplus.inputInt('Introduce un entero del 1 al 10: (o return)', min=1, max=10, blank=True)
print(numero)

# También podemos usar limit= o timeout para limitar las veces o el itempo que queremos que pueden meter datos
# si se pasa de esos valores se generará una excepción RetryLimitException o TimeoutException respectivamente...
response = pyinputplus.inputNum(prompt='Tienes como mucho dos intentos: ', limit=2)


# Si queremos que no se genere una excpeción sino que, pasado el tiempo o los intentos, coja algún valor por
# defecto, podemos utilizar default, el valor del default se activa cuando sobrepasamos los límietes....



