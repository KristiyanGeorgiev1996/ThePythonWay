age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toys_count = 0
money = 0
money_intake = 0

for i in range(1, age + 1):
    if i % 2 == 1:
        toys_count += 1
    else:
        money_intake += 10
        money += money_intake
        money -= 1

money += toys_count * toy_price

if money >= washing_machine_price:
    print(f"Yes! {money - washing_machine_price:.2f}")
else:
    print(f"No! {washing_machine_price - money:.2f}")
