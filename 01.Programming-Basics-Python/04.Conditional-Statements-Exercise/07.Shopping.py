budget = float(input())
videocardsCount = int(input())
processorsCount = int(input())
ramsCount = int(input())

videocardsBill = videocardsCount * 250
processorsBill = processorsCount * (videocardsBill * 0.35)
ramsBill = ramsCount * (videocardsBill * 0.1)

bill = videocardsBill + processorsBill + ramsBill

if videocardsCount > processorsCount:
    bill -= bill * 0.15

if bill <= budget:
    moneyLeft = budget - bill
    print(f"You have {moneyLeft:.2f} leva left!")
else:
    neededMoney = bill - budget
    print(f"Not enough money! You need {neededMoney:.2f} leva more!")
