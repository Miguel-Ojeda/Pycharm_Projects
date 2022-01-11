# \d es un dígito
# {n} obliga que el patrón anterior se repita n veces para ser reconocido...
# podemos crear grupos con ().... luego podremos usar el group con el match objetc
# para pedirle lo que coincida con algún grupo
# si al método group no le pasamos nada (o le pasamos 0) nos mostrará el match de toda la expresión
# # pero si le pasamos algún número, nos mostrará match simplemente de ese grupo

import re

# seguimos con el ejemplo de los EEUU
# En vez de hacer el patrón r_string = r'\d{3}-\d{3}-\d{4}' (que no tiene grupos)
# o r_string = r'\d\d\d-\d\d\d-\d\d\d\d'  que no tieen tampoco ningún grupo...
# podríamos, si nos hiciera falta, crear un patrón con grupos...
patron = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# equivalente a re.compile(r'(\d{3})-(\d{3}-\d{4}')
message = 'Call me at 415-555-111 tomorrow. 415-555-9999 is my office.'
match_object = patron.search(message)

if match_object:

    print(match_object.group(0))
    # o simplemente match_object.group()
    # Significa que buscamos el match de toda la expresión completa!!!
    # >>> 415-555-9999

    print(match_object.group(1))
    # estamos buscando el match del primer grupo
    # >>> 415

    print(match_object.group(2))
    # buscamos el match del segundo grupo
    # >>> 555-9999

    # si queremos una tupla con todos los grupos reconocidos....
    # usar simplemente el método groups()
    area_code, main_number = match_object.groups()
    print(f'Código de área: {area_code}, número: {main_number}')

# Por supuesto, si queremos buscar paréntesis en la expresión
# habrá que poner antes el backslah
# Por ejemplo si queremos buscar números EEUU de esta forma alternativa
# (415) 555-4242
# La r_string de la expresión regular sería (utilizando por ejemplo dos grupos
# uno para área y otro para número principal....

r_string2 = r'(\(\d{3}\)) (\d{3}-\d{4})'
pattern_object_2 = re.compile(r_string2)
match_object2 = pattern_object_2.search('My phone number is (415) 555-4242.')
if match_object2:
    area, number = match_object2.groups()
    print(f'Código de área: {area}, número: {number}')

# Otros caracteres con significado especial, a los que debemos anteponer \ si queremos buscarlos...
# ----> .  ^  $  *  +  ?  {  }  [  ]  \  |  (  )