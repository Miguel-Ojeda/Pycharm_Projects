"""Review of Regular Expression Matching
While there are several steps to using regular expressions in Python, each step is fairly simple.
1. Import the regex module with import re.
2. Create a Pattern / Regex object with the re.compile() function. (Remember to use a raw string.)
3. Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
4. Call the Match object’s group() method to return a string of the actual matched text."""

# 1
import re

# 2 creamos la r_string y el objeto patron...
# para reconocer números teléfono EEUU
r_string = r'\d{3}-\d{3}-\d{4}'
pattern_object = re.compile(r_string)

# mensaje en el que buscaremos el patrón...
message = 'Call me at 415-555-111 tomorrow. 415-555-9999 is my office.'
# 3
# buscamos en el mensaje con el objeto de reconocimeitno de patrones
match_object = pattern_object.search(message)

# 4
# Mostramos las coincidencias
if match_object:
    print('Phone number found: ' + match_object.group())