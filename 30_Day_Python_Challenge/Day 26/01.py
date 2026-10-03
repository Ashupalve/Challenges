# Q1. Write a program to implement a simple LRU (Least Recently Used) Cache using OrderedDict.

from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
lru = LRUCache(2)
lru.put(1, "A")
lru.put(2, "B")
print(lru.get(1))
lru.put(3, "C")
print(lru.get(2))