exspected_sum = 2020

with open('input.txt') as input_file:
    entries = [int(l) for l in input_file.readlines()]

for idx_i, i in enumerate(entries):
    for j in entries[idx_i+1:]:
        if i + j == exspected_sum:
            print('{} * {} = {}'.format(i, j, i * j))
            exit()
