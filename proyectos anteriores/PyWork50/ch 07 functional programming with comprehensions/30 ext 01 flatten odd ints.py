"""
Write a version of the flatten function mentioned earlier called flatten_odd_ints.
It’ll do the same thing as flatten, but the output will only contain odd integers.

* Inputs that are neither odd nor integers should be excluded.
* Inputs containing strings that could be converted to integers should be converted;
* other strings should be excluded
"""


def flatten_list(lista):
    return [int(item)
            for sublista in lista
            for item in sublista
            if (isinstance(item, int) and (item % 2))
            or (isinstance(item, str) and item.strip().isdigit() and (int(item) % 2))
            ]


def flatten_list_2(lista):
    """Reuven se ahorra un condicional y varios métodos intermedios!!!
    Primero convierte (si no lo fuera) el elemento a analizar cadena y
    ya no tiene que estar con varios casos
    Es más corto y sencillo"""
    return [int(item)
            for sublista in lista
            for item in sublista
            if str(item).strip().isdigit() and int(item) % 2
            ]


lista = [[], [1, 2], [3, 4], [5, 6, 7, 8], [9], [10], ['aa', 12], ['b', 11,  '   13   ']]
lista_plana = flatten_list(lista)
print(lista_plana)

lista_plana_2 = flatten_list_2(lista)
print(lista_plana_2)