hour = int(input())
dayOfWeek = input()

if 10 <= hour <= 18:
    if dayOfWeek in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
        print("open")
    else:
        print("closed")
else:
    print("closed")
