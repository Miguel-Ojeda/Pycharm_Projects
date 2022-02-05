import webbrowser   # es de la standar library que viene con Python
import pprint   # También viene con Python
import requests
import json  # Sólo para probar como se ve con el método dump...

print("Let's find an old website.")
site = input("Type a website URL: ")
era = input("Type a year, month, and day, like 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = requests.get(url)

# pprint.pprint(response.text)
# print(type(response.text))

data = response.json()

# Lo pasamos a json, simplemente por comodidad para acceder a los datos...
# Si miráramos simplemente el texto habría que ir buscando...
# Con el json obtenemos algo con una estructura jerárquica-->
# print(data)
'''
{'archived_snapshots': {'closest': {'available': True,
                                    'status': '200',
                                    'timestamp': '20151023052507',
                                    'url': 'http://web.archive.org/web/20151023052507/http://www.lolcats.com:80/'}},
 'timestamp': '20151022',
 'url': 'lolcats.com'}
'''

# Para acceder a la url simplemente sería parecido a un diccionario, pero, en este json, con 3 niveles...
# Realmente data es un diccioanario, pero como algunos valores pues son tb. diccionarios, podemos
# ir navegando por varios niveles!!
print(type(data))  # --> <class 'dict'>
pprint.pprint(data)
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    # Si no existe este campo, pues se produciría una excepción!!!
    print("Found this copy: ", old_site)
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)

