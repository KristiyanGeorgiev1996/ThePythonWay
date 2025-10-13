original_string = input()
reverse_string = ""

for i in range(len(original_string) - 1, -1, -1):
    reverse_string += original_string[i]

print(reverse_string)
