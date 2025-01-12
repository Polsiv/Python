import sys

# 0: references the script
print(f"\n[+] Script name: {sys.argv[0]}")

print(f"\n[+] Total of arguments passed to the program: {len(sys.argv)} ")

print(f"\n[+] Displaying first argument: {sys.argv[1]}")
print(f"\n[+] Displaying second argument: {sys.argv[2]}")
print(f"\n[+] Displaying all arguments: {", ".join(sys.argv)}")

#path hijacking
print(f"\n[+] Displaying Python path: \n")
for element in sys.path:
    print(element)

print("\n [+] Closing the program with an status code 1 (not successful)")
sys.exit(1)