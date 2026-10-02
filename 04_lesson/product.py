class Product:

    def __init__(self, name, category, price, quantity):
        self.__name = name
        self.__category = category
        self.__price = price
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, (int, float)):
            raise TypeError(
                f"Error: type value {type(new_price)}! Only integer or float is accepted. "
            )
        if new_price <= 0:
            raise ValueError(f"Error: value {new_price} must be positive!")

        self.__price = new_price

    def set_price(self, new_price):
        if not isinstance(new_price, (int, float)):
            raise TypeError(
                f"Error: type value {type(new_price)}! Only integer or float is accepted. "
            )

        if new_price <= 0:
            raise ValueError(f"Error: value {new_price} must be positive!")

        self.__price = new_price

    def change_quantity(self, value):
        if not isinstance(value, int):
            raise TypeError(f"Error: type value {type(value)}! Only integer.")

        if self.__quantity + value < 0:
            raise ValueError(f"Error: value {value} unacceptable!")

        self.__quantity += value
