# Given a list of lists, with each list containing zero or more numbers, sort by the
# sum of each inner list’s numbers

lista = [[2, 3, 0, 0, 0, 0], [2, 3, -1], [6, 1], [8]]
lista_ordenada = sorted(lista, key=sum)

print(lista_ordenada)
# >>> [[2, 3, -1], [2, 3, 0, 0, 0, 0], [6, 1], [8]]