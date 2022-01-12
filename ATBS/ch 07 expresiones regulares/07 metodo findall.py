# Cuando tenemos un objeto patrón podemos usar para buscar dos métodos:
# El método search() nos devuleve un objeto match con la primera ocurrencia encontrada
# Es lo que hemos visto hasta ahora...

import re
r_string = r'Batman|Tina Fey'
pattern_object = re.compile(r_string)
match_oject = pattern_object.search('Hola somos Batman y Tina Fey')
if match_oject:
    print(match_oject.group())
    # >>> 'Batman'

# Pero realmente el patrón también debería reconocer a 'Tina Fey'
# lo que pasa es que el método search solo nos retorna el primer patrón reconocido

# Si queremos obtener TODOS LOS PATRONES RECONOCIDOS, tenemos que
# utilizar el método findall()
# El método findall NO DEVULEVE UN OBJETO MATCH...
# El método findall devuelve...
# a Si no utilizamos grupos en la expresión....
#   devuelve una lista, con cada ítem una de las cadenas reconocidas...
# b Si utilizamos grupos en la expresión... devuelve una lista de tuplas
#   Each tuple represents a found match, and its items are the
#   matched strings for each group in the regex.

# Ejemplo del método findall cuando NO EXISTEN GRUPOS
# Devuelve una lista de cadenas, con todos los match...
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
lista_resultados = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(lista_resultados)
# >>> ['415-555-9999', '212-555-0000']

# Ejemplo del método findall cuando NO EXISTEN GRUPOS
# Devuelve una lista de tuplas, donde las distintos items
# de la tupla corresponden a los distintos grupos reconocidos..
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
lista_resultados = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(lista_resultados)
# >>> [('415', '555', '9999'), ('212', '555', '0000')

# Observar que con el método findall() no es necesario mirar
# si el objeto devuelto es None...
# ya que, aunque no se encontrara nada, siempre tendremos
# la lista vacía []