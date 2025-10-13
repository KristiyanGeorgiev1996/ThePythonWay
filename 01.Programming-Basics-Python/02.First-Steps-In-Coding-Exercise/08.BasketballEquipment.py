yearBasketBallFee = float(input())

shoesPrice = yearBasketBallFee - (yearBasketBallFee * 0.4)
equipmentPrice = shoesPrice - (shoesPrice * 0.2)
basketBallPrice = equipmentPrice / 4
accessoriesPrice = basketBallPrice / 5

bill = yearBasketBallFee + shoesPrice + equipmentPrice + basketBallPrice + accessoriesPrice
print(bill)
