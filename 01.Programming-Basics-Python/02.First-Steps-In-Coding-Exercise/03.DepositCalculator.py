deposit = float(input())
monthsTerm = int(input())
yearPercent = float(input()) / 100

sum = deposit + monthsTerm * ((deposit * yearPercent) / 12)
print(sum)
