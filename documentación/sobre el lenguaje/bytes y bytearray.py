"""
bytes es una string de bytes, pero es INMUTABLE, o sea, son como una tupla de bytes
bytearry es lo mismo, pero mutable, o sea, como una lista de bytes
"""
lista = [0, 1, 2, 3, 64, 65, 66, 0xab, 0b1000000, 200, 248, 255]

the_bytes = bytes(lista)
print(type(the_bytes))
print(the_bytes)
'''
<class 'bytes'>
b'\x00\x01\x02\x03@AB\xab@\xc8\xf8\xff'
Observar que, al mostrar, aquellos valores que se corresponden con caracteres ASCII
64 (0x40) muestra como @, 65 muestra A, 66 muestra A, 0b10000000 = 64 pues muestra @
y los demás se muestran en hexadecimal'''

# También podemos asignarlos de forma similar, dando valores o caracteres ASCII
the_bytes = b'\x00\x01\x02\x03\x40ABCD@k\x52\x1f'
print(the_bytes)
# >>> b'\x00\x01\x02\x03@ABCD@kR\x1f'

# Además, de una byte string podremos obtener un entero...
entero_1 = int.from_bytes(the_bytes, 'big')
# Creamos un entero con esos bytes, suponiendo el primer byte es el más significativo, vamos, lo normal
print(entero_1)
# >>> 311918213854038574766969375
print(f'{entero_1:x}')
# 102034041424344406b521f son los valores en el mismo orden
# falta el primer valor pq es 00, y del segundo sólo se muestra el 1, claro...

# Podemos hacer lo mismo diciendo que el primer byte que damos sea el menos significativo
# the_bytes = b'\x00\x01\x02\x03\x40ABCD@k\x52\x1f'
entero_1 = int.from_bytes(the_bytes, 'little')
print(entero_1)
# >>> 2481580467300923534918719504640
print(f'{entero_1:x}')
# 1f526b40444342414003020100
# ES UN Número formado por los mismos bytes, pero en orden inverso!!!


# los bytes podemos referirnos a ellos por su índice, pero no modificarlos pq son inmutables!!
print(the_bytes[4])
# 64 (0x40)
'''
the_bytes[4] = 65
TypeError: 'bytes' object does not support item assignment
'''

# los bytearray es lo mismo, pero son modificables...
the_byte_array = bytearray(lista)
print(the_byte_array)
# bytearray(b'\x00\x01\x02\x03@AB\xab@\xc8\xf8\xff')
# Se puede hacer lo mismo, y, además , modificar!!