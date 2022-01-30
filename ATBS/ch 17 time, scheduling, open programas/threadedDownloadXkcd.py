'''El objetivo es hacer el programa que descarga los comics, pero que sea multihilo!!!
Para aprovechar mejor el ancho de banda... realmente si sólo tenemos un hilo estamos desperdiciando
porque se está a la espera mucho tiempo, simplemente para establecer la conexión!!!

Podríamos utilizar varios hilos... y que cada hilo se descargara un bloque de comics...
para ello tendríamos que definir una función para que se ejecutara en el hilo
que se descargara un conjunto de comics... desde uno de inicio hasta uno de fin...


ESTA PENDIENTE DE HACER... ya vi como se hacía...

'''

import bs4
import requests
import sys
from pathlib import Path
import threading


def get_xkcd_comic_previous(url_actual):
    url_base = 'https://xkcd.com'
    request = requests.get(url_actual)
    request.raise_for_status()
    soup = bs4.BeautifulSoup(request.text, 'lxml')
    # EL comic estará en el único bloque div con id = comic....
    div_comic = soup.select('div[id="comic"]')[0]
    url_imagen = 'https:' + div_comic.img['src']

    # el comic previo estará en un elemento a cuyo atributo rel es prev
    url_comic_previo  = url_base + soup.select('a[rel="prev"]')[0]['href']

    return url_imagen, url_comic_previo


url_base = 'https://xkcd.com'
contador = 0
path_comics = Path.cwd() / 'xkcd_comics'
path_comics.mkdir(exist_ok=True)


while not url_base.endswith('#'):   # O sea, si no es el anterior al primero, que no hay nada...
    url_imagen, url_comic_previo = get_xkcd_comic_previous(url_base)
    request = requests.get(url_imagen)
    request.raise_for_status()
    name_comic = path_comics / url_imagen.split('/')[-1]
    print(f'Grabando el comic {url_imagen}')
    with open(name_comic, 'wb') as comic:
        for chunk in request.iter_content(100_000):
            comic.write(chunk)
    url_base = url_comic_previo
    contador += 1
