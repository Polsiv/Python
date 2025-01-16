#!/usr/bin/env python3

import multiprocessing as mult
import time
import requests

def task(num_task):
    print(f"Initializing Task {num_task}")
    time.sleep(2)
    print(f"Ending Task {num_task}")

process1 = mult.Process(target = task, args = (1,))
process2 = mult.Process(target = task, args = (2,))

process1.start()
process2.start()

process1.join()
process2.join()

# Example

def request(url):
    r = requests.get(url)
    print(f"{len(r.content)} bytes")

domains = [ 
    "https://google.es", "https://hack4u.io",
    "https://youtube.com",
    "https://github.com/polsiv"
]

start = time.time()
processes = []

for i in domains:
    process = mult.Process(target = request, args = (i,))
    process.start()
    processes.append(process)


for i in processes:
    i.join()

end = time.time()

print("Took:", end - start)
