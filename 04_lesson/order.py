from product import Product


class Order:

    def __init__(self):
        self.products = []
        self.total_price = 0

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объект Product")

        self.products.append(product)

    def calculate_total_price(self):
        self.total_price = 0

        for product in self.products:
            self.total_price += product.price

        return self.total_price
