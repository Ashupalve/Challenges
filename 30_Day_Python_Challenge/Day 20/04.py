# Q4. Write a program to implement a hash table from scratch (using separate chaining) with insert
# and search methods.

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    def _hash(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        idx = self._hash(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[idx].append([key, value])
    def search(self, key):
        idx = self._hash(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                return pair[1]
        return None
ht = HashTable()
ht.insert("name", "Aarav")
ht.insert("age", 22)
print(ht.search("name"))
print(ht.search("age"))