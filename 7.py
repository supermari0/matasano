import base64
from Crypto.Cipher.AES import AESCipher

KEY = 'YELLOW SUBMARINE'

if __name__ == '__main__':
    cipher = AESCipher(KEY)
    with open('7.txt', 'r') as f:
        ctext = base64.b64decode(f.read())
    print(cipher.decrypt(ctext))
