budget = float(input())
season = input()
fishersCount = int(input())

rent = 0

if season == "Spring":
    rent = 3000
elif season in ["Summer", "Autumn"]:
    rent = 4200
elif season == "Winter":
    rent = 2600

if fishersCount <= 6:
    bill = rent * 0.9
elif 7 <= fishersCount <= 11:
    bill = rent * 0.85
else:
    bill = rent * 0.75

if fishersCount % 2 == 0 and season != "Autumn":
    bill *= 0.95

if bill <= budget:
    remainingMoney = budget - bill
    print(f"Yes! You have {remainingMoney:.2f} leva left.")
else:
    neededMoney = bill - budget
    print(f"Not enough money! You need {neededMoney:.2f} leva.")
