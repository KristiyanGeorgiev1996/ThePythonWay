days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

n = int(input())

if 1 <= n <= 7:
    print(days_of_week[n - 1])
else:
    print("Invalid day!")
