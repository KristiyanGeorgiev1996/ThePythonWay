number = float(input())

isInRange = -100 <= number <= 100 and number != 0

if isInRange:
    print("Yes")
else:
    print("No")
