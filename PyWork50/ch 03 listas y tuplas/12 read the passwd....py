# Write a program to read /etc/passwd on a Unix computer. The first field contains
# the username, and the final field contains the user’s shell, the command interpreter.
# Display the shells in decreasing order of popularity, such that the most popular shell is shown first,
# the second most popular shell second, and so forth.

# Recordar que cada línea se compone de 7 campos separados por :
# Each line in /etc/passwd file represents an individual user account and contains
# following seven fields separated by colons (:).
#
# Username or login name
# Encrypted password
# User ID
# Group ID
# User description
# User’s home directory
# User’s login shell

# Ejemplo con algunas líneas
# invscout:*:200:1::/var/adm/invscout:/usr/bin/ksh
# nuucp:*:6:5:uucp login user:/var/spool/uucppublic:/usr/sbin/uucp/uucico
# daemon:x:2:2:daemon:/sbin:/sbin/nologin
# root:x:0:0:root:/root:/bin/bash
# meera:x:502:502:Meera Yadav:/home/meera:/bin/bash

# Para este este ejemplo utilizaré el fichero "ejemplo_passwd" que me descargué...

from collections import Counter

file = './ejemplo_passwd'   # es un ejemplo que descargué...
lista_de_shells = []

with open(file) as f:
    for line in f:
        # Imprimimos la línea, ponemos end='' para que no ponga un newline adicional al que ya tiene la línea
        # print(line, end='')
        # Ahora vamos a hacer el split para tener los 7 campos... el último campo será el shell
        # Debería ser una lista con 7 elementos, el último el shell

        # creo que me faltaría poner que cuando empieza por # o \n continúe....

        campos_linea = line.split(sep=':')
        # Le quito si hubiera espacio y tb. el carácter de nueva línea que hay siempre (ya que es el último campo)
        campo_shell = campos_linea[-1].strip(' \n')
        if campo_shell:
            lista_de_shells.append(campo_shell)

    # Ya tenemos la lista con todos los shells (los que tengan algo, claro)
    # Ahora, con un counter, obtenemos todos ordenados por popularidad...
    shells_por_popularidad = Counter(lista_de_shells).most_common()

    print('Imprimiendo los shells encontrados, ordenados por popularidad...')
    for tupla in shells_por_popularidad:
        print(f'{tupla[0]} ---> utilizado {tupla[1]} veces')
