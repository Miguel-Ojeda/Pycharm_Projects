import requests  # va a descargar de la web lo que le digamos
import bs4  # va a analizar el html con el parser...

# Para llamar a beautiful soup para que analice una página web, antes tenemos que tener el contenido
# en una string... o en un objeto file también vale...
#
# pues vamos a descargar la página y luego meterla en una string para poder analizarla

request = requests.get('https://nostarch.com')
request.raise_for_status()
html_content = request.text

# nostarch_soup = bs4.BeautifulSoup(html_content, features='html.parser')
# # Ahora tenemos ya un BeatifulSoup object...
# # (también podíamos haber pasado a BeautifulSoup un objeto file)

file = open('files/example.html')
# exampleSoup = bs4.BeautifulSoup(file, 'html.parser')
# el html parser ya viene con python...
# se puede instalar el lxml que es más rápido!!
exampleSoup = bs4.BeautifulSoup(file, 'lxml')

exampleSoup.select()

file.close()
'''
# Extracción de ELEMENTOS--- método select()
# Habría que pasarle un string o CSS selector de lo que estamos buscando!!!
# Los selectors son similares a expresiones regulares
'''

'''
Lo primero ahora es seleccionar con método select...

Posibilidades de selector...

Buscar elementos con el nombre dado:
soup.select('div') --> All elements named <div>

Buscar elementos que incluyen el atributo dado
soup.select('#author')  --> The element with an id attribute of author

buscar elementos con el atributo CSS dado
soup.select('.notice')  --> All elements that use a CSS class attribute named notice

Busca elementos ubicados dentro de otros
soup.select('div span')  --> All elements named <span> that are within an element named <div>

Busca elementos ubicados justo interiormente un nivel por dentro de otros
soup.select('div > span')  --> All elements named <span> that are directly within
                                an element named <div>, with no other element in between

Elementos con el nombre dato, que incluyan el atributo dado entre corchetes
soup.select('input[name]')  --> All elements named <input> that have a name attribute with any value

Elementos con el nombre dado, que incluyan el atributo dato, con el valor dado
soup.select('input[type]="button"]')  --> All elements named <input> that have an attribute named type with value button
'''


'''
Cuando, en las anterior condiciones, hacemos el método select() en el objeto beatifulsoup, el método nos devuelve
una lista de objetos tab (realmente va a ser un objeto tipo ResultSet) con todos los tags que cumplen con las 
condiciones. 

Por ejemplo... para buscar elementos de un bloque p
elems = example_soup.select('p')
Ahora podremos referirnos a cada elemento, o iterando, o con el índice
item = elems[0]



Con cada elemento del ResultSet podríamos hacer varias cosas...

Ver toda la cadena --> str(item)
Ver el texto (lo que está en medio de los tags) --> item.getText()
Ver los atributos que contiene el tag... --> item.attr  --> nos devuelve un dict...
Buscar el valor de un atributo--- item.get(atributo) -- si no existiera, nos devuelve None
'''