'''
Open a log file from a Unix/Linux system—for example, one from the Apache server.
For each response code (i.e., three-digit code indicating the HTTP request’s success or failure),
store a list of IP addresses that generated that code
'''

# Lo haré pero metiendo en vez de en una lista en un set...
# para que no se repitan y sea más rápido acceder...

# Descargué el fichero de muestra del github del autor:
# https://github.com/reuven/python-workout
# es el fichero mini-access-log.txt que utilizaré para el ejercicio...

'''
Se puede hacer con expresiones regulares... pero lo haremos en plan sencillo...
----> Vemos que la ip es justo lo que hay antes del primer espacio de cada línea...
----> Vemos que el código devuelto es lo que aparece justo después de "<espacio>
'''

from collections import defaultdict
DATA = defaultdict(set)
# creamos el diccionario con los datos,
# para clave no existente cuando haga falta se iniciará con el conjunto vacío

with open('files/mini-access-log.txt') as log:
    for line in log:
        espacio = line.find(' ')
        comillas_esp = line.find('" ')
        ip = line[:espacio]
        codigo = line[(comillas_esp + 2): (comillas_esp + 5)]
        # print(f'IP: {ip}  /  Código: {codigo}')
        # Añadimos el conjunto al set... si ya existe pues no tiene efecto, claro
        DATA[codigo].add(ip)

        '''
        ¡¡ La actualización del defaultdict es una línea de código...!!
        Si fuera un dict normal... el código sería...
        if not codigo in DATA:
            DATA[codigo] = {}
        DATA[codigo].add(ip)
        '''

# Ahora mostramos los resultados...
for codigo, set in DATA.items():
    print(f'\nPara el código {codigo}, las ips grabadas han sido, sin repetir...\n')
    for ip in set:
        print('\t--> ', ip)









