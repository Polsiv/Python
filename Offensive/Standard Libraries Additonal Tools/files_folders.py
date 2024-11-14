import os

if os.path.exists("file.txt"):
    print("\n[+] File exists")
else:
    print("\n[+] doesn't exists")
    
    
if not os.path.exists("folder"):
    os.mkdir("folder")
    
    
if not os.path.exists("folder2/sub_folder"):
    os.mkdirs("folder2/sub_folder")