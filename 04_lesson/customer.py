from order import Order


class Customer:

    def __init__(self, name, email):
        self.__name = name
        self.__email = email
        self.__orders = []

    def add_order(self, new_order):
        if not isinstance(new_order, Order):
            raise TypeError(
                "Error: type argument is not correct! Must be obj class Order"
            )

        self.__orders.append(new_order)
