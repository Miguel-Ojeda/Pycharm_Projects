# Este módulo se basa en urllib (y otros) pero es muchísimo más sencillo de manejar...
# https://docs.python-requests.org/en/latest/#

# FUnciones... entre otras...
# get() nos dará un objeto Response...
# EL objeto Response tiene un status_code que nos informa de cómo fue el request...
# también tienen un atributo text con el contenido del response...
# También podemos invocar el método raise_for_status() que, sí algo fue mal, genera una excepción
# también tiene un método iter_content() que nos permite ir recuperando, poco a poco, el contenido que sea del request

# Ejemplos...
import requests

# SOlicitamos un texto de Romeo y Julieta que está en la web del libro...

response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# Cómo fue???
if response.status_code == requests.codes.ok:
    # Todo_ fue bien.... code 200
    # Esto significa que el objeto Respone tendrá toda la respuesta del servidor...
    # estará en el atributo text...
    print(f'La longitud del objeto solicitado es de {len(response.text)} bytes')
    print(f'Los primeros 1000 bytes son...')
    print(response.text[:1000])
else:
    print('Ha habido un error, no se ha podido recuperar la solicitud')

# Hemos visto como solicitar un objeto, ver el tamaño de su respuesta, y mostrarlo
# y comprobar antes de nada, si todo ha ido bien...

# Podemos comprobar tb. si todo_ ha ido bien, utilizando el método raise_for_status....
# Si todo_ ha ido bien, pues no hace nada... pero si ha ido mal el request, pues lo que
# pasa es que se genera una excepción...
# Veamos un ejemplo cuando intentamos recuperar algo que no existe...
response = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# Si ahora hacemos response.raiste_for_status se generará una excepción....
# para que no termine el programa, vamos a ponerlo en un try...
try:
    response.raise_for_status()
    # Si ha ido bien aquí haríamos las operaciones que quisiéramos con el Response object...
except requests.exceptions.HTTPError as error:
# O también simplemente  except Exception as error:
    print('Ufff.... vaya, parece que la hemos liado...')

# Descarga de ficheros al disco duro... para descargar cosas muy grandes, lo hacemos con
# el método iter_count(), al que le pasamos la cantidad de bytes que queremos leer cada vez
# hasta terminar... una buena cifra es 100_000...
# Lo que hace esto es que del .text va leyendo podo a poco, en esas cantidades... y lo vamos escribiendo
# a la vez al fichero....
# IMportante, al ir escribiendo los datos de los chunks que recuperamos, lógicamente, lo haremos
# abriendo un fichero, pero NO EN MODO 'w', sino en modo 'wb' (binary data) para mantener el Unicode Encoding!!!
# También tenemos la opción de utilziar un iterador por líneas...
# Ejemplo de descarga...
response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
try:
    response.raise_for_status()
    # Si estamos aquí, es que todo_ ha ido bien... o sea, tenemos ya TODO_ EL CONTENIDO SOLICITADO
    # Ahora, lo vamos a ir leyendo (ya está en nuestro ordenador, en response) con un iterador
    # e ir copiando a un fichero del disco duro!!!
    with open('files/Romeo_y_julieta.txt', 'wb') as fichero:
        # chunk = response.iter_lines()
        # Usaremos iterador más rápido... leeremos y escribiremos al fichero de 100_000 en 100_000
        for chunk in response.iter_content(100_000):
            print('escribiendo chunk --->')
            fichero.write(chunk)

except requests.exceptions.HTTPError as error:
    # O también simplemente  except Exception as error:
    print('Ufff.... vaya, parece que la hemos liado...')


# Otro ejemplo...
# La página del marca...
response = requests.get('https://www.marca.com')
try:
    response.raise_for_status()
    print('Fue bien el raise!!')
    with open('files/marca.html', 'wb') as fichero:
        for chunk in response.iter_content(100_000):
            fichero.write(chunk)
        # OJo... si hacemos simplemente fichero.write(response.txt) da error pq es demasiado grande!!!
        print('Copiando el marca...')
except Exception:
    print('Uff.... algo fue mal leyendo el marca...')
