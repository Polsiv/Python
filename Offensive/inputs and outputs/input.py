from getpass import getpass

while True:
    try:
        name = input("[+] name?: ")
        age =   int(input("[+] Age?: "))
        password = getpass("[+] Enter your password: ")
        print(f"\n[+] Omg is {name} ur actual name! :O, AND {age} NO WAY, AND HERE'S yo Password!: {password}")
        break
    except ValueError:
        print("Wrong!")