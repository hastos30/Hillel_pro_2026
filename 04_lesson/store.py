import json

from product import Product
from customer import Customer
from order import Order


class Store:

    def __init__(self):
        self.products = []
        self.customers = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только Product")

        self.products.append(product)

    def add_customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Можно добавить только Customer")

        self.customers.append(customer)

    def save_to_files(self):
        products_data = []

        for product in self.products:
            products_data.append(
                {
                    "name": product.name,
                    "category": product.category,
                    "price": product.price,
                    "quantity": product.quantity,
                }
            )

        with open("04_lesson/data/products.json", "w", encoding="utf-8") as file:

            json.dump(products_data, file, indent=4, ensure_ascii=False)

        customers_data = []

        for customer in self.customers:
            customers_data.append(
                {"name": customer.name, "email": customer.email, "orders": []}
            )

        with open("04_lesson/data/customers.json", "w", encoding="utf-8") as file:

            json.dump(customers_data, file, indent=4, ensure_ascii=False)

    def load_from_files(self):
        with open("04_lesson/data/products.json", "r", encoding="utf-8") as file:

            products_data = json.load(file)

        self.products = []

        for product in products_data:

            new_product = Product(
                product["name"],
                product["category"],
                product["price"],
                product["quantity"],
            )

            self.products.append(new_product)

        with open("04_lesson/data/customers.json", "r", encoding="utf-8") as file:

            customers_data = json.load(file)

        self.customers = []

        for customer in customers_data:
            new_customer = Customer(customer["name"], customer["email"])
            self.customers.append(new_customer)
