tabs_opened = int(input())
salary = int(input())

for _ in range(tabs_opened):
    current_site = input()
    if current_site == "Facebook":
        salary -= 150
    elif current_site == "Instagram":
        salary -= 100
    elif current_site == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)
