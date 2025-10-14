def add(lst, lesson_title):
    if lesson_title not in lst:
        lst.append(lesson_title)
    return lst

def insert(lst, lesson_title, index):
    if lesson_title not in lst and 0 <= index < len(lst):
        lst.insert(index, lesson_title)
    return lst

def remove(lst, lesson_title):
    if lesson_title in lst:
        lst.remove(lesson_title)
    if lesson_title + "-Exercise" in lst:
        lst.remove(lesson_title + "-Exercise")
    return lst

def swap(lst, lesson_title1, lesson_title2):
    if lesson_title1 in lst and lesson_title2 in lst:
        index1, index2 = lst.index(lesson_title1), lst.index(lesson_title2)
        lst[index1], lst[index2] = lst[index2], lst[index1]

        if lesson_title1 + "-Exercise" in lst:
            lst.remove(lesson_title1 + "-Exercise")
            lst.insert(lst.index(lesson_title1) + 1, lesson_title1 + "-Exercise")
        if lesson_title2 + "-Exercise" in lst:
            lst.remove(lesson_title2 + "-Exercise")
            lst.insert(lst.index(lesson_title2) + 1, lesson_title2 + "-Exercise")
    return lst

def exercise(lst, lesson_title):
    if lesson_title in lst and lesson_title + "-Exercise" not in lst:
        lst.insert(lst.index(lesson_title) + 1, lesson_title + "-Exercise")
    elif lesson_title not in lst:
        lst.extend([lesson_title, lesson_title + "-Exercise"])
    return lst

def softuni_course_planning(lst, command):
    action = command[0]
    if action == "Add":
        return add(lst, command[1])
    elif action == "Insert":
        return insert(lst, command[1], int(command[2]))
    elif action == "Remove":
        return remove(lst, command[1])
    elif action == "Swap":
        return swap(lst, command[1], command[2])
    elif action == "Exercise":
        return exercise(lst, command[1])
    return lst

lst = input().split(", ")

while True:
    line = input()
    if line == "course start":
        break
    command = line.split(":")
    lst = softuni_course_planning(lst, command)

for i, lesson in enumerate(lst, 1):
    print(f"{i}.{lesson}")
