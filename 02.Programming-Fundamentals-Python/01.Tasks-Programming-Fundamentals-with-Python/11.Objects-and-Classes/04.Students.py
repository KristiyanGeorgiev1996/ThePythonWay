class Student:
    def __init__(self, first_name, last_name, age, home_town):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.home_town = home_town

students = []

while True:
    line = input()
    if line == 'end':
        break
    student_data = line.split()
    student = Student(student_data[0], student_data[1], student_data[2], student_data[3])
    students.append(student)

city = input()

for student in students:
    if student.home_town == city:
        print(f"{student.first_name} {student.last_name} is {student.age} years old.")
