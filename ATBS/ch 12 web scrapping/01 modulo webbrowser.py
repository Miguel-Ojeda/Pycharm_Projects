#! python
# Simplemente es un módulo que nos permite automatizar la apertura de una dirección en el navegador...
# Haremos como proyecto un programa que, pasada una dirección , abre una página en el navegador
# que muestra dicha dirección en google maps...
# si no pasamos la dirección como argumento, pues copia como dirección lo que haya en el portapapeles...

import webbrowser
import pyperclip
import sys

# Antes de nada hacer pruebas a ver con google maps, a ver como se ve en la barra de direcciones http
# según la dirección que buscamos...
# Parece que la web apropiada para mostrar una dirección sería similar a esto...
# Suponer que queremos buscar calle granadera canaria...
# https://www.google.com/maps/place/Calle+granadera+canaria/
# o sea, después de place va la cadena con la dirección, donde cada palabra está separada por un +
# Análogamente parece que si buscamos para la dirección  870 Valencia St, San Francisco, CA
# la dirección sería...
# https://www.google.com/maps/place/870+Valencia+St+San+Francisco+CA/

# Pues hagamos esto!!!
# Si escribimos algo además del nombre del programa para invocarlo... ese algo es la dirección!!
if len(sys.argv) > 1:
    direccion = ' '.join(sys.argv[1:])
else:
    direccion = pyperclip.paste()

direccion_http = 'https://www.google.com/maps/place/' + direccion


webbrowser.open(direccion_http)
webbrowser.open('www.marca.com')
webbrowser.open('www.amazon.com')


