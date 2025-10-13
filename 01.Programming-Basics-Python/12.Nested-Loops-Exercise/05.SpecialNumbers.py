n = int(input())

for current_num in range(1111, 10000):
    is_special = True
    current_num_str = str(current_num)

    for digit in current_num_str:
        digit = int(digit)
        if digit == 0 or n % digit != 0:
            is_special = False
            break

    if is_special:
        print(current_num, end=" ")
