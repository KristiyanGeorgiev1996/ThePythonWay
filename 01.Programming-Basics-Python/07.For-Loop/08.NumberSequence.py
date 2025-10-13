n = int(input())

max_number = float('-inf')
min_number = float('inf')

for _ in range(n):
    current_num = int(input())
    if current_num > max_number:
        max_number = current_num
    if current_num < min_number:
        min_number = current_num

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
