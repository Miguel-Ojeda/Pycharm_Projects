"""
In the /etc/passwd file you used earlier, what different shells are assigned to users?
Use a set comprehension to gather them.
"""
import pprint

def get_shells(passwd_file):
    with open(passwd_file) as pw_file:
        return {linea.split(':')[-1].strip()
                for linea in pw_file
                if not linea.startswith('#')
                if not linea.isspace()
                }




passwd_file = 'files/passwd.txt'
resultado = get_shells(passwd_file)
pprint.pprint(resultado)