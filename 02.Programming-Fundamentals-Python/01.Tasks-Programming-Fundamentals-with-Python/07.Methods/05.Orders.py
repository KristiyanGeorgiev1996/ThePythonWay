product = input()
price = float(input())

def total_price_of_products(product, price):
    total_sum = 0
    if product == "coffee":
        total_sum = price * 1.50
    elif product == "water":
        total_sum = price * 1.00
    elif product == "coke":
        total_sum = price * 1.40
    elif product == "snacks":
        total_sum = price * 2.00
    print(f"{total_sum:.2f}")

total_price_of_products(product, price)
