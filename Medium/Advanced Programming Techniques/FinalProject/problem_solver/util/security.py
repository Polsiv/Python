#pylint: disable =C0114, R0801
import json
import binascii
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes 
from Crypto.Util.Padding import pad, unpad

class Cryptographer:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def save_keys_to_files(self):
        """save keys in .pem format"""
        keys_dir = 'keys'

        with open(os.path.join(keys_dir, "problem_solver_pk"), "wb") as private_file:
            private_file.write(self.private_key.export_key())

        with open(os.path.join(keys_dir, "problem_solver_pvk"), "wb") as public_file:
            public_file.write(self.public_key.export_key())

    def generate_keys(self):
        """Generate both private and public key for data server"""
        self.private_key = RSA.generate(1024)
        self.public_key = self.private_key.publickey()
        self.save_keys_to_files()

    def encrypt(self, data, data_server_pk):
        """Encrypts the data"""

        receiver_public_key = RSA.import_key(data_server_pk)

        #generate random 16-byte
        aes_key = get_random_bytes(16)

        #initialize the AES cipher in CBC mode with the generated AES key
        cipher_aes = AES.new(aes_key, AES.MODE_CBC)
        iv = cipher_aes.iv

        #encrypt the data with AES and pad it to match the block size
        encrypted_data = cipher_aes.encrypt(pad(data, AES.block_size))

        #initialize RSA cipher with data server's public key
        cipher_rsa = PKCS1_OAEP.new(receiver_public_key)

        #encrypt the AES key with RSA
        encrypted_aes_key = cipher_rsa.encrypt(aes_key)

        #return a dictionary containing the encrypted AES key, encrypted data, and IV
        return {
            'encrypted_aes_key': binascii.hexlify(encrypted_aes_key).decode(),
            'encrypted_data': binascii.hexlify(encrypted_data).decode(),
            'iv': binascii.hexlify(iv).decode()
        }

    def decrypt(self, encrypted):
        """decrypts the data"""
        #hex string convertion (converting the hex strings back to bytes)
        encrypted_aes_key = binascii.unhexlify(encrypted['encrypted_aes_key'])
        encrypted_data = binascii.unhexlify(encrypted['encrypted_data'])
        iv = binascii.unhexlify(encrypted['iv'])

        #initialize the RSA cipher with the private key
        cipher_rsa = PKCS1_OAEP.new(self.private_key)

        #decrypt the AES key using the RSA cipher
        decrypted_aes_key = cipher_rsa.decrypt(encrypted_aes_key)

        #initialize the AES cipher in CBC mode with the decrypted AES key and IV.
        cipher_aes = AES.new(decrypted_aes_key, AES.MODE_CBC, iv)

        #decrypt the encrypted data using the AES cipher and unpad it.
        decrypted_data = unpad(cipher_aes.decrypt(encrypted_data), AES.block_size)

        #decode decrypted bytes to a JSON string and then parse it back to a python dictionary.
        decrypted_json = decrypted_data.decode()
        return json.loads(decrypted_json)
