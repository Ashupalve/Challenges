# Q3. Write a program using a context manager (class-based, with __enter__ and __exit__) to
# manage file writing.

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
with FileManager("test.txt", "w") as f:
    f.write("Using a custom context manager!")
print("File written successfully")