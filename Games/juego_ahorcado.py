import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''','''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''','''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']


palabras = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt otter owl panda
parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
skunk sloth snake spider stork swan tiger toad trout turkey turtle
weasel whale wolf wombat zebra'''.split()

diccionario_de_palabras = {}
diccionario_de_palabras['frutas']= 'manzana pera albaricoque kiwi aguacate'.split()
diccionario_de_palabras['animales']='perro gato ballena guepardo puma leon conejo raton gacela liebre conejo'.split()
diccionario_de_palabras['colores']='blanco negro gris marron verde cyan amarillo magenta rosa morado purpura'.split()
diccionario_de_palabras['formas']= '''triangulo circulo circunferencia cono prisma piramide esfera ovalo pentagono 
                                        cuadrado trapecio paralelogramo elipse parabola pentagono decagono'''.split()

def display_palabra_con_espacios(palabra):
    for letra in palabra:
        print(letra, end = ' ')
    print()


def display_status():
    num_fallos = len(letras_falladas)
    longitud_palabra = len(palabra_secreta)
    print(HANGMAN_PICS[num_fallos])
    print("Letras falladas: ", end = '')
    display_palabra_con_espacios(letras_falladas)
    print("Letras acertadas: ", end='')
    display_palabra_con_espacios(letras_acertadas)

    mostrar = ''
    for letra in palabra_secreta:
        if letra in letras_acertadas:
            mostrar += letra
        else:
            mostrar += '_'
    print(f"La palabra secreta, de la categoría {categoria} es: ", end = '')
    display_palabra_con_espacios(mostrar)
    print()

def nueva_letra():
    while True:
        letra = input("Elige una nueva letra para probar: ")
        letra = letra.lower()
        if len(letra) != 1:
            print("Sólo debes escribir una letra!!")
        elif letra in todas_letras_probadas:
            print("Ya habías dicho esa letra, prueba otra...")
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print("Debes introducir una letra, ningún otro carácter es válido")
        else:
            return letra

def juegas_de_nuevo():
    juegas_otra = input("Quieres jugar otra partida? (y/n): ")
    return juegas_otra.lower().startswith('y')

def acertadas_todas(palabra, letras):
    for letra in palabra:
        if letra not in letras:
            return False
    return True

def elegir_categoria_y_palabra(diccionario):
    clave = random.choice(list(diccionario.keys()))
    return [clave, random.choice(list(diccionario[clave]))]


# A JUGAR!!!
# Inicializamos estados...
nueva_partida = True
partida_terminada = False

while True:
    if nueva_partida: # justo estamos empezando una nueva partida ahora...
        nueva_partida = False
        categoria, palabra_secreta = elegir_categoria_y_palabra(diccionario_de_palabras)
        letras_acertadas = letras_falladas = todas_letras_probadas = ''
        print('Nueva partida de H A N G M A N')
        display_status()

    letra_a_probar = nueva_letra()
    todas_letras_probadas += letra_a_probar
    if letra_a_probar in palabra_secreta:
        letras_acertadas += letra_a_probar
    else:
        letras_falladas += letra_a_probar
    display_status()


    if acertadas_todas(palabra_secreta, letras_acertadas): # hemos terminado
        print(f"Felicidades, has descubierto la palabra secreta: '{palabra_secreta}'.")
        partida_terminada = True
    elif len(letras_falladas) == len(HANGMAN_PICS) -1:  #hemos terminado, demasiados fallos...
        print(f"Lo siento, demasiados fallos... La palabra secreta era: '{palabra_secreta}'.")
        partida_terminada = True

    if partida_terminada:
        if juegas_de_nuevo():
            nueva_partida = True
            partida_terminada = False
        else:
            break
