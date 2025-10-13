input_money = float(input())
change = round(input_money * 100)
coins_counter = 0

while change > 0:
    if change - 200 >= 0:
        change -= 200
        coins_counter += 1
    elif change - 100 >= 0:
        change -= 100
        coins_counter += 1
    elif change - 50 >= 0:
        change -= 50
        coins_counter += 1
    elif change - 20 >= 0:
        change -= 20
        coins_counter += 1
    elif change - 10 >= 0:
        change -= 10
        coins_counter += 1
    elif change - 5 >= 0:
        change -= 5
        coins_counter += 1
    elif change - 2 >= 0:
        change -= 2
        coins_counter += 1
    elif change - 1 >= 0:
        change -= 1
        coins_counter += 1

print(coins_counter)
