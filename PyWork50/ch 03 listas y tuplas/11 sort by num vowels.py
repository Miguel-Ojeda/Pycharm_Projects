def count_vowels(word):
    contador = 0
    for letter in word:
        if letter in ('a', 'e', 'i', 'o', 'u'):
            contador += 1

    return contador

lista = ['holaaaaaa', 'ijlokhjht', 'balandril']
lista_ordenada = sorted(lista, key=count_vowels)
print(lista, '\n', lista_ordenada)
lista = ['miguel', 'carlos', 'iris', 'eustaquio', 'angel', 'joel', 'mariate', 'yurena', 'margarita']
lista_ordenada = sorted(lista, key=count_vowels)
print(lista, '\n', lista_ordenada)








# Pruebas
# word = 'abecedario'
# contador = count_vowels(word)
# print(word, ' vocales --> ', contador)
# word = 'yzlaighj'
# contador = count_vowels(word)
# print(word, ' vocales --> ', contador)
# word = 'artilugio'
# contador = count_vowels(word)
# print(word, ' vocales --> ', contador)
# word = 'megalomaniaco'
# contador = count_vowels(word)
# print(word, ' vocales --> ', contador)
# word = 'uxuxu'
# contador = count_vowels(word)
# print(word, ' vocales --> ', contador)
# word = 'ajjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj'
# contador = count_vowels(word)
# print(word, ' vocales --> ', contador)
