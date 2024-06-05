from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes 
from Crypto.Util.Padding import pad, unpad
import json
import binascii
import os

class Cryptographer:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def save_keys_to_files(self):
        keys_dir = 'keys'
        
        with open(os.path.join(keys_dir, "problem_solver_pk"), "wb") as private_file:
            private_file.write(self.private_key.export_key())

        with open(os.path.join(keys_dir, "problem_solver_pvk"), "wb") as public_file:
            public_file.write(self.public_key.export_key())

    def generate_keys(self):
        self.private_key = RSA.generate(1024)
        self.public_key = self.private_key.publickey()
        self.save_keys_to_files()
    
    
    def encrypt(self, data, public_key_pem):

        receiver_public_key = RSA.import_key(public_key_pem)
        aes_key = get_random_bytes(16)
        cipher_aes = AES.new(aes_key, AES.MODE_CBC)
        iv = cipher_aes.iv

        encrypted_data = cipher_aes.encrypt(pad(data, AES.block_size))

        cipher_rsa = PKCS1_OAEP.new(receiver_public_key)
        encrypted_aes_key = cipher_rsa.encrypt(aes_key)

        return {
            'encrypted_aes_key': binascii.hexlify(encrypted_aes_key).decode(),
            'encrypted_data': binascii.hexlify(encrypted_data).decode(),
            'iv': binascii.hexlify(iv).decode()
        }

    def decrypt(self, encrypted):

        encrypted_aes_key = binascii.unhexlify(encrypted['encrypted_aes_key'])
        encrypted_data = binascii.unhexlify(encrypted['encrypted_data'])
        iv = binascii.unhexlify(encrypted['iv'])
        cipher_rsa = PKCS1_OAEP.new(self.private_key)
        decrypted_aes_key = cipher_rsa.decrypt(encrypted_aes_key)
        cipher_aes = AES.new(decrypted_aes_key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher_aes.decrypt(encrypted_data), AES.block_size)
        decrypted_json = decrypted_data.decode()

        return json.loads(decrypted_json)
    