width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height

while free_space > 0:
    input_value = input()
    if input_value == "Done":
        break
    free_space -= int(input_value)

if free_space >= 0:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
