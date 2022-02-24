"""
You saw how the simple int type in Python can be used to represent a bit string.
Write an ergonomic wrapper around int that can be used generically as a
sequence of bits (make it iterable and implement __getitem__()).
Reimplement CompressedGene, using the wrapper.
"""


class Entero_Con_Nucleotidos:
    def __init__(self, valor_inicial: int) -> None:
        self.valor = valor_inicial

    def __getitem__(self, numero_nucleotido) -> bool:
        """Este metodo nos retorna el valor del bit indicado"""
        return (self.valor >> (2 * numero_nucleotido)) & 0b11

    def __setitem__(self, numero_nucleotido, value) -> None:
        """Este método nos retorna el valor del bit indicado"""
        self.valor |= (0b11 & value)  << (2 * numero_nucleotido)

    def __iter__(self):
        return self.nucleotidos()

    def nucleotidos(self):
        for index in range((self.valor.bit_length() + 1) // 2):
            yield self[index]

    def __repr__(self):
        return str(self.valor)


class Compressed_Gene:
    def __init__(self, secuencia_genetica: str) -> None:
        self._compress(secuencia_genetica)

    def _compress(self, secuencia_genetica: str) -> None:
        """
        Este método lo ponemos con _ para que no se llame desde fuera
        Lo que hace es, para una secuencia de nucleótidos, codificarlo
        como una secuencia de bits... como hemos puesto al princpio de
        este documento"""
        # Inicialmente metemos un 1 en la información genética
        # para que, si fuera por ejemplo AAAAA, no valiera 0 sino 1_00_00_00_00_00
        self.gene_bits: int = 1
        for nucleotido in secuencia_genetica.upper():
            # Hacemos hueco para el nuevo nucleótido que vamos a agregar al campo de bits...
            self.gene_bits <<= 2
            if nucleotido == 'A':
                self.gene_bits |= 0b00
                # esto se podría omitir, claro, pq no hace nada
            elif nucleotido == 'C':
                self.gene_bits |= 0b01
            elif nucleotido == 'G':
                self.gene_bits |= 0b10
            elif nucleotido == 'T':
                self.gene_bits |= 0b11
            else:
                raise ValueError(f'Nucleótido no válido {nucleotido}!')

    # def decompress(self) -> str:
    #     # Este método nos devuelve la cadena de nucleótidos
    #     numero_bases = (self.gene_bits.bit_length() - 1) // 2  # quitamos el elemento centinela
    #     secuencia_genetica = ''
    #     copia_gene_bits = self.gene_bits
    #     for i in range(numero_bases):
    #         # Obtenemos el nucleótido representado por los 2 últimos bits (el último añadido)
    #         bits = copia_gene_bits & 0b11
    #         if bits == 0b00:
    #             secuencia_genetica += 'A'
    #         elif bits == 0b01:
    #             secuencia_genetica += 'C'
    #         elif bits == 0b10:
    #             secuencia_genetica += 'G'
    #         else: # bits == 0b11:
    #             secuencia_genetica += 'T'
    #         # Ahora desplazo 2 bits a la derecha para poder luego acceder a los siguientes
    #         copia_gene_bits >>= 2
    #
    #     # Cuidado, ahora en secuencia genética están los nucleótidos, pero en orden inverso!!
    #     return secuencia_genetica[::-1]
    #
    # def __repr__(self):
    #     return self.decompress()


if __name__ == '__main__':
    n = Entero_Con_Nucleotidos(0)
    # for i in n:
    #     print(i)

    n[1] = 3
    n[3] = 3
    print(n.valor)

    # print(0, n[0])
    # print(1, n[1])
    # print(2, n[2])
    # print(3, n[3])
    # print(4, n[4])
    # print(5, n[5])
    # print(6, n[6])
    # print(7, n[7])

    # genes = 'TACGTACAA'
    # gen_bits = Compressed_Gene(genes)
    # print(f'{gen_bits.gene_bits:b}')
    # '''
    # >>> 1110001101100010000
    # Si lo parto queda 1(Sentinel)_11(T)_00(A)_01(C)_10(G)_11(T)_00(A)_01(C)_00(A)_00(A)
    # O sea, se han guardado bien los bits... la compresión
    # '''
    # # veamos ahora si descomprime bien...
    # print(gen_bits)
    # # >>> TACGTACAA  # CORRECTO!!!!
    #
    # # Otra prueba, cogida del libro!!!
    # from sys import getsizeof
    # print('---------------------------\nPrueba 2:')
    # original = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    # print(f'El tamaño de la información genética sin comprimir es de {getsizeof(original)} bytes')
    # genetic_bits = Compressed_Gene(original)
    # print(f'El tamaño de la información comprimida es de {getsizeof(genetic_bits)} bytes')
    # print(genetic_bits)
    # if genetic_bits.decompress() == original:
    #     print('La información está bien codificada')
