nylonPrice = 1.50
paintPrice = 14.50
paintThinnerPrice = 5.00

nylonNeeded = int(input())
paintNeeded = float(input())
paintThinnerNeeded = int(input())
workingHours = int(input())

nylonSum = nylonPrice * (nylonNeeded + 2)
paintSum = paintPrice * (paintNeeded + paintNeeded * 0.1)
paintThinnerSum = paintThinnerPrice * paintThinnerNeeded
bagsPrice = 0.40

materialsPrice = paintSum + nylonSum + paintThinnerSum + bagsPrice
workMenPrice = workingHours * (materialsPrice * 0.3)

print(workMenPrice + materialsPrice)
