number = int(input())
number2 = int(input())
number3 = int(input())

if number >= number2 and number >= number3:
    print(number)
    if number2 >= number3:
        print(number2)
        print(number3)
    else:
        print(number3)
        print(number2)
elif number2 >= number3 and number2 >= number:
    print(number2)
    if number >= number3:
        print(number)
        print(number3)
    else:
        print(number3)
        print(number)
else:
    print(number3)
    if number >= number2:
        print(number)
        print(number2)
    else:
        print(number2)
        print(number)
