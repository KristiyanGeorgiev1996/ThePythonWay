one = input()[0]
two = input()[0]

if one < two:
    for i in range(ord(one) + 1, ord(two)):
        print(chr(i), end=" ")
elif one > two:
    for i in range(ord(two) + 1, ord(one)):
        print(chr(i), end=" ")
