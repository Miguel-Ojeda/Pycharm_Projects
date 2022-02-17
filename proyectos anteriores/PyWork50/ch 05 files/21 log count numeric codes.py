'''
Open an HTTP server’s log file. (If you lack one, then you can read one from
me at http://mng.bz/vxxM.) Summarize how many requests resulted in numeric
response codes—202, 304, and so on.
'''
import pprint
from collections import defaultdict, Counter


def get_numeric_count(log_file):
    resultado = defaultdict(int)
    with open(log_file) as logs:
        for linea in logs:
            code = linea.split()[8]
            resultado[code] += 1

    return resultado

# Creo que no aporta nada utilziar un Counter... el counter está guay a la hora
# de crearse, pq nos crea el diccionario basandose en las veces que se repite algo...
def get_numeric_count_Reuven(log_file):
    resultado = Counter()
    with open(log_file) as logs:
        for linea in logs:
            code = linea.split()[8]
            resultado[code] += 1

    return resultado



log_file = 'files/mini-access-log.txt'
resultado = get_numeric_count(log_file)
pprint.pprint(resultado)
resultado_2 = get_numeric_count_Reuven(log_file)
pprint.pprint(resultado_2)



