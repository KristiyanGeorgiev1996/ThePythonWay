while True:
    text = input()
    if text == "end":
        break
    reversed_text = text[::-1]  # slice notation reverses the string
    print(f"{text} = {reversed_text}")
