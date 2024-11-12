def main():
    algoritmo, clave, iv, texto = solicitar_datos()
    clave_ajustada = ajustar_clave(clave, algoritmo)
    
    texto_cifrado = cifrar(algoritmo, clave_ajustada, iv, texto)
    print("Texto cifrado:", texto_cifrado)
    
    texto_descifrado = descifrar(algoritmo, clave_ajustada, iv, texto_cifrado)
    print("Texto descifrado:", texto_descifrado.decode('utf-8'))

if __name__ == "__main__":
    main()
