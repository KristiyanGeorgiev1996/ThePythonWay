numbers = list(map(float, input().split()))

for num in numbers:
    rounded_number = round(num)
    print(f"{num} => {rounded_number}")
