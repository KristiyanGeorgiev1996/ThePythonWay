import math

count_kegs = int(input())

biggest_model_name = ""
biggest_keg_volume = 0

for _ in range(count_kegs):
    model = input()
    radius = float(input())
    height = int(input())

    volume = math.pi * radius ** 2 * height
    if volume > biggest_keg_volume:
        biggest_keg_volume = volume
        biggest_model_name = model

print(biggest_model_name)
