power = int(input())
distance = int(input())
exhaustion_factor = int(input())

rest_power = power
targets_count = 0

while rest_power >= distance:
    if rest_power == power * 0.5 and exhaustion_factor != 0:
        rest_power /= exhaustion_factor
    if rest_power < distance:
        break
    rest_power -= distance
    targets_count += 1

print(rest_power)
print(targets_count)
