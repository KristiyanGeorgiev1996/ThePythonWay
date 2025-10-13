input_value = input()
max_number = float('-inf')

while input_value != "Stop":
    current_number = int(input_value)
    if current_number > max_number:
        max_number = current_number
    input_value = input()

print(max_number)
