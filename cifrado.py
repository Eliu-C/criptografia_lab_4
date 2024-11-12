from Crypto.Cipher import DES, AES, DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes   

def cifrar(algoritmo, clave, iv, texto):
    if algoritmo == 'DES':
        cipher = DES.new(clave, DES.MODE_CBC, iv)
        block_size = DES.block_size
    elif algoritmo == '3DES':
        cipher = DES3.new(clave, DES3.MODE_CBC, iv)
        block_size = DES3.block_size
    elif algoritmo == 'AES-256':
        cipher = AES.new(clave, AES.MODE_CBC, iv)
        block_size = AES.block_size
    else:
        raise ValueError("Algoritmo no soportado")

    texto_cifrado = cipher.encrypt(pad(texto, block_size))
    return texto_cifrado

def descifrar(algoritmo, clave, iv, texto_cifrado):
    if algoritmo == 'DES':
        cipher = DES.new(clave, DES.MODE_CBC, iv)
        block_size = DES.block_size
    elif algoritmo == '3DES':
        cipher = DES3.new(clave, DES3.MODE_CBC, iv)
        block_size = DES3.block_size
    elif algoritmo == 'AES-256':
        cipher = AES.new(clave, AES.MODE_CBC, iv)
        block_size = AES.block_size
    else:
        raise ValueError("Algoritmo no soportado")

    texto_descifrado = unpad(cipher.decrypt(texto_cifrado), block_size)
    return texto_descifrado
