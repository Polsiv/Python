import os

#returns the path for the current directory
current_directory = os.getcwd()
print(f"\n[+]current_directory: {current_directory}")

#list all resources

files = os.listdir(current_directory)

for file in files:
    print(file)

if not os.path.exists("Nested directory"): 
    os.mkdir("Nested directory")

    print("Directory: Nested directory")

    files = os.listdir(current_directory)
    for file in files:
        print(file)

print(f"\n[+] Does the 'Nested directory' exist: {os.path.exists('Nested directory')}")
print(f"\n[+] Does the 'my_file.txt' exist: {os.path.exists('file.txt')}")

#returns that environment variable
get_env = os.getenv("HOMEPATH")
print(f"\n[+] Value of HOMEPATH: {get_env}")