# Métodos interesantes
# upper, lower, capitalize, isalpha, isdecimal, isalnum, ...
# ljust, rjust, center,
# split, join, partition...
# Consultar doc python!!! sobre los string methods!!!

def print_justified(diccionario, left_size, right_size, relleno_char):
    for key, value in diccionario.items():
        print(key.ljust(left_size, relleno_char), str(value).rjust(right_size, ' '))



picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

print_justified(picnicItems, 14, 6, '.')