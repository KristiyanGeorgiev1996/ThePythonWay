number = float(input())

bonusPoints = 0

if number <= 100:
    bonusPoints = 5
elif number <= 1000:
    bonusPoints = number * 0.2
else:
    bonusPoints = number * 0.1

additionalBonusPoints = 0

if number % 2 == 0:
    additionalBonusPoints += 1
elif number % 10 == 5:
    additionalBonusPoints += 2

print(bonusPoints + additionalBonusPoints)
print(number + bonusPoints + additionalBonusPoints)
