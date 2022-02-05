# To make your regex caseinsensitive, you can pass re.IGNORECASE or re.I
# as a second argument to re.compile(). Enter the following into the interactive shell:
import re
robocop = re.compile(r'robocop', re.IGNORECASE)

mo = robocop.search('Hola soy RoboCOP')
if mo:
    print(mo.group())
# Resultado --> RoboCOP
