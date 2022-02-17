'''
From /etc/passwd, create a dict in which the keys are the usernames (as in the
main exercise) and the values are themselves dicts with keys (and appropriate
values) for user ID, home directory, and shell.
Nos interesa guardar en el diccioanrio el uid, el home, y el shell..
'''

from io import StringIO  # para hacer pruebas
import pprint

fake_file = StringIO('''
# This is a comment
# You should ignore me

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
''')

def passwd_to_dict(filename):
    output = dict()
    for linea in fake_file:
        linea = linea.strip()
        if linea.startswith('#') or linea == '':
            continue
        username, password, uid, *ignore, home, shell = linea.split(':')
        output[username] = {'UID': uid, 'home': home, 'shell': shell}

    return output

datos_usuarios = passwd_to_dict('files/passwd.txt')
pprint.pprint(datos_usuarios)