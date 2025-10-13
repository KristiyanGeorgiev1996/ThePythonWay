prime_nums_sum = 0
non_prime_nums_sum = 0

while True:
    input_value = input()
    if input_value == "stop":
        break

    number = int(input_value)
    if number < 0:
        print("Number is negative.")
        continue

    is_prime = True
    if number <= 1:
        is_prime = False
    elif number != 2 and number % 2 == 0:
        is_prime = False
    else:
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        prime_nums_sum += number
    else:
        non_prime_nums_sum += number

print(f"Sum of all prime numbers is: {prime_nums_sum}")
print(f"Sum of all non prime numbers is: {non_prime_nums_sum}")
