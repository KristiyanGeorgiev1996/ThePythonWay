projectionType = input()
rowsCount = int(input())
colsCount = int(input())

premierePrice = 12
normalPrice = 7.5
discountPrice = 5

income = 0

if projectionType == "Premiere":
    income = rowsCount * colsCount * premierePrice
elif projectionType == "Normal":
    income = rowsCount * colsCount * normalPrice
elif projectionType == "Discount":
    income = rowsCount * colsCount * discountPrice

print(f"{income:.2f} leva")
