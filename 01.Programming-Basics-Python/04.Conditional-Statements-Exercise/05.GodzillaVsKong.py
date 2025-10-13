movieBudget = float(input())
backgroundActorsCount = int(input())
backgroundActorClothingPrice = float(input())

decorPrice = movieBudget * 0.1
backgroundActorsClothingSum = backgroundActorsCount * backgroundActorClothingPrice

if backgroundActorsCount > 150:
    backgroundActorsClothingSum *= 0.9

totalCost = decorPrice + backgroundActorsClothingSum

if totalCost > movieBudget:
    print("Not enough money!")
    print(f"Wingard needs {totalCost - movieBudget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {movieBudget - totalCost:.2f} leva left.")
