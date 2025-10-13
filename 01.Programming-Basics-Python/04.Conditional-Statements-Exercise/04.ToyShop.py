excursionPrice = float(input())
puzzlesCount = int(input())
dollsCount = int(input())
bearsCount = int(input())
minionsCount = int(input())
trucksCount = int(input())

puzzlePrice = 2.60
dollPrice = 3
bearPrice = 4.10
minionPrice = 8.20
truckPrice = 2

toysBill = (puzzlePrice * puzzlesCount) + (dollPrice * dollsCount) + (bearPrice * bearsCount) + (minionPrice * minionsCount) + (truckPrice * trucksCount)
toysCount = puzzlesCount + dollsCount + bearsCount + minionsCount + trucksCount

if toysCount >= 50:
    toysBill *= 0.75

shopRent = toysBill * 0.1
toysBill -= shopRent

if toysBill >= excursionPrice:
    print(f"Yes! {toysBill - excursionPrice:.2f} lv left.")
else:
    print(f"Not enough money! {excursionPrice - toysBill:.2f} lv needed.")
