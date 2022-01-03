# Escribir una función que aplane una lista!!

def aplanar_lista(lista: list):
    if lista == []:
        return lista
    elif len(lista) == 1:
        if isinstance(lista[0], list):
            return aplanar_lista(lista[0])
        else:
            return lista
    # tenemos 2 o más elementos
    elif isinstance(lista[0], list):
        return aplanar_lista(lista[0]) + aplanar_lista(lista[1:])
    else:
        return [lista[0]] + aplanar_lista(lista[1:])

l = [[[1,2],3,[4,[[5,6],7],[8]]],[9,10,11]]
print (aplanar_lista([[[[]]], [[[1]]], 2, 3, [4, 5, [6, 7, [[[]]]]]]))
print(aplanar_lista(l))