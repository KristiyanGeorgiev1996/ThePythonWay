month = input()
daysStay = int(input())

studioPrice = 0
apartmentPrice = 0

if month in ["May", "October"]:
    studioPrice = 50
    apartmentPrice = 65
    if 7 < daysStay <= 14:
        studioPrice *= 0.95
    elif daysStay > 14:
        studioPrice *= 0.7
elif month in ["June", "September"]:
    studioPrice = 75.20
    apartmentPrice = 68.70
    if daysStay > 14:
        studioPrice *= 0.8
elif month in ["July", "August"]:
    studioPrice = 76
    apartmentPrice = 77

if daysStay > 14:
    apartmentPrice *= 0.9

studioBill = daysStay * studioPrice
apartmentBill = daysStay * apartmentPrice

print(f"Apartment: {apartmentBill:.2f} lv.")
print(f"Studio: {studioBill:.2f} lv.")
