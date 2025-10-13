ages = int(input())

if 0 <= ages <= 2:
    print("baby")
elif 3 <= ages <= 13:
    print("child")
elif 14 <= ages <= 19:
    print("teenager")
elif 20 <= ages <= 65:
    print("adult")
elif ages >= 66:
    print("elder")
