from Crypto.Random import get_random_bytes

def ajustar_iv(iv, algoritmo):
    if algoritmo == 'AES-256':
        tamano_iv = 16
    else:
        tamano_iv = 8

    if len(iv) < tamano_iv:
        iv += get_random_bytes(tamano_iv - len(iv))
    elif len(iv) > tamano_iv:
        iv = iv[:tamano_iv]

    print(f"IV ajustado: {iv}")
    return iv
