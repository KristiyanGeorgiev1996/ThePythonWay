text = input()

while text != "END":
    is_palindrome = True
    length = len(text)
    for i in range(length // 2):
        if text[i] != text[length - 1 - i]:
            is_palindrome = False
            break

    print("true" if is_palindrome else "false")
    text = input()
