"""
For this exercise, I want you to write a function (calc) that expects a single
argument —a string containing a simple math expression in prefix notation—with an
operator and two numbers.
Your program will parse the input and produce the appropriate output.

For our purposes, it’s enough to handle the six basic arithmetic operations in Python:
addition, subtraction, multiplication, division (/), modulus (%), and exponentiation (**).

The normal Python math rules should work, such that division always results in a floating-point number.

We’ll assume, for our purposes, that the argument will only contain one of our six operators and two valid numbers.

But wait, there’s a catch—or a hint, if you prefer: you should implement each of the operations as a separate function,
and you shouldn’t use an if statement to decide which function should be run.
Another hint: look at the operator module, whose functions implement many of Python’s operators.
"""

import operator


def prefix_notation_calculator_v0(operation):
    """
    Esto no es válido... pq utilizo el if que estaba prohibido en el problema
    Lo hago sólo para comparar con las otras implementaciones...
    """
    operacion, num1, num2 = operation.split()
    num1 = float(num1)
    num2 = float(num2)
    if operacion == '+':
        return num1 + num2
    elif operacion == '-':
        return num1 - num2
    elif operacion == '*':
        return num1 * num2
    elif operacion == '**':
        return num1 ** num2
    elif operacion == '/':
        return num1 / num2
    else:
        return num1 % num2


def prefix_notation_calculator_v1(operation):
    """Es mucho más compacto y elegante"""
    operaciones = {'+': operator.add, '-': operator.sub, '*': operator.mul,
                   '**': operator.pow, '/': operator.truediv, '%': operator.mod}
    operacion, num1, num2 = operation.split()
    num1 = float(num1)
    num2 = float(num2)
    return operaciones[operacion](num1, num2)


resultado = prefix_notation_calculator_v1(' **  43  32')
print(resultado)
