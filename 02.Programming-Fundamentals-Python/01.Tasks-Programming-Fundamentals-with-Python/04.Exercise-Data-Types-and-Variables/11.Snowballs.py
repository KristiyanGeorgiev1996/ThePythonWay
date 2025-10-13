n = int(input())

best_snow = 0
best_time = 0
best_quality = 0
best_value = 0

for _ in range(n):
    snow = int(input())
    time = int(input())
    quality = int(input())

    value = (snow // time) ** quality

    if best_value < value:
        best_value = value
        best_quality = quality
        best_snow = snow
        best_time = time

print(f"{best_snow} : {best_time} = {best_value} ({best_quality})")
