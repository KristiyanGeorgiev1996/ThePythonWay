length = float(input())
width = float(input())
height = float(input())
percent = float(input())

aquariumVolume = length * width * height
aquariumLitersVolume = aquariumVolume / 1000
takenSpace = aquariumLitersVolume * (percent / 100)

neededLiters = aquariumLitersVolume - takenSpace
print(neededLiters)
