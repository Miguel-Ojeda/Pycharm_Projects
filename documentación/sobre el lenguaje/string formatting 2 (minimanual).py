# Resumen muy bueno sacado del libro Introducing Python chapter 5

'''
ESTO ES VÁLIDO PARA CUALQUIER MÉTODO, el antiguo de %, el de format, el de las f-strings...
Table 5-1. Conversion types
s string
d decimal integer
x hex integer
o octal integer
f decimal float
e exponential float
g decimal or exponential float
'''

numero = 145
# print(f'{numero:s}')
# No hace falta el formato string, pq por defecto se convierte a string
print(f'{numero}')
print(f'{numero:b}')  # --> 10010001
print(f'{numero:o}')  # --> 221
print(f'{numero:x}')  # --> 91
print(f'{numero:f}')  # 145.000000
print(f'{numero:e}')  # 1.450000e+02

'''
El minilenguaje completo es el siguiente:

•   An initial colon (':').
•   An optional fill character (default ' ') to pad the value string if it’s shorter than minwidth.
•   An optional alignment character. This time, left alignment is the default.
    '<' also means left, '>' means right, and '^' means center.
•   An optional sign for numbers. Nothing means only prepend a minus sign ('-')
    for negative numbers. ' ' means prepend a minus sign for negative numbers,
    and a space (' ') for positive ones.
•   An optional minwidth. An optional period ('.') to separate minwidth and maxchars.
•   An optional maxchars.
•   The conversion type.
'''

thing = 'wereduck'
place = 'werepond'
numero = 140_000

print(f'The {thing:>20} is in the {place:^20}')
# The             wereduck is in the       werepond
print(f'The {thing:#>20} is in the {place:.^20}')
# The ############wereduck is in the ......werepond......
print(f'The {thing:-^20} is in the {place:-^20}, a {numero:-^20} metros de distancia')
# The ------wereduck------ is in the ------werepond------, a -------140000------- metros de distancia
print(f'The {thing:-^20} is in the {place:-^20}, a {numero:-^20x} metros de distancia')
# The ------wereduck------ is in the ------werepond------, a -------222e0-------- metros de distancia
# Si queremos rellenar el principio del número con 0, es simplemente utilizar el carácter 0
print(f'The {thing:-^20} is in the {place:-^20}, a {numero:0>20} metros de distancia')
# The ------wereduck------ is in the ------werepond------, a 00000000000000140000 metros de distancia
# Podemos separar de 3 en 3 con comas o con _
print(f'The {thing:-^20} is in the {place:-^20}, a {numero:^20_} metros de distancia')
# The ------wereduck------ is in the ------werepond------, a       140_000        metros de distancia














