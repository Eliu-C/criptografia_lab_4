from Crypto.Random import get_random_bytes

def ajustar_clave(clave, algoritmo):
    if algoritmo == 'DES':
        tamano = 8
    elif algoritmo == '3DES':
        tamano = 24
    elif algoritmo == 'AES-256':
        tamano = 32
    else:
        raise ValueError("Algoritmo no soportado")

    if len(clave) < tamano:
        clave += get_random_bytes(tamano - len(clave))
    elif len(clave) > tamano:
        clave = clave[:tamano]

    print(f"Clave ajustada ({algoritmo}):", clave)
    return clave
