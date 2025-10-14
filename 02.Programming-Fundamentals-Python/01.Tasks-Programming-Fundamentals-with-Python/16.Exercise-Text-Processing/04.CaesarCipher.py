line = input()
result = ''

for ch in line:
    ascii_number = ord(ch) + 3
    result += chr(ascii_number)

print(result)
