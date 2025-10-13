student_name = input()

expels_count = 0
years_count = 0
grades_sum = 0

while expels_count < 2 and years_count < 12:
    grade = float(input())
    years_count += 1
    if grade < 4:
        expels_count += 1
        continue
    grades_sum += grade

if expels_count < 2:
    average_grade = grades_sum / years_count
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
else:
    print(f"{student_name} has been excluded at {years_count - 1} grade")
