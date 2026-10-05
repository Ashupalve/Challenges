# Q1. Write a program to build a simple URL shortener that maps long URLs to short codes and can
# resolve them back, using a dictionary-backed class

import random
import string
class URLShortener:
    def __init__(self):
        self.url_map = {}
    def shorten(self, long_url):
        code = "".join(random.choices(string.ascii_letters, k=6))
        self.url_map[code] = long_url
        return code
    def resolve(self, code):
        return self.url_map.get(code, "URL not found")
shortener = URLShortener()
code = shortener.shorten("https://www.example.com/very/long/path")
print("Short code generated")
print(shortener.resolve(code))