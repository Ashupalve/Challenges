# Q3. Capstone: Build a simple `Inventory Management System` that tracks stock levels, supports
# restocking, selling, and raises a custom exception on insufficient stock.

class InsufficientStockError(Exception):
    pass
class Inventory:
    def __init__(self):
        self.stock = {}
    def restock(self, item, qty):
        self.stock[item] = self.stock.get(item, 0) + qty
        print(f"Restocked {qty} of {item}. Total: {self.stock[item]}")
    def sell(self, item, qty):
        if self.stock.get(item, 0) < qty:
            raise InsufficientStockError(f"Not enough stock for {item}")
        self.stock[item] -= qty
        print(f"Sold {qty} of {item}. Remaining: {self.stock[item]}")
inv = Inventory()
inv.restock("Laptop", 10)
inv.sell("Laptop", 4)
try:
    inv.sell("Laptop", 20)
except InsufficientStockError as e:
    print("Error:", e)