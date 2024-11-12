from cifrado import cifrar, descifrar
from utils import solicitar_datos, ajustar_clave
from ajustes import ajustar_iv

def main():
    algoritmo, clave, iv, texto = solicitar_datos()
    clave_ajustada = ajustar_clave(clave, algoritmo)
    iv_ajustado = ajustar_iv(iv)
    
    texto_cifrado = cifrar(algoritmo, clave_ajustada, iv, texto)
    print("Texto cifrado:", texto_cifrado)
    
    texto_descifrado = descifrar(algoritmo, clave_ajustada, iv_ajustado, texto_cifrado)
    print("Texto descifrado:", texto_descifrado.decode('utf-8'))

if __name__ == "__main__":
    main()
