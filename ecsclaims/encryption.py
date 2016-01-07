from Crypto import Random
from Crypto.Cipher import AES
import base64

# Para AES 128
# block size = 16
# Llave en hexadecimal, hay que convertir a bytes
# key = 'f74de1d77975e92a4061fe31d8fe0656'
# Modo = ECB
# Padding = PKCS5
# No utiliza IV

class AESCipher:
    def __init__(self, key, mode='hex'):
        self.bs = 16
        if mode == 'hex':
            self.key = key.decode('hex')
        else:
            self.key = key

    def decrypt(self, enc):
        aes = AES.new(self.key)
        return self.unpad(aes.decrypt(base64.b64decode(enc)))

    def encrypt(self, raw):
        aes = AES.new(self.key)
        return base64.b64encode(aes.encrypt(self.pad(raw)))

    def pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def unpad(self, s):
        return s[:-ord(s[len(s)-1:])]
