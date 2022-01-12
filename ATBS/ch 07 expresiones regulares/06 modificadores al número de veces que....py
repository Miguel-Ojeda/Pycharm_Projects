import re

# Optional Matching with the Question Mark --> ?
# ? significa que puede o no aparecer la expresión regular que le precede!!!
# ? significa --> que aparezca 0 ó 1 vez
r_string = r'Miguel (Angel )?Ojeda Acosta'
# Esto quiere decir que el grupo Angel es opcional...
# es válido tanto que aparezca, como que no aparezca...
pattern_ob = re.compile(r_string)

message_1 = 'Me llamo Miguel Angel Ojeda Acosta, y, ...'
message_2 =  'Me llamo Miguel Ojeda Acosta, y, ...'

match_ob_1 = pattern_ob.search(message_1)
match_ob_2 = pattern_ob.search(message_2)

if match_ob_1:
    print(match_ob_1.group())
    # >>> Miguel Angel Ojeda Acosta
if match_ob_2:
    print(match_ob_2.group())
    # Miguel Ojeda Acosta

# Otro ejemplo con el número teléfono EEUU
# Habíamos visto que la expresión era....
# r'\d{3}-\d{3}-d{4}'
# Si queremos que los 3 dígitos iniciales (de área) sean opcionales
# La rstring quedaría...
r_string = r'(\d{3}-)?\d{3}-\d{4}'
pattern_ob = re.compile(r_string)

message_1 = 'My number is 415-555-4242'
message_2 = 'My number is 555-4242'

match_ob_1 = pattern_ob.search(message_1)
match_ob_2 = pattern_ob.search(message_2)

if match_ob_1:
    print(match_ob_1.group())
    # >>>
if match_ob_2:
    print(match_ob_2.group())

# Matching Zero or More with the Star --> *
# Significa eso, que la expresión puede aparecer 0 veces, o las que sean....
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
# 'Batman'
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
# 'Batwoman'
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
# 'Batwowowowoman'

# Matching One or More with the Plus --> +
# Es similar al *, pero como mínimo
# la expresión que le antecede tieen que ocurrir al menos 1 vez !!
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
# >>> mo1.group() --> 'Batwoman'
mo2 = batRegex.search('The Adventures of Batwowowowoman')
# >>> mo2.group()  --> 'Batwowowowoman'
mo3 = batRegex.search('The Adventures of Batman')
# >>> mo3 es None !!!

# Matching Specific Repetitions with Braces --> {num}
# dentro de las llaves indicamos el número de veces concreto
# que debe aparecer para ser reconocido el patrón...

# (Ha){3} will match the string 'HaHaHa', but it will not match 'HaHa'
# Significaría que tiene que repetirse justo 3 veces!!

# Otra forma de uso!! {min_num, max_num}
# (Ha){3,5} se verificaría con 3, 4, o 5 repeticiones....

# SOn equivalentes!!!
# (Ha){3}  --> (Ha)(Ha)(Ha)
# (Ha){3,5} --> ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))
# Cuidado, es {3,5}, no sirve con {3, 5}

# Resumen
# {} especifica un número de veces concreto que se tiene que repetir (o un rango de valores)
# ? significa 0 o 1 repetición
# * significa 0 o más repeticiones
# + significa 1 o más repeticiones

# Greedy and Non Greedy (lazy) matching...
# Por defecto, los match son Greedy, o sea, se intenta acaparar
# y que la expresión encontrada sea lo más posible si hubiera ambigüedad...
# Ejemplo
r_string = r'(Ha){3,5}'
pattern_ob = re.compile(r_string)
match_ob = pattern_ob.search('Ufff, qué mal, HaHaHaHaHa, esperemos que ...')
print(match_ob.group())
# Como por defecto el match es Greedy, codicioso...
# Como tanto HaHaHa, como HaHaHaHa, como HaHaHaHa hacen match... pues
# Nos devuelve el resultado más largo: HaHaHaHaHA
# >>> HaHaHaHaHa

# Podemos configurar el modo lazy utilizando ?
r_string = r'(Ha){3,5}?'
pattern_ob = re.compile(r_string)
match_ob = pattern_ob.search('Ufff, qué mal, HaHaHaHaHa, esperemos que ...')
print(match_ob.group())
# >>> HaHaHa

# Importante: en las expresiones regulares hemos visto que ? tiene dos usos
# totalmente distintos:
# 1: para encontrar 0 o 1 veces la expresión que le antecede...
# 2 para poner modo lazy en la expresión que le antecede!!