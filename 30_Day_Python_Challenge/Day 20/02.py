# Q2. Write a program to find the height (max depth) of a Binary Search Tree.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
def height(node):
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))
root = None
for val in [50, 30, 70, 20, 40]:
    root = insert(root, val)
print("Height:", height(root))