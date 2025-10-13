number = int(input())
divisor = 0

if number % 10 == 0:
    divisor = 10
elif number % 7 == 0:
    divisor = 7
elif number % 6 == 0:
    divisor = 6
elif number % 3 == 0:
    divisor = 3
elif number % 2 == 0:
    divisor = 2

if divisor != 0:
    print(f"The number is divisible by {divisor}")
else:
    print("Not divisible")
