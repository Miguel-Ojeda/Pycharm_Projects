# Given a sequence of positive and negative numbers, sort them by absolute value

lista = [-5, 7, 2, 3, 0, -14, 5, -3.28, -2.14, 3.27]

sorted_abs = sorted(lista, key=abs)

print(sorted_abs)