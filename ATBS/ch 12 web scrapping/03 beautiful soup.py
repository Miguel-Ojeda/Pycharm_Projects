import requests  # va a descargar de la web lo que le digamos
import bs4  # va a analizar el html con el parser...

# Para llamar a beautiful soup para que analice una página web, antes tenemos que tener el contenido
# en una string... pues vamos a descargar la página y luego meterla en una string para poder analizarla

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

'''
# Extracción de ELEMENTOS--- método select()
# Habría que pasarle un string o CSS selector de lo que estamos buscando!!!
# Los selectors son similares a expresiones regulares
'''

'''
Posibilidades de selector...

soup.select('div') --> All elements named <div>
soup.select('#author')  --> The element with an id attribute of author
soup.select('.notice')  --> All elements that use a CSS class attribute named notice
soup.select('div span')  --> All elements named <span> that are within an element named <div>
soup.select('div > span')  --> All elements named <span> that are directly within
                                an element named <div>, with no other element in between
soup.select('input[name]')  --> All elements named <input> that have a name attribute with any value
soup.select('input[type="button"]')  --> All elements named <input> that have an attribute named type with value button
'''


'''
The select() method will return a list of Tag objects, which is how Beautiful Soup represents an HTML elemens
Estos tags values pueden ser pasados a la función str() para msotrar las tags HTML que representan
Tag values also have an attrs attribute that shows all the HTML attributes of the
tag as a dictionary
'''

'''
Lo primero ahora es seleccionar con método select...
Nos devuelve un objeto ResultSet, que es como una lista con todos los elementos que coinciden...
Por ejemplo... para buscar elementos de un bloque p
elems = example_soup.select('p')
Ahora podremos referirnos a cada elemento, o iterando, o con el índice, realmente es como un set o una lista???

que podemos hacer con cada item de elems.. por ejemplo, con item = elems[0]
Ver toda la cadena --> str(item)
Ver el texto (lo que está en medio de los tags) --> item.getText()
Ver los atributos que contiene el tag... --> item.attr  --> nos devuleve un dict...
Buscar el valor de un atributo--- item.get(atributo) -- si no existiera, nos devuelve None



'''






print(type(exampleSoup))
