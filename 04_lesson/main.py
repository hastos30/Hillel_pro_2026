from product import Product
from order import Order
from customer import Customer

toy = Product("Мягкая игрушка", "Игрушки", 500, 10)
lego = Product("Конструктор", "Игрушки", 1000, 5)

order = Order()

order.add_product(toy)
order.add_product(lego)

print("Сумма заказа:", order.calculate_total_price())

customer = Customer("Виктор", "hastos30@gmail.com")

customer.add_order(order)

print(customer.name, "имеет заказов:", len(customer.orders))
