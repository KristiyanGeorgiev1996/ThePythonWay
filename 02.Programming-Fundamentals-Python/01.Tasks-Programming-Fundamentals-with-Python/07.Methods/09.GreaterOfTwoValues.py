input_type = input()
value1 = input()
value2 = input()

def game_max(input_type, value1, value2):
    if input_type == "int":
        return max(int(value1), int(value2))
    elif input_type in ("char", "string"):
        return value1 if value1[0] > value2[0] else value2
    else:
        return ""

print(game_max(input_type, value1, value2))
