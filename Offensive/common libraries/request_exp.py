#! /usr/bin/env python3
import requests

response = requests.get("https://httpbin.org/get")

print(response.status_code)

# sourcecode

with open("response.html", "w") as f:
    f.write(response.text)
print(response.text)


