city = input()
sales = float(input())

commission = 0

if city == "Sofia":
    if sales < 0:
        print("error")
    elif sales <= 500:
        commission = 5
    elif sales <= 1000:
        commission = 7
    elif sales <= 10000:
        commission = 8
    else:
        commission = 12
elif city == "Varna":
    if sales < 0:
        print("error")
    elif sales <= 500:
        commission = 4.5
    elif sales <= 1000:
        commission = 7.5
    elif sales <= 10000:
        commission = 10
    else:
        commission = 13
elif city == "Plovdiv":
    if sales < 0:
        print("error")
    elif sales <= 500:
        commission = 5.5
    elif sales <= 1000:
        commission = 8
    elif sales <= 10000:
        commission = 12
    else:
        commission = 14.5
else:
    print("error")

if commission > 0:
    output = commission * sales / 100
    print(f"{output:.2f}")
