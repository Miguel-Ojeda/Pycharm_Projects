import cProfile
def fib_5(n: int) -> int:
    if n < 2:
        return n
    resultado = 1
    anterior = 0
    for n in range(2, n + 1):
        '''Opción 1
        aux = resultado
        resultado += anterior
        anterior = aux
        '''
        '''Opción 2, más simple
        primero intercambiamos valores, y luego actualizamos el resultado
        anterior, resultado = resultado, anterior
        resultado += anterior
        '''
        '''Opción 3, más simple todavía'''
        anterior, resultado = resultado, resultado + anterior
    return resultado

resultado = fib_5(8)
print(resultado)

# Evidentemente, aquí, como es iterativa, en el cálculo sólo se invoca una función
# es la versión más eficiente, lógicamente...

resultado = fib_5(20)
print(resultado)
cProfile.run('fib_5(20)')
'''
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 05 fibonacci iterativo.py:2(fib_5)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''