#!/usr/bin/env python3
import threading 
import time 
import requests
# Problem using no threads, sequencial approach 

def task(num_task):
    print(f"Initializing Task {num_task}")
    time.sleep(2)
    print(f"Ending Task {num_task}")

task(1)
task(2)

# Problem using threads

def task_thread(num_task):
    print(f"Initializing Thread {num_task}")
    time.sleep(2)
    print(f"Ending Thread {num_task}")

thread_1 = threading.Thread(target=task_thread, args=(1,))
thread_2 = threading.Thread(target=task_thread, args=(2,)) # args = function arguments

# Initializing threads

thread_1.start()
thread_2.start()

# Letting threads finish

thread_1.join()
thread_2.join()

# Example

def request(url):
    response = requests.get(url)
    print(f"[+] Lenght: {len(response.content)} bytes")

domains = [ 
    "https://google.es",
    "https://hack4u.io",
    "https://youtube.com",
    "https://github.com/polsiv"
]

start = time.time()

threads = []
for url in domains:
    thread = threading.Thread(target = request, args = (url,))
    thread.start()
    threads.append(thread)
    print(threads)

for thread in threads:
    thread.join()


end = time.time()

print(f"Took: {end - start}")
