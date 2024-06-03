import rsa

def generate_key_pair():
    public_key, private_key = rsa.newkeys(1024)

    with open("public.pem", "wb") as f:
        f.write(public_key.save_pkcs1("PEM"))

    
    with open("private.pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM"))


def encrypt_data( data, key):

    public_key = rsa.PublicKey.load_pkcs1(key.encode())

    encrypted_data = rsa.encrypt(data, public_key)

    return encrypted_data

def get_pk():
    with open("keys", "rb") as f:
        pk = f.read
    return pk

