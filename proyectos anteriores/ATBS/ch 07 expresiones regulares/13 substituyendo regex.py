# Aparte de utilizar patrones para encontrar sus ocurrencias en cadenas... con search, findall
# podemos utilziar el método sub() para sustituir las ocurrencias de esa regex por otra cadena...
# pattern_obj.sub('Cadena para sustituir', 'cadena en donde buscar')

import re

#ejemplo, por privacidad queremos sustituir la expresión 'Agent XXXX' por 'CENSORED'

regex = r'Agent \w+'   # Esto me va a buscar Agent Juan  o Agent Filomena ...
pattern = re.compile(regex)

cadena_resultante = pattern.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(cadena_resultante)
# CENSORED gave the secret documents to CENSORED.

# En el primer argumento donde aparece la cadena que vamos a colocar para sustituir
# podemos utilizar la expresión \1 o \2 o \3 para referirnos a que coloque ahí el primer grupo encontrado
# o el segundo, o el tercero... etc

# Por ejemplo, imagino que queremos poner lo de antes, pero mostrando, en vez de censored, ?***** donde ? sería
# la primera letra del nombre del agente... O sea, si fuera Agent Johanthan queremos poner J*****

# Lo haríamos así.... igual que antes pero creando un grupo para la primera letra del nombre...
regex = r'Agent (\w)\w*'
pattern = re.compile(regex)
cadena_resultante = pattern.sub(r'Agente \1****', 'Agent Alice gave the secret documents to Agent Bob.')
print(cadena_resultante)
# Agente A**** gave the secret documents to Agente B****.


