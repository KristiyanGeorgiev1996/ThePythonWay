text = input()
sum_vowels = 0

while len(text) != 0:
    last_character = text[-1]
    if last_character in "AaEeIiOoUu":
        sum_vowels += 1
    text = text[:-1]

print(sum_vowels)
