from product import Product


class Order:

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError(
                f"Error: type value {type(product)}! Only obj class Product."
            )

        self.__products.append(product)

    def calculate_total_price(self):
        total_price = 0
        for product in self.__products:
            total_price += product.price

        return total_price
