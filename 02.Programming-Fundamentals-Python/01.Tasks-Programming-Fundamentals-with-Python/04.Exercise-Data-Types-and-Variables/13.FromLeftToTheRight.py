lines_number = int(input())

for _ in range(lines_number):
    left_number, right_number = input().split()

    left = int(left_number)
    right = int(right_number)

    max_number = max(left, right)
    max_number = abs(max_number)

    digit_sum = 0
    while max_number > 0:
        digit_sum += max_number % 10
        max_number //= 10

    print(digit_sum)
