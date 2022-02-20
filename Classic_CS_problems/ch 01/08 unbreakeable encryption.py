# One-time pad encryption

from secrets import token_bytes


def random_key(length: int) -> int:
    """Creamos una clave de la longitud dada
    Primero obtenemos los bytes que hagan falta al azar,
    y luego con esos bytes formamos un entero, que va a ser la clave devuelta
    La clave se va a utilizar para realizar un XOR con los datos que queremos encriptar
    También nos servirá para desencriptar luego"""
    byte_string = token_bytes(length)
    '''
    es un objeto de la clase bytes
    Ahora creamos un entero utilizando esos bytes
    Consideramos que el primer byte es el más significativo (big endian)
    '''
    return int.from_bytes(byte_string, 'big')


def encrypt(mensaje: str) -> tuple:
    """La función coge la cadena, la transforma en entero, genero un número al azar
    con su misma longitud que se utilziar para hacer el XOR
    El resultado es el mensaje encriptado con XOR y la clave"""

    mensaje_bytes = mensaje.encode(encoding='utf-8')
    clave_a_utilizar: int = random_key(len(mensaje_bytes))
    mensaje_int = int.from_bytes(mensaje_bytes, 'big')
    # Da igual si ponemos big o little, lo importante es
    # usar lo mismo en ambas funciones encrypt y decrypt
    mensaje_cifrado = mensaje_int ^ clave_a_utilizar   # REALIZAMOS EL XOR
    return mensaje_cifrado, clave_a_utilizar


def decrypt(mensaje_cifrado: int, clave_a_utilizar: int) -> str:
    mensaje_original = mensaje_cifrado ^ clave_a_utilizar
    mensaje_original_bytes = mensaje_original.to_bytes((mensaje_original.bit_length() + 7) // 8, 'big')
    '''
    Importante, a lo mejor el último byte, el mayor del número, no utiliza todos los bits...
    Supongamos que el número es de 8 bytes, pero del último sólo utiliza un bit,
    entonces la longitud en bits sería de 57 bits, con lo que al hacer la división entera por 8
    no obtendríamos el número correcto de bytes, sino tendríamos 7 bytes...
    Por es sumamos 7, para, en el peor de los casos, (aquel en el que el último byte sólo utiliza un bit)
    nos dé bien el número de bytes
    '''

    mensaje_original_string = mensaje_original_bytes.decode()
    return mensaje_original_string











if __name__ == '__main__':
    key1, key2 = encrypt("Esto es un mensaje secreto 125432")
    print(key1, key2)
    result: str = decrypt(key1, key2)
    print(result)




