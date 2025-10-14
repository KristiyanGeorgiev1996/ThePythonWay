banned_strings = input().split(", ")
text = input()

for banned in banned_strings:
    stars = '*' * len(banned)
    text = text.replace(banned, stars)

print(text)
