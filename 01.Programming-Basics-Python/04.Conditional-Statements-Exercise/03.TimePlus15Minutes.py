hours = int(input())
minutes = int(input())

if minutes >= 45:
    hours += 1
    minutes = (minutes + 15) % 60
else:
    minutes += 15

if hours == 24:
    hours = 0

if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")
