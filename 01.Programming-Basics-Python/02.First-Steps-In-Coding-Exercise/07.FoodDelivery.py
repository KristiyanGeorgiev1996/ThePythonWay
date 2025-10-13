chickenMenuPrice = 10.35
fishMenuPrice = 12.40
vegetarianMenuPrice = 8.15

chickenMenusCount = int(input())
fishMenusCount = int(input())
vegetarianMenusCount = int(input())

bill = chickenMenuPrice * chickenMenusCount + fishMenuPrice * fishMenusCount + vegetarianMenuPrice * vegetarianMenusCount
dessertPrice = bill * 0.2
finalBill = bill + dessertPrice + 2.50

print(finalBill)
