# Reconocimiento de patrones 'manual'
# Los teléfonos de EEUU son del tipo: 415-555-4242
# Esto es previo... luego veremos el uso de la
# herramienta de expresiones regulares, que es
# muchísimo más potente

def is_phone_number(text: str):

    # Tiene que tener longitud 12!!
    if len(text) != 12:
        return False

    guiones = text[3] + text[7]
    if guiones != '--':
        return False

    digitos = text[:3] + text[4:7] + text[8:]
    # print('Dígitos:', digitos)
    if digitos.isalnum():
        return True
    else:
        return False

# Ahora una función que busca números de teléfono EEUU en los mensajes...
def locate_phone_numbers(message):
    if not message:
        return
    for i in range(len(message)):
        seleccion = message[i:i+12]
        # seleccionamos doce caracteres.... recuerda que no hay problema con los slices si nos salimos...
        if is_phone_number(seleccion):
            print(f'He encontrado un número de teléfono en el texto: {seleccion}')
    # es bastante cutre la implementación, podríamos hacerlo más inteligente
    # por ejemplo, si encontramos un teléfono avanzar i 12 lugares, etc...


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
locate_phone_numbers(message)
