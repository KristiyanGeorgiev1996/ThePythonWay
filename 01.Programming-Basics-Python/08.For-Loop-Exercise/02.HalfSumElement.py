n = int(input())

total_sum = 0
max_number = float('-inf')

for _ in range(n):
    current_number = int(input())
    total_sum += current_number
    if current_number > max_number:
        max_number = current_number

sum_without_max = total_sum - max_number

if max_number == sum_without_max:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    diff = abs(max_number - sum_without_max)
    print("No")
    print(f"Diff = {diff}")
