number = int(input())
sum_of_number = 0

while number != 0:
    sum_of_number += number % 10
    number //= 10

print(sum_of_number)
