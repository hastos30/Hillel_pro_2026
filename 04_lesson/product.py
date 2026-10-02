class Product:

    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def change_price(self, new_price):
        if new_price <= 0:
            raise ValueError("Цена должна быть больше 0")

        self.price = new_price

    def change_quantity(self, value):
        if self.quantity + value < 0:
            raise ValueError("Количество товара не может быть отрицательным")

        self.quantity += value
