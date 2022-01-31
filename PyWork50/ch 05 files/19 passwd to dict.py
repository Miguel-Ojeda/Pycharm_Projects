'''
In this exercise, write a function, passwd_to_dict, that reads from a Unix-style
“password file,” commonly stored as /etc/passwd, and returns a dict based on it.
Each line is one user record, divided into colon-separated fields.
The first field (index 0) is the username, and the third field (index 2) is the user’s unique ID number.
For our purposes, you can ignore all but these two fields.
'''

from io import StringIO
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
    name_id = {}
    with open(filename) as file:
        for linea in file:
            '''
            Reuven se ahorra el strip()
            Simplemente utiliza if not line.startswith(('#', '\n')) 
            Lo malo que esto sólo sirve para líneas en blanco, no si tiene espacios
            '''
            linea = linea.strip()
            if linea.startswith('#') or linea == '':
                continue
            user_info = linea.split(':')
            name_id[user_info[0]] = user_info[2]
            '''
            Otra opción que vi en Reuven es aprovechar ya con el split, y asignar variables...
            user_name, *ignore, user_id = linea.split(':')
            # *ignore aquí significa lista con los otros campos, que no nos interesan, 
            # para no poner los otros 6 campos, ponemos *, para indicar que es una lista con lo otro..
            name_ide[user_name] = user_id
            '''

    return name_id


diccionario = passwd_to_dict('files/passwd.txt')
pprint.pprint(diccionario)

