class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def get_value(self):
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_inventory_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.get_value()
        return total_value

    def display_inventory(self):
        for product in self.products:
            print(product)


if __name__ == "__main__":
    product1 = Product(1, "Laptop", 1000, 5)
    product2 = Product(2, "Smartphone", 500, 10)
    product3 = Product(3, "Tablet", 300, 8)

    inventory = Inventory()

    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product3)

    print("Inventory:")
    inventory.display_inventory()

    total_value = inventory.calculate_inventory_value()
    print(f"\nTotal Inventory Value: ${total_value}")
