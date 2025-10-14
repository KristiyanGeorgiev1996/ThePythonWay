size_of_the_field = int(input())
initial_indexes = list(map(int, input().split()))
playground = [0] * size_of_the_field

for idx in initial_indexes:
    if 0 <= idx < len(playground):
        playground[idx] = 1

def ladybug_flight_left(start, end, playground):
    if end == 0:
        return playground
    if end < 0:
        return ladybug_flight_right(start, abs(end), playground)

    flight_index = start - end

    if 0 <= flight_index < len(playground):
        if playground[flight_index] == 0:
            playground[flight_index] = 1
            playground[start] = 0
        else:
            new_index = -1
            i = flight_index
            while i >= 0:
                if playground[i] == 0:
                    new_index = i
                    playground[new_index] = 1
                    playground[start] = 0
                    break
                i -= end
            if new_index < 0:
                playground[start] = 0
    else:
        playground[start] = 0

    return playground

def ladybug_flight_right(start, end, playground):
    if end == 0:
        return playground
    if end < 0:
        return ladybug_flight_left(start, abs(end), playground)

    flight_index = start + end

    if 0 <= flight_index < len(playground):
        if playground[flight_index] == 0:
            playground[flight_index] = 1
            playground[start] = 0
        else:
            new_index = -1
            i = flight_index
            while i < len(playground):
                if playground[i] == 0:
                    new_index = i
                    playground[new_index] = 1
                    playground[start] = 0
                    break
                i += end
            if new_index < 0:
                playground[start] = 0
    else:
        playground[start] = 0

    return playground

while True:
    command = input()
    if command == "end":
        break
    parts = command.split()
    start = int(parts[0])
    direction = parts[1]
    end = int(parts[2])

    if 0 <= start < len(playground) and playground[start] == 1:
        if direction == "left":
            playground = ladybug_flight_left(start, end, playground)
        elif direction == "right":
            playground = ladybug_flight_right(start, end, playground)

print(' '.join(map(str, playground)))
