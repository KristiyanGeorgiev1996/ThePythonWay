number = float(input())

isValid = (100 <= number <= 200) or number == 0

if not isValid:
    print("invalid")
