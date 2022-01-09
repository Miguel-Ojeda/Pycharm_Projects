# English to Pig Latin: https://en.wikipedia.org/wiki/Pig_Latin
# Vocales en inglés...
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

def descompone_cadena(cadena):
    '''devuelve tupla formada por prefijo, palabra, sufijo...
    Observar que varias de las partes pueden ser nulas!!!
    La transformación pig_latin sólo se aplica a la palabra'''
    prefijo = sufijo = palabra = ''

    final_prefijo = -1 # esto significaría que no existe prefijo!!!
    while final_prefijo + 1 < len(cadena):
        if not cadena[final_prefijo].isalpha():
            final_prefijo += 1
        else:
            break
    prefijo = cadena[:final_prefijo + 1]
    if prefijo == cadena:
        return(prefijo, '', '')

    inicio_sufijo = len(cadena) - 1
    while not cadena[inicio_sufijo].isalpha():
        inicio_sufijo -= 1
    sufijo = cadena[inicio_sufijo + 1:]

    palabra = cadena[final_prefijo + 1: inicio_sufijo + 1]

    return (prefijo, palabra, sufijo)

def pig_latin(palabra: str):
    if palabra == '':
        return ''
    era_mayusculas = palabra.isupper()
    era_Title = palabra.istitle()

    palabra = palabra.lower()
    # Miramos el primer carácter... a ver si es vocal...
    if palabra[0] in VOWELS:
        respuesta = palabra + 'yay'
    else:
        # buscar la agrupación de consonantes inicial que hay que llevar al final...
        ultima_consonante = 0  # ya verificada!! hay que buscar las siguientes que son consonantes...
        while (ultima_consonante + 1) < len(palabra):
            if palabra[ultima_consonante + 1] in VOWELS:
                break
            else:
                ultima_consonante += 1
        respuesta = palabra[ultima_consonante + 1:] + palabra[:ultima_consonante+1] + 'ay'

    if era_Title:
        respuesta = respuesta.title()
    elif era_mayusculas:
        respuesta = respuesta.upper()

    return respuesta

# message = input('Enter the English message to translate into Pig Latin:')
message = 'My name is AL SWEIGART and I am 4,000 years old.'
palabras = message.split(' ')
nuevas_palabras = []
for agrupacion in palabras:
    prefijo, palabra, sufijo = descompone_cadena(agrupacion)
    nueva_palabra = prefijo + pig_latin(palabra) + sufijo
    nuevas_palabras.append(nueva_palabra)

message_pig_latin = ' '.join(nuevas_palabras)
print(message_pig_latin)



