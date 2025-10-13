country = input()

if country == "USA" or country == "England":
    print("English")
elif country in ["Spain", "Argentina", "Mexico"]:
    print("Spanish")
else:
    print("unknown")
