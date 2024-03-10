import re

password = "m38nk'is+klY@"

print(bool(not re.search(r"[A-Za-z0-9!-/]", password)))