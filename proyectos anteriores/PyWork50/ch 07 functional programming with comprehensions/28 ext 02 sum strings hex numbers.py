"""
Given a LIST of strings containing hexadecimal numbers, sum the numbers together.
"""


# Como list comprehension
def sum_hex_numbers_string(hex_list):
    return sum([int(numero, base=16)
                for numero in hex_list])


def sum_hex_numbers_string_v2(hex_list):
    """Como generator expression
    """
    return sum(int(numero, base=16)
               for numero in hex_list)



suma = sum_hex_numbers_string(['01','a0', 'f0', 'ab', '20', '34'])
print(suma)

suma = sum_hex_numbers_string_v2(['01', '10', '30', 'a0', '20', 'a'])
print(suma)