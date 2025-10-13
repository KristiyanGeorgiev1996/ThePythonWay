n = int(input())
all_liters = 0

for _ in range(n):
    liters = int(input())
    if liters > 255:
        print("Insufficient capacity!")
    elif liters + all_liters <= 255:
        all_liters += liters
    else:
        print("Insufficient capacity!")

print(all_liters)
