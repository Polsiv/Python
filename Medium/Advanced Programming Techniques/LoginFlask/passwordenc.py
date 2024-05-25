import bcrypt

text = input("enter a text")

pwd = text.encode('UTF-8')
sal = bcrypt.gensalt()
encript = bcrypt.hashpw(pwd , sal)

print(encript)

what = b'$2b$12$BTA0Eu/KqMfmrunbSLj8teznftByK9AKJVZUMs1gANklmt2GaDOOq'



text2 = bytes(input("enter a text 2"), 'utf-8')

if bcrypt.checkpw(text2, what):
    print("correct")

else: print("password incorrect")