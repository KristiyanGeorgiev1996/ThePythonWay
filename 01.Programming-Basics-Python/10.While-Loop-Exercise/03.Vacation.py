money_for_trip = float(input())
saved_money = float(input())

all_days_counter = 0
spend_days_counter = 0

while saved_money < money_for_trip:
    action = input()
    current_money = float(input())
    all_days_counter += 1

    if action == "spend":
        spend_days_counter += 1
        saved_money -= current_money
        if saved_money < 0:
            saved_money = 0
        if spend_days_counter == 5:
            print("You can't save the money.")
            print(all_days_counter)
            break
    elif action == "save":
        spend_days_counter = 0
        saved_money += current_money

if saved_money >= money_for_trip:
    print(f"You saved the money for {all_days_counter} days.")
