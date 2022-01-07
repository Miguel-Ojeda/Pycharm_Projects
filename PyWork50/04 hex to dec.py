def mi_hex_output():
    decnum =0
    hexnum = input('Enter a hex number to convert: ')
    for index, char in enumerate(reversed(hexnum)):
        # faltan comprobaciones.... pero es solo para pensar...
        valor = int(char, 16)
        valor *= 16 ** index
        decnum += valor
    print(decnum)

def mi_bin_output():
    decnum = 0
    numero_binario = input('Introduce un número binario: ----> ')
    for index, bit in enumerate(reversed(numero_binario)):
        if bit not in ('0', '1'):
            print('Ufff, no es un número binario...')
            return
        if bit == '1':
            decnum += 2 ** index
    print(decnum)






while True:

    # mi_hex_output()
    mi_bin_output()