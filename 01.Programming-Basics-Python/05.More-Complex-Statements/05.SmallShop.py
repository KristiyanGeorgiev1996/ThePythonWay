product = input()
city = input()
quantity = float(input())

priceOfProduct = 0

if city == "Sofia":
    if product == "coffee":
        priceOfProduct = 0.50
    elif product == "water":
        priceOfProduct = 0.80
    elif product == "beer":
        priceOfProduct = 1.20
    elif product == "sweets":
        priceOfProduct = 1.45
    elif product == "peanuts":
        priceOfProduct = 1.60
elif city == "Plovdiv":
    if product == "coffee":
        priceOfProduct = 0.40
    elif product == "water":
        priceOfProduct = 0.70
    elif product == "beer":
        priceOfProduct = 1.15
    elif product == "sweets":
        priceOfProduct = 1.30
    elif product == "peanuts":
        priceOfProduct = 1.50
elif city == "Varna":
    if product == "coffee":
        priceOfProduct = 0.45
    elif product == "water":
        priceOfProduct = 0.70
    elif product == "beer":
        priceOfProduct = 1.10
    elif product == "sweets":
        priceOfProduct = 1.35
    elif product == "peanuts":
        priceOfProduct = 1.55

finalPrice = priceOfProduct * quantity
print(finalPrice)
