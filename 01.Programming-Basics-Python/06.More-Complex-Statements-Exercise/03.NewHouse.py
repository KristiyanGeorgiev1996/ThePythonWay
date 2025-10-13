typeFlowers = input()
flowersCount = int(input())
budget = float(input())

rosePrice = 5
dahliaPrice = 3.80
tulipPrice = 2.80
narcissPrice = 3
gladiolaPrice = 2.50

bill = 0

if typeFlowers == "Roses":
    bill = flowersCount * rosePrice
    if flowersCount > 80:
        bill *= 0.9
elif typeFlowers == "Dahlias":
    bill = flowersCount * dahliaPrice
    if flowersCount > 90:
        bill *= 0.85
elif typeFlowers == "Tulips":
    bill = flowersCount * tulipPrice
    if flowersCount > 80:
        bill *= 0.85
elif typeFlowers == "Narcissus":
    bill = flowersCount * narcissPrice
    if flowersCount < 120:
        bill *= 1.15
elif typeFlowers == "Gladiolus":
    bill = flowersCount * gladiolaPrice
    if flowersCount < 80:
        bill *= 1.2

if bill <= budget:
    remainingMoney = budget - bill
    print(f"Hey, you have a great garden with {flowersCount} {typeFlowers} and {remainingMoney:.2f} leva left.")
else:
    neededMoney = bill - budget
    print(f"Not enough money, you need {neededMoney:.2f} leva more.")
