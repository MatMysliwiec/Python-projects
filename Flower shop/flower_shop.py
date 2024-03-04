class Flower:
    def __init__(self, name, color, price, stock):
        self.name = name
        self.color = color
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f"{self.color} {self.name} - ${self.price:.2f} per stem")

    def order_more(self, quantity):
        print(f"Ordering {quantity} more {self.color} {self.name} stems")
        self.stock += quantity


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower, quantity):
        if flower.stock >= quantity:
            self.flowers.extend([flower] * quantity)
            flower.stock -= quantity
            print(f"Added {quantity} {flower.color} {flower.name} stems to the bouquet.")
        else:
            print(f"Not enough {flower.color} {flower.name} to add to the bouquet.")

    def display_bouquet(self):
        print("Bouquet Composition:")
        for flower in self.flowers:
            flower.display_info()

    def calculate_price(self):
        return sum(flower.price for flower in self.flowers)


rose = Flower("Rose", "Red", 20.0, 44)
tulip = Flower("Tulip", "Yellow", 12.0, 21)
lily = Flower("Lily", "White", 15.5, 11)

bouquet = Bouquet()
bouquet.add_flower(rose, 3)
bouquet.add_flower(tulip, 5)
bouquet.add_flower(lily, 11)

bouquet.display_bouquet()

print(f"Total price for bouquet is {bouquet.calculate_price()}")
