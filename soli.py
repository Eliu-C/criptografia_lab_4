import os

def solicitar_datos():
    algoritmo = input("Seleccione el algoritmo (DES, 3DES, AES-256): ").strip().upper()
    clave = input("Ingrese la clave: ").encode('utf-8')
    iv = input("Ingrese el Vector de Inicialización (IV): ").encode('utf-8')
    texto = input("Ingrese el texto a cifrar: ").encode('utf-8')
    return algoritmo, clave, iv, texto