class Student:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

students = []

while True:
    line = input()
    if line == 'end':
        break
    tokens = line.split()
    first_name, last_name, age, city = tokens[0], tokens[1], int(tokens[2]), tokens[3]

    existing = False
    for student in students:
        if student.first_name == first_name and student.last_name == last_name:
            student.age = age
            existing = True
            break

    if not existing:
        students.append(Student(first_name, last_name, age, city))

filter_city = input()

for student in students:
    if student.city == filter_city:
        print(f"{student.first_name} {student.last_name} is {student.age} years old.")
