import re

class Order:
    def __init__(self, customer, product, count, price):
        self.customer = customer
        self.product = product
        self.count = count
        self.price = price

    @property
    def total_price(self):
        return self.count * self.price

orders_input = [
    "%George%<Pizza>|2|10.50$",
    "%Peter%<Burger>|1|5.00$",
    "end of shift"
]

total_income = 0
pattern = re.compile(r'%([A-Z][a-z]+)%[^|$%.]*<(\w+)>[^|$%.]*\|(\d+)\|[^|$%.]*?(\d+(?:\.\d+)?)\$')

for command in orders_input:
    if command == "end of shift":
        break

    match = pattern.search(command)
    if not match:
        continue

    order = Order(match.group(1), match.group(2), int(match.group(3)), float(match.group(4)))
    total_income += order.total_price
    print(f"{order.customer}: {order.product} - {order.total_price:.2f}")

print(f"Total income: {total_income:.2f}")
