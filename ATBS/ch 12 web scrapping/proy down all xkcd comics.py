'''
Objetivo: descargarse rápido todos los comics de
https://xkcd.com/
Es fácil, pq en cada página simplemente tenemos que buscar... el comic
tiene como padre un tag div que incluye un atributo id con valor comic

<div id="comic">
<img src="//imgs.xkcd.com/comics/alien_observers.png" title="ALERT: Human 910-25J-1Q38 has created a Youtube channel. Increase erratic jerkiness of flying by 30% until safely out of range." alt="Alien Observers" srcset="//imgs.xkcd.com/comics/alien_observers_2x.png 2x" style="image-orientation:none">
</div>
Tag <img src="//imgs.xkcd.com/comics/alien_observers.png" nos va a decir la imagen del comic de esa página
<a rel="prev" href="/2571/" accesskey="p">&lt; Prev</a> nos da el número del comic anterior

En este caso significaria que el comic estaría en https://xkcd.com/2571/

Además, en el primer comic está que el previo es https://xkcd.com/1/# URL,
con lo que, cuando encontremos este previo, sabremos que hemos acabado!!!
'''

import bs4
import requests
import sys
from pathlib import Path


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
