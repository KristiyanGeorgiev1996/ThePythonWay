jury_count = int(input())

presentations_count = 0
all_grades_sum = 0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        break

    presentations_count += 1
    current_grades_sum = 0

    for _ in range(jury_count):
        grade = float(input())
        current_grades_sum += grade
        all_grades_sum += grade

    average_grade = current_grades_sum / jury_count
    print(f"{presentation_name} - {average_grade:.2f}.")

average_grade_all = all_grades_sum / (presentations_count * jury_count)
print(f"Student's final assessment is {average_grade_all:.2f}.")
