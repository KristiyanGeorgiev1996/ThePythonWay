import re

class Participant:
    def __init__(self, name):
        self.name = name
        self.distance = 0

participants_input = "George, Peter, Bill, Tom"
race_input = [
    "G4e@55or%6g6!68e!!@",
    "R1@!3a$y4456@",
    "B5@i@#123ll",
    "G@e54o$r6ge#",
    "7P%et^#e5346r",
    "T$o553m&6",
    "end of race"
]

participants_arr = participants_input.split(", ")
participants = {p: Participant(p) for p in participants_arr}

letters_pattern = re.compile(r'[A-Za-z]')
digits_pattern = re.compile(r'\d')

for command in race_input:
    if command == "end of race":
        break

    name = ''.join(letters_pattern.findall(command))
    distance = sum(int(d) for d in digits_pattern.findall(command))

    if name in participants:
        participants[name].distance += distance

ordered = sorted(participants.values(), key=lambda x: x.distance, reverse=True)[:3]

print(f"1st place: {ordered[0].name}")
print(f"2nd place: {ordered[1].name}")
print(f"3rd place: {ordered[2].name}")
