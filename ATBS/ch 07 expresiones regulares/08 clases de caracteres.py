# Hay varias clases de caracteres definidas que
# podemos usar para construir nuestras expresiones regulares...
# \d representa cualquier dígito (suelto... una sola cifra)
# \d realmente sería lo mismo que (0|1|2|3|4|5|6|7|8|9)
# \D cualquier caracter que NO SEA un dígito (lo contrario que \d)
# \w cualquier letra, dígito, o underscore (o sea, representa caracteres que podríamos usar en 'palabras')
# \W cualquier caracter que no sea letra, dígito o underscore (lo contrario de \w)
# \s cualquier carácter espacio, nueva línea o tabulador
# \S lo contrario de \s

# Obs... no existe ninguna clase para carácter alfabético
# ... aunque es fácil crear nuestras propias clases

# Ejemplo si queremos buscar patrones que sean un número entero, seguido de un espacio
# y luego una palabra.... como por ejemplo 124 coches   225 motos 346 cubos...
# sería así...
import re
r_string = re.compile(r'\d+ \w+')
# También podríamos haber puesto r_string = re.compile(r'\d+\s\w+')

lista_resultados = r_string.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids,'
                                    '7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(lista_resultados)
# ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans',
# '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']

# Realamente sería, en lugar de \w+ algo que sea cualquier_caracter+
# porque como está ahora tb sería válido 6 geese126_1
# Lo veremos luego como hacerlo luego...

# Crear nuestras clases de caracteres... [......]
# Para definir las clases simplemente, entre corchetes pondremo
# uno a uno (o con rangos) todos los caracteres que forman la clase...
# MUY IMPORTANTE: dentro de la definición ya los caracteres no tienen
# significados especiales, o sea si ponemos [12345?] significa que
# la clase está formada por los 6 caracteres 1, 2, 3, 4, 5, y ? (el ? y los demás
# caracteres especiales no tieenn valor especial dentro de la definición de la clase)

# Ejemplo 1: [aeiouAEIOU] es una clase de caracteres que encuentra 1 vocal
# Importante, estas clases representan 1 solo carácter de los especificados ....
# Entonces, para buscar donde ocurren dos vocales seguidas podemos hacer...
r_string = r'[aeiouAEIOU]{2}'
patron = re.compile(r_string)
lista_resultados = patron.findall('Hola, llevé mi peonza y me dijeron que no tenian piezas para arreglarla')
print(lista_resultados)  # --> ['eo', 'ue', 'ia', 'ie']

# Podemos especificar rangos de letras o digitos utilizando el hyphen...
# Así, cualquier letra sería simplemente [a-zA-Z]
# Así, el ejemplo previo que vimos de encontrar expresiones del tipo.... 24 calles  85 perros
# quedaría...
r_string = r'\d+ [a-zA-Z]+'
r_string = re.compile(r_string)
lista_resultados = r_string.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids,'
                                    '7 swans, 6 geese1_343, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(lista_resultados)
# Clase contraria!!! usando el caret ^
# Si, nada más poner [ ponemos el carácter ^ significará que queremos coger la clase contraria
# ejemplo:
consonantes = r'[^aeiouAEIOU]'
# estamos diciendo que cogemos todos los caracteres que no sean vocal!!!
# quizás no esté bien porque estaríamos cogiendo números, etc...
# Para mejorarlo también vamos a quitar espacios
consonantes = r'[^aeiouAEIOU ]'
patron_consonantes = re.compile(consonantes)
lista_resultados = patron_consonantes.findall('RoboCop eats baby food. BABY FOOD.')
print(lista_resultados)




