daysStay = int(input()) - 1
typeRoom = input()
feedback = input()

bill = 0

if typeRoom == "room for one person":
    bill = daysStay * 18
elif typeRoom == "apartment":
    bill = daysStay * 25
    if daysStay < 10:
        bill *= 0.7
    elif 10 <= daysStay <= 15:
        bill *= 0.65
    else:
        bill *= 0.5
elif typeRoom == "president apartment":
    bill = daysStay * 35
    if daysStay < 10:
        bill *= 0.9
    elif 10 <= daysStay <= 15:
        bill *= 0.85
    else:
        bill *= 0.8

if feedback == "positive":
    bill *= 1.25
elif feedback == "negative":
    bill *= 0.9

print(f"{bill:.2f}")
