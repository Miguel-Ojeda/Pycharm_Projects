"""
Convert /etc/passwd from a CSV-style file into a JSON-formatted file. The
JSON file will contain the equivalent of a list of Python tuples, with each tuple
representing one line from the file
"""

import json
from pathlib import Path

'''Observar que nuestro password no es el típico de 7 campos, sino q tiene 10, del 0 al 9... 
el 5, 6, 7 no se corresponden con los típicos y podemos pasar de ellos... no sirven...'''


def passwd_to_json(passwd_file):
    directorio = Path(passwd_file).parent
    json_file = directorio / f'{Path(passwd_file).stem}.json'
    passwd_data = []
    with open(passwd_file) as pass_file:
        for linea in pass_file:
            if linea.startswith('#'):
                continue
            elif linea.strip().startswith('\n'):
                continue
            pass_info_user = tuple(linea.split(':'))
            passwd_data.append(pass_info_user)

    with open(json_file, 'wt') as jsonf:
        # si no especificamos indent, será todo supercompacto!!
        # podemos especificar alguna cadena, o número de espacios...
        json.dump(passwd_data, jsonf, indent='\t')
        return json.dumps(passwd_data, indent=4)



file = 'files/passwd.txt'
resultado = passwd_to_json(file)

print(resultado)
