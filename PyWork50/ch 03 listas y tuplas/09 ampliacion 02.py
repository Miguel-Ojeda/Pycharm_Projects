# Write a function that takes a list or tuple of numbers.
# Return the result of alternately adding and subtracting numbers from each other.
# So calling the function as plus_minus([10, 20, 30, 40, 50, 60]),
# you’ll get back the result of 10+20-30+40-50+60, or 50.

def plus_minus(secuencia: list):
    if not secuencia:
        return 0

    # Inicialmente el total es el primer elemento...
    total = secuencia.pop(0)

    # mientras quede algo
    while secuencia:
        total += secuencia.pop(0)
        if secuencia:
            # si queda algo, ahora toca restar el siguiente...
            total -= secuencia.pop(0)

    return total


print(plus_minus([10, 20, 30, 40, 50, 60]))
