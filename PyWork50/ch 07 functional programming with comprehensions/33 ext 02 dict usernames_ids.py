"""
Use a dict comprehension to create a dict in which the keys are usernames and
the values are (integer) user IDs, based on a Unix-style /etc/passwd file. Hint:
in a typical /etc/passwd file, the usernames are the first field in a row (i.e.,
index 0), and the user IDs are the third field in a row (i.e., index 2). If you need
to download a sample /etc/passwd file, you can get it from http://mng.bz/
2XXg. Note that this sample file contains comment lines, meaning that you’ll
need to remove them when creating your dict.
"""
import pprint


def get_dict_user_ids_v0(passwd_file):
    with open(passwd_file) as password_f:
        return {linea.split(':')[0]: linea.split(':')[2]
                for linea in password_f
                if not linea.startswith('#')
                }




passwd_file = 'files/passwd.txt'
resultado = get_dict_user_ids_v0(passwd_file)
pprint.pprint(resultado)





