import cProfile

def fib_1(n: int) -> int:
    if n < 2:
        return n
    return fib_1(n - 1) + fib_1(n - 2)

resultado = fib_1(8)
print(resultado)

# El problema con la definición recursiva es que, en seguida, se acumulan muchísimas llamadas
cProfile.run('fib_1(5)')
'''
         18 function calls (4 primitive calls) in 0.000 seconds
...
'''

cProfile.run('fib_1(8)')
'''
70 function calls (4 primitive calls) in 0.000 seconds
'''
cProfile.run('fib_1(10)')
'''
180 function calls (4 primitive calls) in 0.000 seconds
...
177/1    0.000    0.000    0.000    0.000 01 fibonacci.py:3(fib_1)
O sea, 177 llamadas simplemente para calcular fib(10)!!
'''

cProfile.run('fib_1(20)')
'''
21891 llamadas simplemente para calcular fib(20)
21891/1    0.010    0.000    0.010    0.010 01 fibonacci.py:3(fib_1)
'''

# O sea, no podemos utilizar esta implementación, el stack se desbordaría, ya que
# el número de llamadas crece exponencialmente!!
