"""
In the United States, phone numbers have 10 digits—a three-digit area code,
followed by a seven-digit number: XXX-YYY-ZZZZ

Dada una lista de teléfonos, use a list comprehension to return a new list of strings,
in which any phone number whose YYY code begins with the digits 0–5 will have its area code changed to XXX+1.

For example, given the list of strings
['123-456-7890', '123-333-4444', '123-777-8888'],
we want to convert them to
['124-456-7890', '124-333-4444', '123-777-8888'].

Reuven creo que lo hizo distinto, no hizo lo que dice en la definición...
"""
import pprint

# No encontré la forma de hacerlo, pq pensaba que era hacerlo todo__ de golpe...
#  así que miré la solución y veo que utiliza una función auxiliar
# una función auxiliar para cambiar el número de teléfono si es necesario
# no he mirado más, sino que la utiliza luego para la list comprehension

def increment_area_code(full_phone_number):
    area_code, phone_number = full_phone_number.split('-', maxsplit=1)
    if phone_number[0] in '012345':
        area_code = str(int(area_code) + 1)
    return f'{area_code}-{phone_number}'

def increment_all_area_codes(phone_numbers):
    return [increment_area_code(phone_number)
            for phone_number in phone_numbers]



lista_numeros = ['123-456-7890', '123-333-4444', '123-777-8888']

nuevos_numeros = increment_all_area_codes(lista_numeros)
pprint.pprint(nuevos_numeros)
# >>> ['124-456-7890', '124-333-4444', '123-777-8888']
