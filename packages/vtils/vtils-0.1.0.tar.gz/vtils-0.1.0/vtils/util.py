import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class Cipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha512(key.encode()).digest()
        self.key = self.key[0:AES.block_size]

    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        bytes_to_remove = ord(last_character)
        return plain_text[:-bytes_to_remove]

    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def get_version(self):
        return get_version()


class FileUtils(object):
    def __init__(self,key):
        self.cipher = Cipher(key)

    def encrypt_file(self, fpath, target):
        fr = open(fpath, 'r')
        fw = open(target, 'w')
        for line in fr.readlines():
            encrypted = self.cipher.encrypt(line)
            fw.write(encrypted)
            fw.write('\n')
        fr.close()
        fw.close()


    def decrypt_file(self, fpath, target):
        fr = open(fpath, 'r')
        fw = open(target, 'w')
        for line in fr.readlines():
            decrypted = self.cipher.decrypt(line)
            fw.write(decrypted)
        fr.close()
        fw.close()

    
def get_version():
    return 'Ver. 0.0.9'