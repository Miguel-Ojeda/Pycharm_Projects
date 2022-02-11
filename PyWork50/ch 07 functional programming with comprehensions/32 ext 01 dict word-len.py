"""
Given a string containing several (space-separated) words, create a dict in which
the keys are the words, and the values are the number of vowels in each word.

If the string is “this is an easy test,” then the resulting dict would be
{'this':1, 'is':1, 'an':1, 'easy':2, 'test':1}.
"""

def string_to_word_len_dict(frase):
    return {word: sum([letra in 'aeiou'   # Si es True, es como si fuera el valor 1
                       for letra in word.lower()])
            for word in frase.split()}


string_1 = 'this is an easy test'
string_2 = 'Este es otro test amablemente pensado para ti'


resultado = string_to_word_len_dict(string_1)
print(resultado)

resultado = string_to_word_len_dict(string_2)
print(resultado)