#! python
# A multi-clipboard program
'''El programa recoge una palabra clave de entrada (agree, busy, upsell, despedida...
y copia al portapapeles el texto asociado a la misma
De esta forma implementamos de manera sencilla un mini portapapeles'''

# Aquí pondríamos un diccionario con las keys y el mensaje respectivo que queremos copiar al portapepales...
import sys
import pyperclip

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?""",
        'despedida': '''Sin más, se despide de usted, atentamente, Miguel''',
        }

# Cómo hacer para recoger el parámetro pasado al script???
# The first item in the sys.argv list should always be a string containing the program’s filename
# and the second item should be the first command line argument.

# Primero comprobar que estamos invocando el programa con 1 argumento adicional... si no pues salimos...

if len(sys.argv) != 2:
        print('Uso incorrecto del script.\nDebes suministrar 1 argumento para saber qué texto copiar al portapapeles')
        print('Los argumentos válidos son...')
        # Recordar que TEXT es lo mismo que TEXT.keys()
        for index, key in enumerate(TEXT):
                print(index, ':', key)
        sys.exit()

argumento = sys.argv[1]
if argumento not in TEXT.keys():
        print('Argumento no válido.\n Los argumentos válidos son...')
        for index, key in enumerate(TEXT):
                print(index, ':', key)
        sys.exit()

# SI llegamos aquí es que todo_ va bien... tenemos en clave un argumento ok...
# Simplemente copiar al portapapeles y salir...
pyperclip.copy(TEXT[argumento])

