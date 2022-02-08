
import pprint
import json


diccionario = [{1: 'Juan', "2": 254000, 'profesion': 'azul'},
               {14: 'Juan P', "22": 2, 'profesion': 'verde'},
               {111: 'Juan Luis', 'ho': "2", 'profesion': 'amarillo'},
               ]
resultado = json.dumps(diccionario, indent=4)
print(resultado)

def fu(bar):
    print(bar, bar, bar)

resultado = json.dumps(fu, indent=4)
# Error, no se puede serializar con JSON objetos tipo función
# Sólo permite listas, tuplas, diccionarios, ...
print(resultado)
