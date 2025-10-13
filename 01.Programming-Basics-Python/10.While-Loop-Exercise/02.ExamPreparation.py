max_poor_grades = int(input())

poor_grades_counter = 0
problems_counter = 0
all_grades = 0
last_problem = ""

name_of_problem = input()

while name_of_problem != "Enough":
    current_grade = int(input())
    problems_counter += 1

    if current_grade <= 4:
        poor_grades_counter += 1
        if poor_grades_counter == max_poor_grades:
            print(f"You need a break, {max_poor_grades} poor grades.")
            break

    all_grades += current_grade
    last_problem = name_of_problem

    name_of_problem = input()

if name_of_problem == "Enough":
    average_grade = all_grades / problems_counter
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {problems_counter}")
    print(f"Last problem: {last_problem}")
