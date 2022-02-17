"""
In this exercise, piglatin_file applied the piglatin_word function to every word in a file.
Write a new function, func_file, that will take two arguments —a filename and a function.

The output from the function should be a string, the result of invoking the function on each word in the text file.
You can think of this as a generic version of piglatin_file, one that can return any string value.
"""

def func_file(text_file, function):
    with open(text_file, encoding='utf-8') as texto:
        return ' '.join(function(palabra)
                        for linea in texto
                        for palabra in linea.strip().split())



# Podemos utilizar la función func_file para aplicar, a cada palabra del fichero, la función adicional que queramos
# la función puede ser cualquiera, una definida por nosotros, u otra cualesquiera de Python, etc

text_file = 'files/43-0.txt'
resultado = func_file(text_file, str.lower)
print(resultado)

resultado = func_file(text_file, str.capitalize)
print(resultado)
