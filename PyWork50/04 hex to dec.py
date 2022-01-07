def mi_hex_output():
    decnum =0
    hexnum = input('Enter a hex number to convert: ')
    for index, char in enumerate(reversed(hexnum)):
        # faltan comprobaciones.... pero es solo para pensar...
        valor = int(char, 16)
        valor *= 16 ** index
        decnum += valor
    print(decnum)

def mi_hex_output_2():
    # Utilizaremos char y ordinal
    # Observar que los números son los dígitos son los caracteres unicode desde 48 hasta 57
    # Las letras van desde el 65 ('A') hasta 70 ('F')
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    # Pasamos la cadena a mayúsucla para mirar más fácil
    hexnum = hexnum.upper()
    for index, char in enumerate(reversed(hexnum)):
        # faltan comprobaciones.... pero es solo para pensar...
        if ord('A') <= ord(char) <= ord('F'):
            valor = ord(char) - ord('A') + 10
        elif ord('0') <= ord(char) <= ord('9'):
            valor = ord(char) - ord('0')
        else:
            print('No ha escrito un número hexadecimal... los caracteres válidos son: 0 .. 9 A...F')
            return

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
    # mi_bin_output()
    mi_hex_output_2()