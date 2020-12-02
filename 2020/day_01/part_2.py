exspected_sum = 2020

with open('input.txt') as input_file:
    entries = [int(l) for l in input_file.readlines()]

for idx_i, i in enumerate(entries):
    for idx_j, j in enumerate(entries[idx_i+1:]):
        for o in entries[idx_j+1:]:
            if i + j + o == exspected_sum:
                print('{} * {} * {} = {}'.format(i, j, o, i * j * o))
                exit()
