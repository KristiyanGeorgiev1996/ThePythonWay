products = {}

while True:
    command = input()
    if command == "buy":
        break
    product_name, price_str, quantity_str = command.split()
    price = float(price_str)
    quantity = float(quantity_str)

    if product_name not in products:
        products[product_name] = {"price": price, "quantity": quantity}
    else:
        products[product_name]["quantity"] += quantity
        products[product_name]["price"] = price

for product, data in products.items():
    total_value = data["price"] * data["quantity"]
    print(f"{product} -> {total_value:.2f}")
