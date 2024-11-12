from Crypto.Random import get_random_bytes

def solicitar_datos():
    algoritmo = input("Seleccione el algoritmo (DES, 3DES, AES-256): ").strip().upper()
    clave = input("Ingrese la clave: ").encode('utf-8')
    iv = input("Ingrese el Vector de Inicialización (IV): ").encode('utf-8')
    texto = input("Ingrese el texto a cifrar: ").encode('utf-8')
    return algoritmo, clave, iv, texto

def ajustar_clave(clave, algoritmo):
    if algoritmo == 'DES':
        tamaño_clave = 8
    elif algoritmo == 'AES-256':
        tamaño_clave = 32
    elif algoritmo == '3DES':
        tamaño_clave = 24
    else:
        raise ValueError("Algoritmo no soportado")
    
    if len(clave) < tamaño_clave:
        clave = clave.ljust(tamaño_clave, b'\0')
    elif len(clave) > tamaño_clave:
        clave = clave[:tamaño_clave]
    
    return clave
