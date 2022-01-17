'''El módulo prettyprint incluye la función pformat que lo que hace es nos devuelve una string
del objeto (lista o diccionario)'''

import pprint
import time   # lo usaremos para guardar en un fichero la fecha-hora...

# Pretty Print tuplas listas y diccionarios, recursivamente...
# veamos algún ejemplo

lista = [1, 2, [3, 4, 5], 'seis', (7, 8)]
tupla = (1, 2, 3, 'hola', 'cinco')
diccionario = { 'profesion': 'fontanero', 'comida': ['spam', 'eggs', 'bacon']}

pprint.pprint(lista)  # [1, 2, [3, 4, 5], 'seis', (7, 8)]
pprint.pprint(tupla)  # (1, 2, 3, 'hola', 'cinco')
pprint.pprint(diccionario)  # {'comida': ['spam', 'eggs', 'bacon'], 'profesion': 'fontanero'}

# Lo vueno de pprint es que lo que imprime, realmente, es código Python válido!!
# Y podemos, en vez de imprimir, tener una cadena con ese contenido... con la función pformat !!!
# Con lo que podremos, si nos interesara... crear código Python que simplemente
# guardara esas variables... veamoslo....

codigo_lista = 'lista = ' + pprint.pformat(lista)
# esta cadena vale  --> lista = [1, 2, [3, 4, 5], 'seis', (7, 8)]
codigo_tupla = 'tupla = ' + pprint.pformat(tupla)
# esta cadena valdría --> tupla = (1, 2, 3, 'hola', 'cinco')
codigo_diccionario = 'diccionario = ' + pprint.pformat(diccionario)
# esta cadena valdría --> diccionario = {'comida': ['spam', 'eggs', 'bacon'], 'profesion': 'fontanero'}

# Como vemos, las cadenas contienen código Python, con el que podríamos volver a regenerar las variables!!!
# Guardemos todo_ esto en un script!!!
# Cuidado, al final de cada línea nos queda añadir nueva línea, pq si no estaría todo seguido
with open('crea_variables.py', 'w') as file:
    local_time = time.localtime()
    tiempo_str = time.asctime(local_time)
    file.write(f'# {tiempo_str} Script creado con pprint.format para guardar algunas variables\n')
    file.write(codigo_lista)
    file.write('\n')   # Para pasar a otra línea, claro!!
    file.write(codigo_tupla)
    file.write('\n')   # Para pasar a otra línea, claro!!
    file.write(codigo_diccionario)

# Ahora, desde cualquier programa, este mismo, podríamos recuperar estas variables!!!
import crea_variables

print(crea_variables.lista)
print(crea_variables.tupla)
print(crea_variables.diccionario)

# Conclusión: esto es otro truco más usando pprint

# Es mucho más sencillo utilizar las estanterías del módulo shelve
# pero la ventaja de este método es que lo veríamos fácilmente y podríamos
# modificar las variables si fuera necesario con un editor de texto...

# Además, hay cosas que no pueden ser escritas con pretty print
# a un fichero de texto, como File objects por ejemplo....


