dayOfWeek = input()

if dayOfWeek in ["Monday", "Tuesday", "Friday"]:
    print(12)
elif dayOfWeek in ["Wednesday", "Thursday"]:
    print(14)
elif dayOfWeek in ["Saturday", "Sunday"]:
    print(16)
else:
    print("Invalid day")
