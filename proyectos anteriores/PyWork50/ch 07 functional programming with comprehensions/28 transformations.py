"""
For this exercise, write a function (join_numbers) that takes a range of integers.
The function should return those numbers as a string, with commas between the numbers.
That is, given range(15) as input, the function should return this string:
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
"""


def join_numbers(rango):
    return ','.join([str(number) for number in rango])

def join_numbers_v2(rango):
    """
    Leer el documento list comprehensions y gen expressions.py de este capítulo
    Reuven matiza que también se pueden usar geneerator expresions
    que son muy parecidos a las list comprehensions pero que no ocupan
    la memoria como las listas, pq no creean todo_ el objeto de golpe,
    sino ítem a ítem...
    La expresión en este caso sería, usando generator expresions...
    return ','.join((str(number) for number in rango))
    Pero como, cuando el único argumento de una función es un generator expression
    se puede omitir el paréntesis de la generator expre.... quedaría...
"""
    return ','.join(str(number) for number in rango)

# Con list comprehensions
resultado = join_numbers(range(15))
print(resultado)
# Con generator expressions (sin consumo de memoria!!)
resultado = join_numbers_v2(range(15))
print(resultado)
