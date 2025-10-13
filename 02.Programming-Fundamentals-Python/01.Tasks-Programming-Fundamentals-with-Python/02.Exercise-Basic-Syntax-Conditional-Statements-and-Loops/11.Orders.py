poruhki = int(input())
all_sum = 0

for _ in range(poruhki):
    price_per_capsule = float(input())
    days = float(input())
    capsule_count = float(input())

    total_sum = days * capsule_count * price_per_capsule
    all_sum += total_sum
    print(f"The price for the coffee is: ${total_sum:.2f}")

print(f"Total: ${all_sum:.2f}")
