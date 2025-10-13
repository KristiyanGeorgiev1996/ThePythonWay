number = int(input())
number_copy = number
fact_sum = 0

while number_copy > 0:
    digit = number_copy % 10
    number_copy //= 10

    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i

    fact_sum += factorial

is_strong_number = "yes" if number == fact_sum else "no"
print(is_strong_number)
