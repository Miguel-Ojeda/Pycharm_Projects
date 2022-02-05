# python
'''Es una utilidad que, al texto del portapapeles (que se supone que son varias líneas...
les añade una viñeta para así crear una lista tipo bullet...'''
import pyperclip

CHAR_BULLET = '∙'  # Operador de viñeta u-2219
text = pyperclip.paste()

# Ahora separamos el contenido en una lista de línea...
lineas = text.split('\n')
nuevas_lineas = []
bullet = CHAR_BULLET
for linea in lineas:
    nuevas_lineas.append(CHAR_BULLET + ' ' + linea)

textito = '\n'.join(nuevas_lineas)

pyperclip.copy(textito)