hours = int(input())
minutes = int(input())

minutes += 30
if minutes >= 60:
    hours += 1
    minutes -= 60
if hours >= 24:
    hours -= 24

if 0 <= minutes <= 9:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")
