def get_input():
    with open("input.txt") as f:
        return [int(l) for l in f.readlines()]

def part1(vals):
    for idx_i, i in enumerate(vals):
        for j in vals[idx_i+1:]:
            if i + j == 2020:
                return i * j

def part2(vals):
    for idx_i, i in enumerate(vals):
        for idx_j, j in enumerate(vals[idx_i+1:]):
            for o in vals[idx_j+1:]:
                if i + j + o == 2020:
                    return i * j * o

def main():
    file_input = get_input()
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")

if __name__ == "__main__":
    main()