# Otros caracteres con significado especial, a los que debemos anteponer \ si queremos buscarlos...
# ----> .  ^  $  *  +  ?  {  }  [  ]  \  |  (  )

# | Pipe.... nos permite hacer match a una expresión o a otra (o a varias!!!)
# ejemplo r_string = r'expresion1|expresion2|expresion3...'
# lo que hará es hacer match si cualquiera de las expresiones es encontrada
# en el grupo se nos genera la primera que encuentra!!!
import re
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
# >>> 'Batman'
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())
# >>> mo2.group()
# >>> 'Tina Fey'
# Si quisiéramos que nos mostrara todas las ocurrencias, tendríamos que usar el método findall()

# También podemos usar pipe (realmente significa 'o') para
# crear una expresión deonde el match incluya entre varias opciones
r_string = r'Bat(man|mobile|copter|bat)'
# La r-string corresponde a una expresión regular donde el match se inicia con 'Bat'
# seguido po una de las opciones...   man ó mobile ó copter ó bat  (| significa ó)
pattern_object = re.compile(r_string)
match_oject = pattern_object.search('Mi Batmobile lost a wheel')
if match_oject:
    print(match_oject.group()) # mostramos el match entero encontrado!!
    # >>> 'Batmobile'
    # Mostramos el primer grupo
    print(match_oject.group(1))
    # >>> 'mobile'

# Pero no encuentra el match esto....
match_oject = pattern_object.search('Mi batmobile lost a wheel')
# Porque hemos puesto la b en minúscula
if match_oject:
    print(match_oject.group()) # mostramos el match entero encontrado!!
else:
    print('No encontrado pattern en "Mi batmobile ...."')

# Es fácil arreglarlo con el operador Pipe!!
# Modifiquemos la r_string...
r_string = r'B|bat(man|mobile|copter|bat)'
pattern_object = re.compile(r_string)
match_oject = pattern_object.search('Mi batmobile lost a wheel')
# Porque hemos puesto la b en minúscula
if match_oject:
    print('Ahora sí hemos encontrado un match:', match_oject.group())




