#! python
''' El programa recoge una palabra clave de entrada (agree, busy, upsell, despedida...
y copia al portapapeles el texto asociado a la misma
De esta forma implementamos de manera sencilla un mini portapapeles'''

# Hay que añadirle la siguiente funcionalidad...
# 1. The command line argument for the keyword is checked.
# 2. If the argument is save, then the clipboard contents are saved to # the keyword.
# 3. If the argument is list, then all the keywords are copied to the clipboard.
# 4. Otherwise, the text for the keyword is copied to the clipboard.


# El programa quedaría...
instrucciones = r'''
    Uso del programa:
    1) py mcb save <keyword>
        Asocia a la palabra clave un nuevo mensaje con el contenido del portapapeles.

    2) py mcb del <keyword>
        Borra el mensaje asociado a la clave de la base de mensajes.

    3) py mcb <keyword> - Copia al portapapeles el mensaje asociado.

    4) py mcb list - Nos muestra todas las claves que podemos usar en nuestro programa.
    '''

# Aquí pondríamos un diccionario con las keys y el mensaje respectivo que queremos copiar al portapepales...
import sys
# para poder recoger los parámetros con los que invocamos el programa!!!
import pyperclip
import shelve

# para crear / acceder / modificar a nuestro diccionario de mensajes...

# Si no existe el diccionario/shelf inicial con los mensajes... pues a crearlo... con algunos valores básicos
# Esto simplemente es una clave que creo al crear el diccionario... para comprobar que ya existe el shelf
# No sé si habrá un método más sencillo....

CLAVE_CREACION = 'XYZ2345'

with shelve.open('mcb') as TEXT:
    if CLAVE_CREACION in TEXT:
        # Ya existe el shelf....
        print('Encontrada base de datos con mensajes...')
    else:
        print('Creando nueva base de datos con mensajes iniciales...')
        # Creamos nuestro shelf con algunos mensajes iniciales, para no partir de 0
        TEXT[CLAVE_CREACION] = True  # Simplemente esto es para comprobar si existe ya el shelf
        TEXT['agree'] = 'Sí, estoy completamente de acuerdo con lo que comentas, me parece bien.'
        TEXT['busy'] = 'Lo siento, estoy liado. ¿Podemos quedar más tarde esta semana o la que viene?'
        TEXT['upsell'] = 'Would you consider making this a monthly donation?'
        TEXT['firma'] = 'Saludos cordiales, atentamente, Miguel'

    # The first item in the sys.argv list should always be a string containing the program’s filename
    # and the second item should be the first command line argument , etc...

    if len(sys.argv) == 3:
        # Estamos en la opción "mcb comando clave", opciones 1) o 2) de uso...
        comando, clave = sys.argv[1:]
        if comando == 'save':
            # Añadimos un nuevo mensaje a nuestra base....
            TEXT[clave] = pyperclip.paste()
            print(f'Guardado el nuevo mensaje asociada a la clave "{clave}".')
        elif comando == 'del':
            if clave in TEXT:
                del TEXT[clave]
                print(f'Borrado el mensaje asociado a la clave "{clave}".')
            else:
                print(f'No puedo borrar el mensaje asociado, porque no existe la clave "{clave}".')
        else:
            print('Comando incorrecto')
            print(instrucciones)
        # Pausa y salimos
        input('Hasta la próxima...')
        sys.exit()

    elif len(sys.argv) == 2:
        # Estamos en "mcb comando"...
        # Tenemos dos opciones... "mcb list" ó "mcb keyword"
        argumento = sys.argv[1]
        if argumento == 'list':
            # quiere saber qué claves podemos usar...
            print('Las claves disponibles para usar son las siguientes:')
            for key in TEXT:
                if key == CLAVE_CREACION:
                    continue
                else:
                    print(f'Clave: {key}')
        elif argumento in TEXT:
            # quiere copiar el contenido de la clave al portapapeles...
            print('Copiando el mensaje apropiado al portapepales...')
            pyperclip.copy(TEXT[argumento])
        else:
            # Uff, la clave no está....
            print('La clave utilizada es incorrecta')
            print('Las claves disponibles para usar son las siguientes:')
            for key in TEXT:
                if key == CLAVE_CREACION:
                    continue
                else:
                    print(f'Clave: {key}')
        input('Hasta la próxima...')
        sys.exit()
    else:
        # número de argumentos incorrectos...
        print('Uso incorrecto del programa')
        print(instrucciones)
        input('Hasta la próxima...')
        sys.exit()

