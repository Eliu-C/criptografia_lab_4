import unittest
from cifrado import cifrar, descifrar
from Crypto.Random import get_random_bytes

class TestCifrado(unittest.TestCase):
    
    def test_cifrado_descifrado_DES(self):
        clave = get_random_bytes(8)
        iv = get_random_bytes(8)
        texto = b"Texto de prueba"
        
        texto_cifrado = cifrar('DES', clave, iv, texto)
        texto_descifrado = descifrar('DES', clave, iv, texto_cifrado)
        
        self.assertEqual(texto, texto_descifrado)
    
    def test_cifrado_descifrado_AES(self):
        clave = get_random_bytes(32)
        iv = get_random_bytes(16)
        texto = b"Texto de prueba"
        
        texto_cifrado = cifrar('AES-256', clave, iv, texto)
        texto_descifrado = descifrar('AES-256', clave, iv, texto_cifrado)
        
        self.assertEqual(texto, texto_descifrado)

if __name__ == '__main__':
    unittest.main()
