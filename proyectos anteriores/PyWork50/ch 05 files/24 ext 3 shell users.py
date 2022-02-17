"""
The final field in /etc/passwd is the shell, the Unix command interpreter that’s
invoked when a user logs in. Create a file, containing one line per shell, in
which the shell’s name is written, followed by all of the usernames that use the
shell; for example
/bin/bash: root, jci, user, reuven, atara
/bin/sh: spamd, gitlab
"""
import pprint
from pathlib import Path
from collections import defaultdict

def shell_users(passwd_file):
    passwd_file = Path(passwd_file)
    dir_base = passwd_file.parent
    output_file = dir_base / f'{passwd_file.stem}_shell_users'

    shells = defaultdict(list)

    with open(passwd_file) as password:
        for linea in password:
            if linea.startswith('#') or not linea.strip():
                continue
            user, *resto, shell = linea.strip().split(':')
            shells[shell].append(user)

    with open(output_file, 'w') as users_shell:
        users_shell.write('Lista de shells con sus usuarios\n')
        for shell, usuarios in shells.items():
            usuarios = ', '.join(usuarios)
            users_shell.write(f'--> {shell}: {usuarios}\n')







passwd_file = 'files/ejemplo_passwd'
shell_users(passwd_file)