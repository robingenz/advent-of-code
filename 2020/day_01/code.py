def get_input() -> list:
    with open("input.txt") as f:
        return [int(l) for l in f.readlines()]

def part1(vals: list) -> int:
    for idx_i, i in enumerate(vals):
        for j in vals[idx_i+1:]:
            if i + j == 2020:
                return i * j

def part2(vals: list) -> int:
    for idx_i, i in enumerate(vals):
        for idx_j, j in enumerate(vals[idx_i+1:]):
            for o in vals[idx_j+1:]:
                if i + j + o == 2020:
                    return i * j * o

def main():
    file_input = get_input()
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")

def test():
    test_input = [1721, 979, 366, 299, 675, 1456]
    assert part1(test_input) == 514579
    assert part2(test_input) == 241861950

if __name__ == "__main__":
    test()
    main()