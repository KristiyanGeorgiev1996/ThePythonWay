import math

peoples = float(input())
max_people = float(input())

courses = math.ceil(peoples / max_people)

print(courses)
