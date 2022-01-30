from io import StringIO

'''
StringIO objects are what Python calls “file-like objects.”
They implement the same API as file objects, allowing us to read from them and write to them just like files.
Unlike files, though, StringIO objects never actually touch the filesystem.

Por esta razón son ideales para hacer cualquier test o correr programas sin tener que acceder a ficheros reales.
Además que es mucho más rápido, imagino...
O sea, son objetos que soportan las mismas apis con la que se manejan ficheros, y por tanto podemos usarlas en su lugar.
'''


def get_final_line_v2(file_name):
    for linea in fake_file:  # aquí hacemos el test con la StringIO
        linea_final = linea
    return linea_final


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

print(get_final_line_v2('cualquier cosa'))

# --> mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
