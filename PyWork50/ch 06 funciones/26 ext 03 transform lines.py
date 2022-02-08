"""
Write a function, transform_lines, that takes three arguments:
    * a function that takes a single argument,
    * the name of an input file,
    * and the name of an output file.

Calling the function will run the function on each line of the input file,
with the results written to the output file.
(Hint: the previous exercise and this one are closely related.)
"""

def transform_lines_1(func, original_file, transformed_file):
    """ Hagámoslo basándonos en el anterior..."""
    with open(original_file, encoding='utf-8') as original, \
         open(transformed_file, 'w', encoding='utf-8') as transformed:

        for linea in original:
            transformed.write(func(linea))


def transform_lines_2(func, original_file, transformed_file):
    """ Hagámoslo basándonos en el anterior..."""
    with open(original_file, encoding='utf-8') as original, \
         open(transformed_file, 'w', encoding='utf-8') as transformed:

        # Quizás esto es peligroso porque leemos todas las líneas de golpe!!!
        transformed.writelines([func(linea) for linea in original.readlines()])


transform_lines_1(str.capitalize, 'files/43-0.txt', 'files/43-0-capitalize.txt')
transform_lines_2(str.title, 'files/43-0.txt', 'files/43-0-title.txt')
