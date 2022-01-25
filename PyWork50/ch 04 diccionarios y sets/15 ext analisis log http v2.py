# Lo hago de nuevo pero, después de ver la solución de Reuven pues...
# lo hago poniendo el código en una función y además utilizando la función split, es mucho mejor
from collections import defaultdict


def analiza_log_ip(filename):
    DATA = defaultdict(set)
    with open(filename) as log:
        for line in log:
            campos = line.split()  # Si nada, hace el split por espacios...
            IP = campos[0]
            codigo = campos[8]
            DATA[codigo].add(IP)

    return DATA


DATA = analiza_log_ip('mini-access-log.txt')
# Comprobación
for codigo, IPs in DATA.items():
    print(f'\nPara el código {codigo}, las ips grabadas han sido, sin repetir...\n')
    for IP in IPs:
        print('\t--> ', IP)

