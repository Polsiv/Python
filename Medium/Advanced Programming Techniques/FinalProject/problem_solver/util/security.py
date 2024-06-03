import rsa
import os
import base64

def generate_key_pair():
    public_key, private_key = rsa.newkeys(1024)

    with open("public.pem", "wb") as f:
        f.write(public_key.save_pkcs1("PEM"))

    with open("private.pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM"))


def encrypt_data(data, key):

    public_key = rsa.PublicKey.load_pkcs1(base64.b64decode(key.encode()))
    encrypted_data = rsa.encrypt(data, public_key)
    encoded_data = base64.b64encode(encrypted_data).decode('utf-8')
    return encoded_data

def get_pk():
    key_path = os.path.join(os.path.dirname(__file__), 'keys', 'public.pem')
    with open(key_path, "rb") as f:        
        pk = f.read()
    return base64.b64encode(pk).decode('utf-8')


