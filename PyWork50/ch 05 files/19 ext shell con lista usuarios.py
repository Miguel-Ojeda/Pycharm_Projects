'''
Read through /etc/passwd, creating a dict in which user login shells (the final
field on each line) are the keys. Each value will be a list of the users for whom
that shell is defined as their login shell.
'''
import pprint

def get_shell_users_dict(filename):
    shell_users_dict = {}
    with open(filename) as file:
        for linea in file:
            linea = linea.strip()
            if linea.startswith('#') or linea == '':
                continue
            user_info = linea.split(':')
            shell = user_info[-1]
            user = user_info[0]
            if shell in shell_users_dict:
                shell_users_dict[shell].append(user)
            else:
                shell_users_dict[shell] = [user]

    return shell_users_dict

# Haremos ahora lo mismo pero con defaultdicts para ahorrar código
from collections import defaultdict
def get_shell_users_dict_v2(filename):
    # ya no hará falta comprobar si tenemos valores para cada shell
    shell_users_dict = defaultdict(list)
    with open(filename) as file:
        for linea in file:
            linea = linea.strip()
            if linea.startswith('#') or linea == '':
                continue
            # Usaremos tb. el truco para asignar ya variables...
            user, *resto, shell = linea.split(':')
            # shell = user_info[-1]
            # user = user_info[0]
            shell_users_dict[shell].append(user)

    return shell_users_dict


shell_users_dict = get_shell_users_dict_v2('files/passwd.txt')
pprint.pprint(shell_users_dict)

