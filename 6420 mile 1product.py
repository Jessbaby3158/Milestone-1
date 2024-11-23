class Product:
    def __init__(self, product_id, name, price, is_available=True):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.is_available = is_available

    def create_product(self):
        self.is_available = True
        print(f"Product {self.name} created successfully.")

    def update_product(self, name=None, price=None):
        if name:
            self.name = name
        if price:
            self.price = price
        print(f"Product {self.product_id} updated successfully.")

    def suspend_product(self):
        self.is_available = False
        print(f"Product {self.name} suspended successfully.")

    def __str__(self):
        status = "Available" if self.is_available else "Suspended"
        return f"ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Status: {status}"
