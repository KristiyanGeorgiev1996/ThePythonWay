first_num = int(input())
second_num = int(input())

for current_num in range(first_num, second_num + 1):
    current_num_str = str(current_num)
    even_sum = 0
    odd_sum = 0

    for i, digit in enumerate(current_num_str):
        digit = int(digit)
        if i % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    if even_sum == odd_sum:
        print(current_num, end=" ")
