word = input()
text = input()

index = text.find(word)

while index != -1:
    text = text[:index] + text[index + len(word):]
    index = text.find(word)

print(text)
