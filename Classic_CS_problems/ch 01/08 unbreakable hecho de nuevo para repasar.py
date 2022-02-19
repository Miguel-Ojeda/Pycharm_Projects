from secrets import token_bytes


def get_random_key(length: int) -> int:
    bytes = token_bytes(length)
    return int.from_bytes(bytes, 'big')


def encrypt(mensaje_str: str) -> tuple:
    mensaje_bytes = mensaje_str.encode(encoding='utf-8')
    mensaje_int = int.from_bytes(mensaje_bytes, 'big')

    clave_int = get_random_key(len(mensaje_bytes))
    mensaje_cifrado_int = mensaje_int ^ clave_int
    return mensaje_cifrado_int, clave_int


def decrypt(mensaje_cifrado_int: int, clave_int: int) -> str:
    mensaje_original_int = mensaje_cifrado_int ^ clave_int
    bytes_necesarios = (mensaje_original_int.bit_length() + 7) // 8
    mensaje_original_bytes = mensaje_original_int.to_bytes(bytes_necesarios, 'big')
    mensaje_original_string = mensaje_original_bytes.decode(encoding='utf-8')
    return mensaje_original_string


if __name__ == '__main__':
    key1, key2 = encrypt("Esto es un mensaje secreto 125432")
    print(key1, key2)
    result: str = decrypt(key1, key2)
    print(result)