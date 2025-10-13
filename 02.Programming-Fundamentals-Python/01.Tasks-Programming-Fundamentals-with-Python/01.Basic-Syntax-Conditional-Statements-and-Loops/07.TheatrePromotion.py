day = input()
ages = int(input())

if day == "Weekday":
    if 0 <= ages <= 18 or 65 <= ages <= 122:
        print("12$")
    elif 19 <= ages <= 64:
        print("18$")
    else:
        print("Error!")
elif day == "Weekend":
    if 0 <= ages <= 18 or 65 <= ages <= 122:
        print("15$")
    elif 19 <= ages <= 64:
        print("20$")
    else:
        print("Error!")
elif day == "Holiday":
    if 0 <= ages <= 18:
        print("5$")
    elif 19 <= ages <= 64:
        print("12$")
    elif 65 <= ages <= 122:
        print("10$")
    else:
        print("Error!")
else:
    print("Error!")
