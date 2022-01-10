# Pasar una palabra al 'idioma' Ubbi Dubbi
"""Simplemente escribiremos una función que, dada una palabra,
si hay una vocal le antepone ub.. is None:
    Ejemplo... program --> prubogrubam """

def ubbi_dubbi(word):
    vocales = ('a', 'e', 'i', 'o', 'u')
    ubbi = ''
    for letra in word:
        if letra in vocales:
        # Realmente más fácil if letra in 'aeiou':
            ubbi += 'ub'
        ubbi += letra

    return ubbi

def ubbi_dubbi_2(word):
    # Haremos lo mismo con lista...
    # por lo visto, para casos de muchas strings conviene utilizar listas...
    #pq las strings como son inmutables consumen mucha memoria...
    # cada operación de +  realmente crea un nuevo objeto....
    ubbi = []
    for letra in word:
        if letra in 'aeiou':
            ubbi.append('ub')
        ubbi.append(letra)

    # Ya tenemos la lista... ahora unimos todo_ para crear 1 cadena...
    # Para ello, utilizamos el método join() de strings... lo invocamos desde el objeto
    # con la cadena que queremos utilziar como separador (en este caso, nada!!!)
    return ''.join(ubbi)


print(ubbi_dubbi('program'))
print(ubbi_dubbi_2('program'))

print(ubbi_dubbi('octopus'))
print(ubbi_dubbi_2('octopus'))

print(ubbi_dubbi('elephant'))
print(ubbi_dubbi_2('elephant'))
