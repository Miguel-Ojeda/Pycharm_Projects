'''
Read through a server (e.g., Apache or nginx) log file. What were the different
IP addresses that tried to access your server?
 Reading from that same server log, what response codes were returned to
users? The 200 code represents “OK,” but there are also 403, 404, and 500
errors. (Regular expressions aren’t required here but will probably help.)
'''
import pprint
# Para imprimir 'bonito' algunos objetos como diccionarios, listas, sets, .... no es necesario, claro

def extrae_sets_ips_codes_log(log_file):
    set_ips = set()
    set_codes = set()
    with open(log_file) as log_file:
        for line in log_file:
            # Hacemos el spliteado por campos separados por espacio...
            campos = line.split()
            # Analizando el log, vemos que la ip es justo el primer campo (índice 0)
            # y los códigos el octavo campo (lo vimos ya en el ejercicio 15)
            set_ips.add(campos[0])
            set_codes.add(campos[8])

    return set_ips, set_codes


log_file = 'files/mini-access-log.txt'
set_ips, set_codes = extrae_sets_ips_codes_log(log_file)
print(40*'--')
print('Los códigos de acceso devueltos por el HTTP server han sido:')
pprint.pprint(set_codes)
print(40*'--')
print('Las IPs que han accedido al HTTP server han sido:')
pprint.pprint(set_ips)

