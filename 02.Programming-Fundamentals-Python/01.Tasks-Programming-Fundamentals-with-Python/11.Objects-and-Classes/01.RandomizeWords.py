import random

class StringRandomizer:
    def __init__(self):
        self.input = ''
        self.randomizer_input = []

    def randomize_input(self):
        self.randomizer_input = []
        splitted = self.input.split(' ')
        count = len(splitted)

        for _ in range(count):
            index = random.randrange(len(splitted))
            self.randomizer_input.append(splitted.pop(index))

randomizer = StringRandomizer()
randomizer.input = input()
randomizer.randomize_input()

for item in randomizer.randomizer_input:
    print(item)
