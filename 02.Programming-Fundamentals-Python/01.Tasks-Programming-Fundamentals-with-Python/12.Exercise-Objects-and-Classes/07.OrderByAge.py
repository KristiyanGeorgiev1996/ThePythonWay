class Person:
    def __init__(self, name, ID, age):
        self.name = name
        self.ID = ID
        self.age = age

people = []

while True:
    line = input()
    if line == "End":
        break
    name, ID, age = line.split()
    people.append(Person(name, ID, int(age)))

people.sort(key=lambda p: p.age)

for person in people:
    print(f"{person.name} with ID: {person.ID} is {person.age} years old.")
