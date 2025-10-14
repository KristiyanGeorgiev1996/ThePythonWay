some_string = input()

digits = ""
letters = ""
symbols = ""

for char in some_string:
    if char.isalpha():
        letters += char
    elif char.isdigit():
        digits += char
    else:
        symbols += char

print(digits)
print(letters)
print(symbols)
