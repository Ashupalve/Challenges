# Q4. Write a program to implement a simple concurrent web-scraper-style task simulation using
# threading and a thread-safe queue to collect results.
import threading
import queue
import time
def fetch_data(task_id, result_queue):
    time.sleep(0.1)
    result_queue.put(f"Result from task {task_id}")
result_queue = queue.Queue()
threads = []
for i in range(4):
    t = threading.Thread(target=fetch_data, args=(i, result_queue))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
results = []
while not result_queue.empty():
    results.append(result_queue.get())
print(sorted(results))