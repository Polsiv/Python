import rsa

def generate_key_pair(self):
    public_key, private_key = rsa.newkeys(1024)


    with open("keys/public.pem", "wb") as f:
        f.write(public_key.save_pkcs1("PEM"))

    
    with open("keys/private.pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM"))

def get_pk():
    with open("keys", "rb") as f:
        pk = f.read
    return pk