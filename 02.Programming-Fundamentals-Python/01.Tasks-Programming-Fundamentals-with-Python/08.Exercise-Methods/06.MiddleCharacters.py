input_str = input()

def middle_character(input_str):
    if len(input_str) % 2 == 0:
        middle_character1 = input_str[len(input_str) // 2 - 1]
        middle_character2 = input_str[len(input_str) // 2]
        print(middle_character1 + middle_character2)
    else:
        middle_character = input_str[len(input_str) // 2]
        print(middle_character)

middle_character(input_str)
