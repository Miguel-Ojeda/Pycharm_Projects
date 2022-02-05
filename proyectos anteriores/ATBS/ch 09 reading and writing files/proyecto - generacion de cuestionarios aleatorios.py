# El objetivo es crear 35 cuestionarios (ficheros de texto) aleatorios para una clase de geografía
# con sus 35 ficheros que sirvan de clave de corrección!!  (todo_ esto para que no se puedan copiar en el examen)
# Preguntaremos sobre las capitales de los estados de EEUU
# cada cuestionario estará formado por 50 preguntas al azar... y tendrá 4 respuestas (una sola válida)

# Deberemos pues...
# Crear un gran diccionario con todos los estados y sus capitales...
# Crear cada uno de los cuestionarios y sus clave (open, write con ficheros, el close lo haremos automático con with...
# Usar random shuffle para que todo_ sea aleatorio...
import random
import pprint   # Solo lo utilicé para pruebas....
from pathlib import Path
LETRA = ['A', 'B', 'C', 'D']
NUMERO_PREGUNTAS = 50
NUMERO_CUESTIONARIOS = 35
SUBDIRECTORIO = 'cuestionarios'
PREFIJO_CUESTIONARIO = 'cuestionario'

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
    # Desordenamos los estados para de esa forma, elegimos las NUMERO_PREGUNTAS estados para preguntar
    random.shuffle(estados)
    name, extension = file_name.split('.')
    key_name = name + '_key' + '.' + extension
    with open(file_name, 'w') as cuestionario, open(key_name, 'w') as clave:
        cuestionario.write(f'Cuestionario "{file_name}" sobre las capitales de US:\n')
        cuestionario.write('Nombre y apellidos:\n\n')
        cuestionario.write('ELIGE LA CAPITAL CORRECTA DE CADA ESTADO\n\n')
        clave.write(f'Solucionario del cuestionario "{file_name}" sobre las capitales\n\n')
        # preguntamos por capitales de los primeros NUMERO_PREGUNTAS estados al azar...
        for n, estado in enumerate(estados[:NUMERO_PREGUNTAS]):
            capital_correcta = capitals[estado]
            # capitales_erroneas = capitales.copy()
            # capitales_erroneas.remove(capital_correcta)
            capitales_erroneas = [capital for capital in capitales if capital != capital_correcta]
            # Opción 1....
            # random.shuffle(capitales_erroneas)
            # opciones = capitales_erroneas[:3] + [capital_correcta]
            # Opción 2 para ver las opciones es más sendilla pq me ahorro el shuffle de todo_...
            # simplemente extraigo 3 samples de las capitales erróneas y le añado tb. la capital correcta
            opciones = random.sample(capitales_erroneas, 3) + [capital_correcta]
            random.shuffle(opciones)
            indice_correcto = opciones.index(capital_correcta)
            cuestionario.write(f'{n+1}) La capital de {estado} es:\n\n')
            # clave.write(f'{n+1}) La capital de {estado} es: {LETRA[indice_correcto]}\n')
            clave.write(f'{n+1:02}) {LETRA[indice_correcto]}\n')
            cuestionario.write(f'\tA: {opciones[0].ljust(20)}\n'
                               f'\tB: {opciones[1].ljust(20)}\n'
                               f'\tC: {opciones[2].ljust(20)}\n'
                               f'\tD: {opciones[3].ljust(20)}\n\n'
                               )

# Empezamos el programa creando el directorio donde pondremos los cuestionarios....
path = Path.cwd() / SUBDIRECTORIO
path.mkdir(exist_ok=True)
# Es más sencillo esto...
# con la opción exist_ok True lo que hace es que no canta error si ya esiste el directorio
# y no haría nada si ya existe!!!
# la otra opción es comprobar si existe, y si no crearlo
# if not path.exists():
#     path.mkdir()

for i in range(NUMERO_CUESTIONARIOS):
    genera_cuestionario_al_azar(f'{SUBDIRECTORIO}/{PREFIJO_CUESTIONARIO}_{i+1:2}.txt')


path = Path.cwd() / SUBDIRECTORIO






# i = 1
# genera_cuestionario_al_azar(f'{SUBDIRECTORIO}/{PREFIJO_CUESTIONARIO}_{i:02}.txt')
# pprint.pprint(estados)
# pprint.pprint(capitales)
# estado = 'Kentucky'
# capital_correcta = capitals[estado]
# capitales_erroneas = [capital for capital in capitales if capital != capital_correcta]
# print('Las capitales erróneas serían:')
# pprint.pprint(sorted(capitales_erroneas))
# print('El estado de', estado, 'tiene como capital', capital_correcta)
# capitales_erroneas = capitales.copy()
# print('Las capitales erróneas serían:')
# pprint.pprint(sorted(capitales_erroneas))
# capitales_erroneas.remove(capital_correcta)
# print('Las capitales erróneas serían:')
# pprint.pprint(sorted(capitales_erroneas))

