number = abs(int(input()))
odd = 0
even = 0

while number > 0:
    last_digit = number % 10
    if last_digit % 2 == 0:
        even += last_digit
    else:
        odd += last_digit
    number //= 10

result = even * odd
print(result)
