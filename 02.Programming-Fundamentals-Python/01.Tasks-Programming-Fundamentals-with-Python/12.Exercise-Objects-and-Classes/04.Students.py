class Student:
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

n = int(input())
students = []

for _ in range(n):
    first_name, last_name, grade = input().split()
    students.append(Student(first_name, last_name, float(grade)))

students.sort(key=lambda s: s.grade, reverse=True)

for student in students:
    print(f"{student.first_name} {student.last_name}: {student.grade:.2f}")
