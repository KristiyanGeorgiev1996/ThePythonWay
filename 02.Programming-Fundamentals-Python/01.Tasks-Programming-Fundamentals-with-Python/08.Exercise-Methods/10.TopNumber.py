number = int(input())

def has_odd_digit(num):
    while num > 0:
        if (num % 10) % 2 == 1:
            return True
        num //= 10
    return False

def is_digit_sum_divisible_by_8(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total % 8 == 0

for i in range(1, number + 1):
    if has_odd_digit(i) and is_digit_sum_divisible_by_8(i):
        print(i)
