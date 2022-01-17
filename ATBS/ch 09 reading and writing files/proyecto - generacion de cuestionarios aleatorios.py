# El objetivo es crear 35 cuestionarios (ficheros de texto) aleatorios para una clase de geografía
# con sus 35 ficheros que sirvan de clave de corrección!!  (todo_ esto para que no se puedan copiar en el examen)
# Preguntaremos sobre las capitales de los estados de EEUU
# cada cuestionario estará formado por 50 preguntas al azar... y tendrá 4 respuestas (una sola válida)

# Deberemos pues...
# Crear un gran diccionario con todos los estados y sus capitales...
# Crear cada uno de los cuestionarios y sus clave (open, write con ficheros, el close lo haremos automático con with...
# Usar random shuffle para que todo_ sea aleatorio...

import random
import pprint

NUMERO_PREGUNTAS = 35

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery',
              'Alaska': 'Juneau',
              'Arizona': 'Phoenix',
              'Arkansas': 'Little Rock',
              'California': 'Sacramento',
              'Colorado': 'Denver',
              'Connecticut': 'Hartford',
              'Delaware': 'Dover',
              'Florida': 'Tallahassee',
              'Georgia': 'Atlanta',
              'Hawaii': 'Honolulu',
              'Idaho': 'Boise',
              'Illinois': 'Springfield',
              'Indiana': 'Indianapolis',
              'Iowa': 'Des Moines',
              'Kansas': 'Topeka',
              'Kentucky': 'Frankfort',
              'Louisiana': 'Baton Rouge',
              'Maine': 'Augusta',
              'Maryland': 'Annapolis',
              'Massachusetts': 'Boston',
              'Michigan': 'Lansing',
              'Minnesota': 'Saint Paul',
              'Mississippi': 'Jackson',
              'Missouri': 'Jefferson City',
              'Montana': 'Helena',
              'Nebraska': 'Lincoln',
              'Nevada': 'Carson City',
              'New Hampshire': 'Concord',
              'New Jersey': 'Trenton',
              'New Mexico': 'Santa Fe',
              'New York': 'Albany',
              'North Carolina': 'Raleigh',
              'North Dakota': 'Bismarck',
              'Ohio': 'Columbus',
              'Oklahoma': 'Oklahoma City',
              'Oregon': 'Salem',
              'Pennsylvania': 'Harrisburg',
              'Rhode Island': 'Providence',
              'South Carolina': 'Columbia',
              'South Dakota': 'Pierre',
              'Tennessee': 'Nashville',
              'Texas': 'Austin',
              'Utah': 'Salt Lake City',
              'Vermont': 'Montpelier',
              'Virginia': 'Richmond',
              'Washington': 'Olympia',
              'West Virginia': 'Charleston',
              'Wisconsin': 'Madison',
              'Wyoming': 'Cheyenne'}

# las usaremos para hacer shuffle y que todo_ sea aleatorio
estados = list(capitals.keys())
capitales = list(capitals.values())


def genera_cuestionario_al_azar(file_name):
    # Desordenamos los estados para de esa forma, elegimos las 35 estados para preguntar
    random.shuffle(estados)
    for estado in estados[:35]   # preguntamos por capitales de los primeros 35 estados al azar...
        capital_correcta = capitals[estado]
        # capitales_erroneas = capitales.copy()
        # capitales_erroneas.remove(capital_correcta)
        capitales_erroneas = [capital for capital in capitales if capital != capital_correcta]
        random.shuffle(capitales_erroneas)





pprint.pprint(estados)
pprint.pprint(capitales)


estado = 'Kentucky'
capital_correcta = capitals[estado]
capitales_erroneas = [capital for capital in capitales if capital != capital_correcta]
print('Las capitales erróneas serían:')
pprint.pprint(sorted(capitales_erroneas))

# print('El estado de', estado, 'tiene como capital', capital_correcta)
# capitales_erroneas = capitales.copy()
#
# print('Las capitales erróneas serían:')
# pprint.pprint(sorted(capitales_erroneas))
# capitales_erroneas.remove(capital_correcta)
#
# print('Las capitales erróneas serían:')
# pprint.pprint(sorted(capitales_erroneas))

