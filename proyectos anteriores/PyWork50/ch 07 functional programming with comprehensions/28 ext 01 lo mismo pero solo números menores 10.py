"""
As in the exercise, take a list of integers and turn them into strings. However,
you’ll only want to produce strings for integers between 0 and 10. Doing this
will require understanding the if statement in list comprehensions as well
"""


# Como list comprehensions... dividimos la list compr en 3 bloques como recomienda Reuven para entenderlo mejor...
def join_numbers_0_10(lista):
    return ', '.join([str(number)
                     for number in lista
                     if 0 <= number <= 10])


# Lo mismo como generator expressions... quito tb. el paréntesis exterior...
def join_numbers_0_10_v2(lista):
    return ', '.join(str(number)
                     for number in lista
                     if 0 <= number <= 10)


resultado = join_numbers_0_10([2, -4, 5, 13, 0.7, 1, 2, 2.7, 3.9, 10.0])
print(resultado)
# >>> 2, 5, 0.7, 1, 2, 2.7, 3.9, 10.0

resultado = join_numbers_0_10_v2([2, -4, 5, 13, 0.7, 1, 2, 2.7, 3.9, 10.0])
print(resultado)
# >>> 2, 5, 0.7, 1, 2, 2.7, 3.9, 10.0

