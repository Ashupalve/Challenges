# Q3. Write a program to build a simple contact book using a dictionary that supports add, search,
# and delete operations.

class ContactBook:
    def __init__(self):
        self.contacts = {}
    def add(self, name, phone):
        self.contacts[name] = phone
        print(f"Added {name}")
    def search(self, name):
        print(self.contacts.get(name, "Contact not found"))
    def delete(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Deleted {name}")
        else:
            print("Contact not found")
book = ContactBook()
book.add("Aarav", "9876543210")
book.search("Aarav")
book.delete("Aarav")
book.search("Aarav")