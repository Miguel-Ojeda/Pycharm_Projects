"""
Ahora hacemos lo mismo pero con diccionario; el código es más corto, sencillo,
pero en un diccionario, aunque el acceso es O(1) realmente no es tan eficiente
pq hay q evaluar hash de las keys.. etc....
"""

class Compressed_Gene_2:
    base = {'A': 0b00, 'C': 0b01, 'G': 0b10, 'T': 0b11}
    base_keys_list = list(base.keys())
    base_values_list = list(base.values())

    def __init__(self, secuencia_genetica: str) -> None:
        self._compress(secuencia_genetica)

    def _compress(self, secuencia_genetica: str) -> None:
        # Inicialmente metemos un 1 en la información genética
        # para que, si fuera por ejemplo AAAAA, no valiera 0 sino 1_00_00_00_00_00
        self.gene_bits: int = 1
        for nucleotido in secuencia_genetica.upper():
            # Hacemos hueco para el nuevo nucleótido que vamos a agregar al campo de bits...
            self.gene_bits <<= 2
            if nucleotido in Compressed_Gene_2.base:
                self.gene_bits |= Compressed_Gene_2.base[nucleotido]
            else:
                raise ValueError(f'Nucleótido no válido {nucleotido}!')

    def decompress(self) -> str:
        # Este método nos devuelve la cadena de nucleótidos
        numero_bases = (self.gene_bits.bit_length() - 1) // 2  # quitamos el elemento centinela
        secuencia_genetica = ''
        copia_gene_bits = self.gene_bits
        for i in range(numero_bases):
            # Obtenemos el nucleótido representado por los 2 últimos bits (el último añadido)
            bits = copia_gene_bits & 0b11
            index = Compressed_Gene_2.base_values_list.index(bits)
            secuencia_genetica += Compressed_Gene_2.base_keys_list[index]
            # Ahora desplazo 2 bits a la derecha para poder luego acceder a los siguientes
            copia_gene_bits >>= 2

        # Cuidado, ahora en secuencia genética están los nucleótidos, pero en orden inverso!!
        return secuencia_genetica[::-1]

    def __repr__(self):
        return self.decompress()





if __name__ == '__main__':
    genes = 'TACGTACAA'
    gen_bits = Compressed_Gene_2(genes)
    print(f'{gen_bits.gene_bits:b}')
    '''
    >>> 1110001101100010000
    Si lo parto queda 1(Sentinel)_11(T)_00(A)_01(C)_10(G)_11(T)_00(A)_01(C)_00(A)_00(A)
    O sea, se han guardado bien los bits... la compresión
    '''

    # veamos ahora si descomprime bien...
    print(gen_bits)
    # >>> TACGTACAA  # CORRECTO!!!!


    # Otra prueba, cogida del libro!!!
    from sys import getsizeof
    print('---------------------------\nPrueba 2:')
    original = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print(f'El tamaño de la información genética sin comprimir es de {getsizeof(original)} bytes')
    genetic_bits = Compressed_Gene_2(original)
    print(f'El tamaño de la información comprimida es de {getsizeof(genetic_bits)} bytes')
    print(genetic_bits)
    if genetic_bits.decompress() == original:
        print('La información está bien codificada')




