from order import Order


class Customer:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self, order):
        if not isinstance(order, Order):
            raise TypeError("Можно добавить только объект Order")

        self.orders.append(order)
