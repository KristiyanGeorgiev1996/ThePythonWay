text = input()
new_text = ""

for i in range(len(text)):
    if i == 0 or text[i] != text[i - 1]:
        new_text += text[i]

print(new_text)
