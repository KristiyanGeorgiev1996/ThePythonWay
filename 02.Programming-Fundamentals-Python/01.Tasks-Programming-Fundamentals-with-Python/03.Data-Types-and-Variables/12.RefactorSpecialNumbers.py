n = int(input())

for i in range(1, n + 1):
    current_number = i
    digit_sum = 0

    while current_number > 0:
        digit_sum += current_number % 10
        current_number //= 10

    is_special = digit_sum in (5, 7, 11)
    print(f"{i} -> {is_special}")
