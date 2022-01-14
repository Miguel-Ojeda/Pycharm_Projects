# Caret sirve para indicar que sólo habrá match si la cadena empieza con esa expresión!!
# Dólar es lo mismo , pero indicar que la cadena debe terminar con esa expresión!!

import re

beginsWithHello = re.compile(r'^Hello \d\d\d')

mo = beginsWithHello.search('Hello 1234567')
print(mo.group())


mo = beginsWithHello.search('HHello 1234567')
if mo:
    print(mo.group())
# No hay coincidencia!! porque aunque el patrón está, NO ESTÄ AL PRINCIPIO!!!

ends_with_three_digits_pattern= re.compile(r'\d\d\d$')
mo = ends_with_three_digits_pattern.search('Your number is 423')
if mo:
    print('1 ---> ', mo.group())

# Aquí no lo encontrará, pq está al final...
mo = ends_with_three_digits_pattern.search('Your number is 423 ')
if mo:
    print('2 ---> ', mo.group())

# Expresiones que empiezan y acaban con 3 dígitos... (utiliza tamb. el carácter punto que veremos en 10...)
pattern = re.compile(r'^\d\d\d.*\d\d\d$')
mo = pattern.search('123 Your number is 423')
if mo:
    print('11 ---> ', mo.group())

# Aquí tb lo encuentra!!!
mo = pattern.search('123423')
if mo:
    print('22 ---> ', mo.group())

    