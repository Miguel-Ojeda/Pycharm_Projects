"""
For a slightly different challenge, turn each line in the file into a Python dict.
This will require identifying each field with a unique column or key name.
If you’re not sure what each field in /etc/passwd does, you can give it an arbitrary name.
"""
from pathlib import Path
import json


'''Observar que nuestro password no es el típico de 7 campos, sino q tiene 10, del 0 al 9... 
el 5, 6, 7 no se corresponden con los típicos y podemos pasar de ellos... no sirven...
Buscando en internet veo que en estos passwords con 10 campos... cada uno es...
0 -> Username
1 -> Password
2 ->UID
3 .> GID
4 -> Class ... should be left empty.
5 -> Change ... 
6 -> Expiry ...
7 -> Gecos
8 -> Home
9 -> Shell

Observar que lo típico creo que son 7 campos sólos (no estaríasn ni 4, 5, 6)
'''

def passwd_to_json_dictionary(passwd_file):

    directorio = Path(passwd_file).parent
    json_file = directorio / f'{Path(passwd_file).stem}_dict.json'
    passwd_data = []
    campo = ['User Name', 'Password', 'UID', 'GID', 'Class', 'Change', 'Expiry', 'GECOS', 'Home', 'Shell']
    with open(passwd_file) as pass_file:
        for linea in pass_file:
            if linea.startswith('#'):
                continue
            elif linea.strip().startswith('\n'):
                continue
            pass_info_user = linea.split(':')
            # Ahora lo pasamos a diccionario...
            pass_info_user = {campo[i]: pass_info_user[i] for i in range(0, 10)}
            passwd_data.append(pass_info_user)
            '''
            Otra opción que usa Reuven para crear el diccionario es la función zip, que crea tuplas
            con los elementos de los iterables que les demos...
            Como crea tuplas, él lo transforma en diccioanrio....
            output.append(dict(zip(fields, one_line.split(':'))))
            '''

    with open(json_file, 'wt') as jsonf:
        # si no especificamos indent, será todo supercompacto!!
        # podemos especificar alguna cadena, o número de espacios...
        json.dump(passwd_data, jsonf, indent='\t')

    return json.dumps(passwd_data, indent=4)



file = 'files/passwd.txt'
resultado = passwd_to_json_dictionary(file)

print(resultado)
