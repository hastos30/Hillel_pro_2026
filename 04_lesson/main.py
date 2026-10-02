from store import Store

store = Store()

store.load_from_files()

print("Товары магазина:")

for product in store.products:
    print(product.name, "-", product.quantity, "шт.")

print()

print("Клиенты магазина:")

for customer in store.customers:
    print(customer.name, customer.email)

store.products[0].change_quantity(-2)
store.products[1].change_price(1200)

store.save_to_files()
