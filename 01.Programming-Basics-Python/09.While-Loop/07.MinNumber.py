input_value = input()
min_number = float('inf')

while input_value != "Stop":
    current_number = int(input_value)
    if current_number < min_number:
        min_number = current_number
    input_value = input()

print(min_number)
