import operator
import pprint
from enum import Enum, IntEnum, auto
from typing import Tuple, List

# Enumaración definida por la API
Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
'''Equivalente a la enumeración definida utilizando la clase
class Nucleotide(IntEnum):
    A = auto() o A = 1
    C = auto() o C = 2
    G = auto() o G = 3
    T = auto() o T = 4 o el valor que quisiéramos
    '''


Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gen = List[Codon]

def str_to_gen(string):
    gen: Gen = []
    for i in range(0, len(string), 3):
        if i + 2 >= len(string):
            # significaría que el último codon no está completo
            return gen
        codon = (Nucleotide[string[i]], Nucleotide[string[i+1]], Nucleotide[string[i+2]])
        # codon = string[i], string[i+1], string[i+2]

        print(codon)
        gen.append(codon)
    return gen

# Búsqueda lineal de un codon en una secuencia genética

def gen_linear_contains(gene: Gen, key_codon= Codon) -> bool:
    # Búsqueda lineal...
    '''Esto es solo educativo, realmente basta con
    if codon in gene:
        return True
    else:
        return False
    '''
    for codon in gene:
        if codon == key_codon:
            return True
    return False


def gen_bin_contains(gene_sorted: Gen, key_codon= Codon) -> bool:
    """
     Búsqueda binaria... esto sólo lo podemos hacer si los datos están ordenados
    y conseguiremos orden O(lg n)
    Observar que en este caso los datos no están ordenados (la secuencia genética)
    y ordenarlos nos costaría O(n lg n) con lo que sería más rápido, simplemente
    realizar una búsqueda linea... EXCEPTO SI VAMOS A REALIZAR VARIAS BÚSQUEDAS EN ESOS DATOS...
    Supondremos que los codones están ordenados...
    """
    low = 0
    high = len(gene_sorted) - 1

    while low <= high:
        middle = (low + high) // 2
        if gene_sorted[middle] == key_codon:
            return True
        elif gene_sorted[middle] > key_codon:
            high = middle - 1
        else:
            low = middle + 1
    return False

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTTGGATTT"

genes = str_to_gen(gene_str)
print(genes)

acg_codon: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat_codon: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
print(1)
print(gen_linear_contains(genes, acg_codon))
# Equivalente a simplemente print(acg_codon in genes)
# True
print(2)
print(gen_linear_contains(genes, gat_codon))
# Equivalente a simplemente print(gat_codon in genes)
# False, observar que la secuencia GAT sí que ocurre, pero no en un codon...




my_sorted_gene: Gen = sorted(genes)
pprint.pprint(my_sorted_gene)
print(3)
print(gen_bin_contains(my_sorted_gene, acg_codon)) # True
print(4)
print(gen_bin_contains(my_sorted_gene, gat_codon))# False

