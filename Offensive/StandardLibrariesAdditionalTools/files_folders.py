import os
import shutil

if os.path.exists("file.txt"):
    print("\n[+] File exists")
else:
    print("\n[+] doesn't exists")
    
    
if not os.path.exists("folder"):
    os.mkdir("folder")
    
    
if not os.path.exists("folder2/sub_folder"):
    os.makedirs("folder2/sub_folder")

print(f"\n[+] Listing all resources")
resources = os.listdir()

for resource in resources:
    print(resource)

if os.path.exists("folder"):
    print("Exists")

    os.rmdir("folder")
    shutil.rmtree("folder2", ignore_errors = True)

with open("file.txt", "a") as f:
    f.write("")

if os.path.exists("file.txt"):
    os.rename("file.txt", "file2.txt")    

if os.path.exists("file2.txt"):
    os.remove("file2.txt") 


if os.path.exists("/etc/passwd"):
    size = os.path.getsize("/etc/passwd")
    print(f"size of /etc/passwd: {size} bytes")


if os.path.exists("/etc/passwd"):
    src = "/etc/passwd"
    dst = "example/"
    shutil.copy(src, dst)

# ---------------------- Little Example --------------------


path = os.path.join("example", "file.txt")
print(path)
filename = os.path.basename(path)
dirname = os.path.dirname(path)
print("file name is:", filename)
print("dir name is:", dirname)

print("Using split so we can list all the routes", dirname)
file_folder = os.path.split(path)
for i in file_folder:
    print(i)