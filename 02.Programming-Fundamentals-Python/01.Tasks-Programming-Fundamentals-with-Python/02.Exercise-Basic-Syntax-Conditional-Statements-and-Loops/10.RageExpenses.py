lost_games = int(input())
price_slushalki = float(input())
price_mouse = float(input())
price_klaviatura = float(input())
price_display = float(input())

total_expenses = 0

if lost_games >= 2:
    broken_slushalki = lost_games // 2
    total_expenses += broken_slushalki * price_slushalki
if lost_games >= 3:
    broken_mice = lost_games // 3
    total_expenses += broken_mice * price_mouse
if lost_games >= 6:
    broken_klaviatura = lost_games // 6
    total_expenses += broken_klaviatura * price_klaviatura
if lost_games >= 12:
    broken_display = lost_games // 12
    total_expenses += broken_display * price_display

print(f"Rage expenses: {total_expenses:.2f} lv.")
