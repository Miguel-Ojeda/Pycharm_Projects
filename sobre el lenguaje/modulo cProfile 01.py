# es mucho más completo que timeit pq analiza no sólo velocidad, sino tb uso de memoria y muchas más cosas!!

import cProfile


def addUpNumbers():
    total = 0
    for i in range(1, 1000001):
        total += i


cProfile.run('addUpNumbers()')

'''
         4 function calls in 0.062 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.062    0.062 <string>:1(<module>)
        1    0.062    0.062    0.062    0.062 modulo cProfile 01.py:6(addUpNumbers)
        1    0.000    0.000    0.062    0.062 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

'''
Aclaración del resultado:
ncalls The number of calls made to the function
tottime The total time spent in the function, excluding time in subfunctions
percall The total time divided by the number of calls
cumtime The cumulative time spent in the function and all subfunctions
percall The cumulative time divided by the number of calls
filename:lineno(function) The file the function is in and at which line number
'''

# Ejemplo para ver el profile de la ejecución de un programa real para encriptar
'''
For example, download the rsaCipher.py and al_sweigart_pubkey.txt files
from https://nostarch.com/crackingcodes/. This RSA Cipher program was featured in Cracking Codes with Python
(No Starch Press, 2018).
Enter the following into the interactive shell to profile the encryptAndWriteToFile() function
as it encrypts a 300,000-character message created by the 'abc' * 100000 expression:
'''

import files.rsaCipher
cProfile.run("files.rsaCipher.encryptAndWriteToFile('files/encrypted_file.txt', 'files/al_sweigart_pubkey.txt', 'abc'*100000)")

'''El resultado es una estadística completísima:

         11745 function calls in 32.774 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001   32.774   32.774 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 codecs.py:186(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.009    0.009 cp1252.py:18(encode)
        1    0.000    0.000    0.000    0.000 cp1252.py:22(decode)
        1    0.020    0.020   32.773   32.773 rsaCipher.py:104(encryptAndWriteToFile)
        1    0.256    0.256    0.257    0.257 rsaCipher.py:36(getBlocksFromText)
        1    0.004    0.004   32.741   32.741 rsaCipher.py:70(encryptMessage)
        1    0.000    0.000    0.000    0.000 rsaCipher.py:94(readKeyFile)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_decode}
        1    0.009    0.009    0.009    0.009 {built-in method _codecs.charmap_encode}
        1    0.000    0.000   32.774   32.774 {built-in method builtins.exec}
     2347    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     2344    0.000    0.000    0.000    0.000 {built-in method builtins.min}
     2344   32.479    0.014   32.479    0.014 {built-in method builtins.pow}
        2    0.002    0.001    0.002    0.001 {built-in method io.open}
     4688    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        2    0.000    0.000    0.000    0.000 {method 'close' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'encode' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'read' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        1    0.001    0.001    0.010    0.010 {method 'write' of '_io.TextIOWrapper' objects}
'''
'''
Podemos ver que la función builtins.pow es la que casi se lleva todo el tiempo (32.449 de los 32.774 segundos!!!
Aunque en este caso no podemos cambiar la función (pq viene con Python) sí que podemos, en otros casos, saber
lo que nos interesa optimizar...
Bueno, incluso en este caso podemos ver si existe alguna forma de tirar menos de esta función...
Lo que tenemos claro con este análisis, es que no tiene sentido tratar de optimizar funciones nuestras, como
readKeyFile, porque no consumen prácticamente nada!!!
'''

# Observar, además, que a diferencia de timeit, cProfile ya conoce las funciones definidas o importadas!!!

