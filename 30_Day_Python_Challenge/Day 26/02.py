# Q2. Write a program to implement threading in Python to run two functions concurrently and print
# their outputs.

import threading
import time
def print_numbers():
    for i in range(1, 4):
        print("Number:", i)
        time.sleep(0.1)
def print_letters():
    for ch in "ABC":
        print("Letter:", ch)
        time.sleep(0.1)
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
t1.start()
t2.start()
t1.join()
t2.join()
print("Done")