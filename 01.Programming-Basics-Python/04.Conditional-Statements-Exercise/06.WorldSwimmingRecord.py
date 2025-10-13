import math

recordInSeconds = float(input())
metersToSwim = float(input())
secondsForOneMeterSwim = float(input())

swimSecondsWithoutDelay = metersToSwim * secondsForOneMeterSwim
delayTimes = math.floor(metersToSwim / 15)

swimSeconds = swimSecondsWithoutDelay + delayTimes * 12.5

if swimSeconds < recordInSeconds:
    print(f"Yes, he succeeded! The new world record is {swimSeconds:.2f} seconds.")
else:
    neededSeconds = swimSeconds - recordInSeconds
    print(f"No, he failed! He was {neededSeconds:.2f} seconds slower.")
