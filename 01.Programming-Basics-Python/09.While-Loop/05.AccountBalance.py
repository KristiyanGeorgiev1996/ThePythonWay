input_value = input()
total = 0

while input_value != "NoMoreMoney":
    payment = float(input_value)
    if payment < 0:
        print("Invalid operation!")
        break
    total += payment
    print(f"Increase: {payment:.2f}")
    input_value = input()

print(f"Total: {total:.2f}")
