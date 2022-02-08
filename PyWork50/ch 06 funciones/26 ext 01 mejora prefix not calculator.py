"""
Expand the program you wrote, such that the user’s input can contain any
number of numbers, not just two. The program will thus handle + 3 5 7 or / 100
5 5, and will apply the operator from left to right—giving the answers 15 and 4,
respectively.
"""
import operator

def prefix_notation_calculator_extended(operation):
    operaciones = {'+': operator.add, '-': operator.sub, '*': operator.mul,
                   '**': operator.pow, '/': operator.truediv, '%': operator.mod}
    operacion, *nums = operation.split()


    resultado = operaciones[operacion](float(nums[0]), float(nums[1]))
    for numero in nums[2:]:
        resultado = operaciones[operacion](resultado, float(numero))

    return resultado


def prefix_notation_calculator_extended_v2(operation):
    """La versión de Reuven hace una comprobación a ver si tenemos números
    Además es más sencilla porque inicializa primero el resultado con el primer número"""
    operaciones = {'+': operator.add, '-': operator.sub, '*': operator.mul,
                   '**': operator.pow, '/': operator.truediv, '%': operator.mod}
    operacion, *nums = operation.split()

    if not nums:
        # No hay ningún número!!!
        return 0

    resultado = float(nums[0])
    for numero in nums[1:]:
        resultado = operaciones[operacion](resultado, float(numero))

    return resultado


resultado = prefix_notation_calculator_extended_v2(' ** 2 2 2 2 ')
print(resultado)