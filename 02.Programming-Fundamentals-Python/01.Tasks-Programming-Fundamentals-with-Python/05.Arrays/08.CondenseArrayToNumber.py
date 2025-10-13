main_array = list(map(int, input().split()))

if len(main_array) == 1:
    print(main_array[0])
else:
    while len(main_array) > 1:
        condensed_array = []
        for i in range(len(main_array) - 1):
            condensed_array.append(main_array[i] + main_array[i + 1])
        main_array = condensed_array
    print(main_array[0])
