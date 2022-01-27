import sys
import bs4
import webbrowser
import requests
import pprint

# REcordar que para usar sería... search_pypi cosas a buscar.....
# Analizamos cómo queda la url al buscar algo en pypi.org...
# Por ejemplo, si buscamos panda xml, la página aparece como ... https://pypi.org/search/?q=panda+xml

url = 'https://pypi.org/search/?q=' + '+'.join(sys.argv[1:])

# url = 'https://pypi.org/search/?q=panda+xml'   para test

html_results = requests.get(url)
html_results.raise_for_status()

# Miramos la página web para ver donde están los resultados... en el código de la búsqueda...
# Utilizando la herramienta para desarrolladores, inspeccioanndo vemos que los resultados aparecen así
'''
<a class="package-snippet" href="/project/panda/">
    <h3 class="package-snippet__title">
      <span class="package-snippet__name">panda</span>
      <span class="package-snippet__version">0.3.1</span>
      <span class="package-snippet__released"><time datetime="2015-08-03T13:33:15+0000" data-controller="localized-time" data-localized-time-relative="true" data-localized-time-show-time="false" title="2015-08-03 14:33:15" aria-label="2015-08-03 14:33:15">Aug 3, 2015</time></span>
    </h3>
    <p class="package-snippet__description">A Python implementation of the Panda REST interface</p>
  </a>
'''
'''
O sea, si queremos los nombre --> elementos <span class="package-snippet__name">panda</span>
Versión --> elementos <span class="package-snippet__version">0.3.1</span>
Y si simplemente nos interesa la url, pues 
<a class="package-snippet" href="/project/panda/">
'''

# Busquemos los enlaces de los 10 primeros ítems...
# 1º obtener un objeto beautifulsoap

soup = bs4.BeautifulSoup(html_results.text, parser='lxml', features='lxml')
# Para los urls de los paquetes populare ssimplemente utilizar el selector para recuperar
# <a class="package-snippet" href="/project/panda/">

# Creamos el selector
selector = 'a[class="package-snippet"]'
# Como es una clase CCS también podemos hacer
selector = '.package-snippet'

# Seleccionamos en la sopa
elementos = soup.select(selector=selector)

# Ahora sencillo, simplemente extraer as urls...
'''
lista_urls = []
Esto sería para obtener y abrir todos los de la primera página....
for item in elementos:
    url_item = 'https://pypi.org' + item.get('href')
    lista_urls.append(url_item)

    # Las vamos abriendo también...
    webbrowser.open(url_item)


pprint.pprint(lista_urls)
'''

# Imaginamos que queremos abrir, mejor, los 7 primeros resultados...
items_abrir = min(7, len(elementos))
for i in range(items_abrir):
    url_item = 'https://pypi.org' + elementos[i].get('href')
    webbrowser.open(url_item)

