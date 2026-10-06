# Q2. Write a program to implement a rate-limited task scheduler class that runs queued tasks with a
# maximum of N tasks processed per call.

from collections import deque
class TaskScheduler:
    def __init__(self, max_per_batch):
        self.queue = deque()
        self.max_per_batch = max_per_batch
    def add_task(self, task):
        self.queue.append(task)
    def run_batch(self):
        count = 0
        while self.queue and count < self.max_per_batch:
            task = self.queue.popleft()
            task()
            count += 1
        print(f"Processed {count} tasks, {len(self.queue)} remaining")
scheduler = TaskScheduler(2)
for i in range(1, 5):
    scheduler.add_task(lambda i=i: print(f"Running task {i}"))
scheduler.run_batch()
scheduler.run_batch()