import math

money = float(input())
students = int(input())
swords = float(input())
belt = float(input())
robe = float(input())

real_swords = math.ceil(students * 1.1)
free_belts = students // 6
real_belts = students - free_belts

total_swords_price = real_swords * swords
total_belts_price = real_belts * belt
total_robe_price = students * robe

total_sum = total_swords_price + total_belts_price + total_robe_price

if total_sum <= money:
    print(f"The money is enough - it would cost {total_sum:.2f}lv.")
else:
    needed = total_sum - money
    print(f"John will need {needed:.2f}lv more.")
