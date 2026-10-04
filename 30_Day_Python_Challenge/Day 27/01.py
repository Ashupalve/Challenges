# Q1. Write a program to build a simple in-memory key-value store class supporting set, get, delete,
# and expiry checks (using timestamps).

import time
class KeyValueStore:
    def __init__(self):
        self.store = {}
    def set(self, key, value, ttl=None):
        expire_at = time.time() + ttl if ttl else None
        self.store[key] = (value, expire_at)
    def get(self, key):
        if key not in self.store:
            return None
        value, expire_at = self.store[key]
        if expire_at and time.time() > expire_at:
            del self.store[key]
            return None
        return value
    def delete(self, key):
        self.store.pop(key, None)
kv = KeyValueStore()
kv.set("name", "Aarav")
print(kv.get("name"))
kv.delete("name")
print(kv.get("name"))