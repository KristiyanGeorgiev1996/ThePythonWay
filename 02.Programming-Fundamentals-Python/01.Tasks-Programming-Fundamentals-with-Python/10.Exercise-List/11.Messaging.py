numbers = list(map(int, input().split()))
message = input()

def calculate_index(number):
    index = 0
    while number > 0:
        index += number % 10
        number //= 10
    return index

def get_char_from_message(index, message):
    count_index = 0
    for _ in range(index):
        count_index += 1
        if count_index == len(message):
            count_index = 0
    return message[count_index]

def calculate_real_index(index, message):
    count_index = 0
    for _ in range(index):
        count_index += 1
        if count_index == len(message):
            count_index = 0
    return count_index

for number in numbers:
    index = calculate_index(number)
    current_char = get_char_from_message(index, message)
    print(current_char, end='')

    real_index = calculate_real_index(index, message)
    message = message[:real_index] + message[real_index+1:]

print()
