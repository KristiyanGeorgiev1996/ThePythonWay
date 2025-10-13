coins = 0.0
command = input()

while command != "Start":
    coin = float(command)
    if coin in [0.1, 0.2, 0.5, 1, 2]:
        coins += coin
    else:
        print(f"Cannot accept {coin}")
    command = input()

product = input().lower()
while product != "end":
    if product == "nuts":
        if coins >= 2.0:
            print(f"Purchased {product}")
            coins -= 2.0
        else:
            print("Sorry, not enough money")
    elif product == "water":
        if coins >= 0.7:
            print(f"Purchased {product}")
            coins -= 0.7
        else:
            print("Sorry, not enough money")
    elif product == "crisps":
        if coins >= 1.5:
            print(f"Purchased {product}")
            coins -= 1.5
        else:
            print("Sorry, not enough money")
    elif product == "soda":
        if coins >= 0.8:
            print(f"Purchased {product}")
            coins -= 0.8
        else:
            print("Sorry, not enough money")
    elif product == "coke":
        if coins >= 1.0:
            print(f"Purchased {product}")
            coins -= 1.0
        else:
            print("Sorry, not enough money")
    else:
        print("Invalid product")
    product = input().lower()

print(f"Change: {coins:.2f}")
