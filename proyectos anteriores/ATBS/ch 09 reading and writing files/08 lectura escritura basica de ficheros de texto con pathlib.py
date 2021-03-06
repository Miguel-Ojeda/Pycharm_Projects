'''El módulo pathlib incluye cosas muy básicas para actuar con ficheros de texto...
    incluye los métodos .write_text() y .read_text()
    pero es algo básico, mucho menos potente que lo clásico con el open()

    El método write_text lo que hace es crear (y sobreescribir) un fichero con el contenido
    del string que le pasamos...
    El método read_text recoge en un string todo el contenido del fichero...
'''

from pathlib import Path
path = Path('spam.txt')
path.write_text('Hola voy a escribir este texto al fichero al que apunta el objeto path\nAquí la línea final')

# Para leer es similar... lee todo_ de golpe, a lo bestia...
path = Path('01 objetos path, usar forward_slash y operador slash.py')
# Vamos por ejemplo a copiar el contenido de esto al portapepales...
import pyperclip
pyperclip.copy(path.read_text())


# Observaciones: todo_ esto, utilizando pathlib, es muy rudimentario y sencillo
# No hay que abrir ni cerrar si ficheros... se hace todo_ de golpe, en una sola operación...
# Para algo más potente utilziar lo clásico de open, etc...