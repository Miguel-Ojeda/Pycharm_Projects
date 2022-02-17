'''
Read through a text file on disk. Use a dict to track how many words of each
length are in the file—that is, how many three-letter words, four-letter words,
five-letter words, and so on. Display your results.
'''
import string
from collections import defaultdict

'''Cuidado, esto no sirve!!
for palabra in palabras:
    palabra = palabra.strip(string.whitespace + string.punctuation)
porque como palabra es una string, inmutable, simplemente se 
crearía otro objeto... y la lista de palabras seguiría con cada
ítem apuntando al antiguo objeto... o sea, palabras no se actualizaría!!'''

'''Si quisiéramos obtener otra lista, QUE NO HACE FALTA, sería así...
nuevas_palabras = []
for palabra in palabras:
    nuevas_palabras.append(palabra.strip(string.whitespace + string.punctuation)
'''

# Utilizamos la función strip para quitar caracteres que no nos interesan
# Si no le decimos nada
'''
str.strip([chars])
Return a copy of the string with the leading and trailing characters removed.
The chars argument is a string specifying the set of characters to be removed.
If omitted or None, the chars argument defaults to removing whitespace.
The chars argument is not a prefix or suffix;
rather, all combinations of its values are stripped:
'''

def contabiliza_palabras_por_longitud(libro: str) -> dict:
    diccionario = defaultdict(int)
    with open(libro) as libro:
        for linea in libro:
            for palabra in linea.split():
                palabra = palabra.strip(string.whitespace + string.punctuation)
                diccionario[len(palabra)] += 1

    return diccionario

libro = 'files/pg25525.txt'
diccionario = contabiliza_palabras_por_longitud(libro)
total_letras = 0
for key, value in diccionario.items():
    print(key, '--->', value)
    total_letras += key * value

print(f'El total de letras contabilizado es de {total_letras:_}')



#
#
# palabras_longitud = dict()
#
# with open('files/pg25525.txt') as libro:
#
#
#     palabras_cambiadas = []
#     for palabra in palabras:
#         palabra = palabra.strip(string.whitespace + string.punctuation)
#         palabras_cambiadas.append(palabra)
#     print(palabras)
#     print(palabras_cambiadas)
#
