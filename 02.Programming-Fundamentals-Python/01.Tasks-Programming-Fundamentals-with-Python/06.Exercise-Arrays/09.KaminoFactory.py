length_of_dna = int(input())
command = input()

max_count_of_ones = 0
best_dna = [0] * length_of_dna
best_sequence_index = 0
best_sequence_sum = 0
current_dnas = 0
best_dna_row = 0

while command != "Clone them!":
    current_arr = [int(x) for x in command.split('!') if x != '']

    count_of_ones = 0
    current_max_count_of_ones = 0
    index = 0
    current_best_index = -1

    for current_index, val in enumerate(current_arr):
        if val == 1:
            count_of_ones += 1
            if count_of_ones == 1:
                index = current_index
        else:
            if count_of_ones > current_max_count_of_ones:
                current_max_count_of_ones = count_of_ones
                current_best_index = index
            count_of_ones = 0

    if count_of_ones > current_max_count_of_ones:
        current_max_count_of_ones = count_of_ones
        current_best_index = index

    current_dnas += 1

    if (current_dnas == 1 or
            current_max_count_of_ones > max_count_of_ones or
            (current_max_count_of_ones == max_count_of_ones and current_best_index < best_sequence_index) or
            (current_max_count_of_ones == max_count_of_ones and current_best_index == best_sequence_index and sum(
                current_arr) > best_sequence_sum)):
        max_count_of_ones = current_max_count_of_ones
        best_sequence_index = current_best_index
        best_sequence_sum = sum(current_arr)
        best_dna_row = current_dnas
        best_dna = current_arr

    command = input()

print(f"Best DNA sample {best_dna_row} with sum: {best_sequence_sum}.")
print(' '.join(map(str, best_dna)))
