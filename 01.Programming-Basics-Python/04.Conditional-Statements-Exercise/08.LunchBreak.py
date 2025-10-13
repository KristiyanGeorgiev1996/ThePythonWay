import math

seriesName = input()
episodeLength = float(input())
breakLength = float(input())

lunchTime = breakLength / 8.0
freeTime = breakLength / 4.0
allNeededTime = lunchTime + freeTime + episodeLength

if breakLength >= allNeededTime:
    remainingTime = math.ceil(breakLength - allNeededTime)
    print(f"You have enough time to watch {seriesName} and left with {remainingTime} minutes free time.")
else:
    neededTime = math.ceil(allNeededTime - breakLength)
    print(f"You don't have enough time to watch {seriesName}, you need {neededTime} more minutes.")
