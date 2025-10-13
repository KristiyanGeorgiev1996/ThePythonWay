degrees = float(input())
dayTime = input()

outfit = ""
shoes = ""

if 10 <= degrees <= 18:
    if dayTime == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif dayTime in ["Afternoon", "Evening"]:
        outfit = "Shirt"
        shoes = "Moccasins"
elif 18 < degrees <= 24:
    if dayTime in ["Morning", "Evening"]:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif dayTime == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
elif degrees >= 25:
    if dayTime == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif dayTime == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif dayTime == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
