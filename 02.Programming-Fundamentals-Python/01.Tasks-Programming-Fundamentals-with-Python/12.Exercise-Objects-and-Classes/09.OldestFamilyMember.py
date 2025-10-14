class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Family:
    def __init__(self):
        self.people = []

    def add_member(self, member):
        self.people.append(member)

    def get_oldest_member(self):
        if not self.people:
            return None
        return max(self.people, key=lambda p: p.age)

n = int(input())
family = Family()

for _ in range(n):
    name, age = input().split()
    family.add_member(Person(name, int(age)))

oldest = family.get_oldest_member()
if oldest:
    print(f"{oldest.name} {oldest.age}")
