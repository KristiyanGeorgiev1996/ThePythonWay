class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

n = int(input())
employees = []

for _ in range(n):
    name, salary, department = input().split()
    employees.append(Employee(name, float(salary), department))

department_groups = {}
for emp in employees:
    if emp.department not in department_groups:
        department_groups[emp.department] = []
    department_groups[emp.department].append(emp)

highest_dept = ''
highest_avg_salary = 0

for dept, emps in department_groups.items():
    avg_salary = sum(e.salary for e in emps) / len(emps)
    if avg_salary > highest_avg_salary:
        highest_avg_salary = avg_salary
        highest_dept = dept

print(f"Highest Average Salary: {highest_dept}")
for emp in sorted(department_groups[highest_dept], key=lambda e: e.salary, reverse=True):
    print(f"{emp.name} {emp.salary:.2f}")
