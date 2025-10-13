firstPlayerTime = int(input())
secondPlayerTime = int(input())
thirdPlayerTime = int(input())

timeInSeconds = firstPlayerTime + secondPlayerTime + thirdPlayerTime
minutes = timeInSeconds // 60
seconds = timeInSeconds % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
