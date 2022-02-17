"""
Create a list whose elements are strings—the names of people in your family.
Now use a set comprehension (and, better yet, a nested set comprehension) to
find which letters are used in your family members’ names.
"""


def get_letters_in_names(nombres):
    return {letra
            for palabra in nombres
            for letra in palabra.lower()}


def get_letters_in_names_v2(nombres):
    """Reuven mejor, pq primero une todas las palabras, en una cadena...
    Y luego la recorre"""
    return {caracter
            for caracter in ''.join(nombres).lower()
            if caracter.isalpha()}



nombres = ['Iris', 'Angel', 'Carlos', 'Mariate', 'Miguel']

letras_usadas = get_letters_in_names(nombres)
print(letras_usadas)
letras_usadas = get_letters_in_names_v2(nombres)
print(letras_usadas)




