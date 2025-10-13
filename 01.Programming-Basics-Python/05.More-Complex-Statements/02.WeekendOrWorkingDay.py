dayOfWeek = input()

if dayOfWeek in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("Working day")
elif dayOfWeek in ["Saturday", "Sunday"]:
    print("Weekend")
else:
    print("Error")
