fruit = input()
weekDay = input()
count = float(input())

price = 0

if weekDay in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if fruit == "banana":
        price = count * 2.50
    elif fruit == "apple":
        price = count * 1.20
    elif fruit == "orange":
        price = count * 0.85
    elif fruit == "grapefruit":
        price = count * 1.45
    elif fruit == "kiwi":
        price = count * 2.70
    elif fruit == "pineapple":
        price = count * 5.50
    elif fruit == "grapes":
        price = count * 3.85
    else:
        print("error")
elif weekDay in ["Saturday", "Sunday"]:
    if fruit == "banana":
        price = count * 2.70
    elif fruit == "apple":
        price = count * 1.25
    elif fruit == "orange":
        price = count * 0.90
    elif fruit == "grapefruit":
        price = count * 1.60
    elif fruit == "kiwi":
        price = count * 3.00
    elif fruit == "pineapple":
        price = count * 5.60
    elif fruit == "grapes":
        price = count * 4.20
    else:
        print("error")
else:
    print("error")

if price > 0:
    print(f"{price:.2f}")
