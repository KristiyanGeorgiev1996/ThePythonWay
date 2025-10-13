peoples = int(input())
type_of_group = input()
day_of_week = input()

price = 0
total_price = 0

if type_of_group == "Students":
    if day_of_week == "Friday":
        price = peoples * 8.45
    elif day_of_week == "Saturday":
        price = peoples * 9.80
    elif day_of_week == "Sunday":
        price = peoples * 10.46
    if peoples >= 30:
        total_price = price * 0.85
    else:
        total_price = price
elif type_of_group == "Business":
    if day_of_week == "Friday":
        price = peoples * 10.90
    elif day_of_week == "Saturday":
        price = peoples * 15.60
    elif day_of_week == "Sunday":
        price = peoples * 16
    if peoples >= 100:
        total_price = (peoples - 10) * (price / peoples)
    else:
        total_price = price
elif type_of_group == "Regular":
    if day_of_week == "Friday":
        price = peoples * 15
    elif day_of_week == "Saturday":
        price = peoples * 20
    elif day_of_week == "Sunday":
        price = peoples * 22.50
    if 10 <= peoples <= 20:
        total_price = price * 0.95
    else:
        total_price = price

print(f"Total price: {total_price:.2f}")
