words = input().split()
chars = {}

for word in words:
    for letter in word:
        chars[letter] = chars.get(letter, 0) + 1

for letter, count in chars.items():
    print(f"{letter} -> {count}")
