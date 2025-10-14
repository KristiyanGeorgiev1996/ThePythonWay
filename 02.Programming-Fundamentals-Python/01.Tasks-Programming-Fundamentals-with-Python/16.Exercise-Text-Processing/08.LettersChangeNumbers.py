text = input().split()
total_sum = 0

for s in text:
    first_char = s[0]
    last_char = s[-1]
    number = int(s[1:-1])

    # Process first letter
    if first_char.isupper():
        total_sum += number / (ord(first_char) - ord('A') + 1)
    else:
        total_sum += number * (ord(first_char) - ord('a') + 1)

    # Process last letter
    if last_char.isupper():
        total_sum -= ord(last_char) - ord('A') + 1
    else:
        total_sum += ord(last_char) - ord('a') + 1

print(f"{total_sum:.2f}")
