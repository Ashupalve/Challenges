# Q4. Write a program to implement a `LinkedList` class with methods to insert a node at the end
# and print the list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")
ll = LinkedList()
for val in [10, 20, 30]:
    ll.insert(val)
ll.display()