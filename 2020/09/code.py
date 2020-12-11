def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [int(l[:-1]) for l in f.readlines()]


def has_pair(sum_val: int, vals: list) -> bool:
    for idx_i, i in enumerate(vals):
        for j in vals[idx_i+1:]:
            if i + j == sum_val:
                return True
    return False


def find_invalid(numbers: list, preamble: int) -> int:
    for idx, val in enumerate(numbers[preamble:]):
        if not has_pair(val, numbers[idx:preamble+idx]):
            return val


def part1(vals: list, preamble: int) -> int:
    return find_invalid(vals, preamble)


def part2(vals: list, preamble: int) -> int:
    invalid_number = find_invalid(vals, preamble)
    count = len(vals)
    for x in range(count):
        set_sum = vals[x]
        for y in range(x+1, count):
            set_sum += vals[y]
            if set_sum == invalid_number:
                return min(vals[x:y]) + max(vals[x:y])
            if set_sum > invalid_number:
                break


def main():
    file_input = get_input()
    print(f"Part 1: {part1(file_input, 25)}")
    print(f"Part 2: {part2(file_input, 25)}")


def test():
    test_input = [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]
    assert part1(test_input, 5) == 127
    assert part2(test_input, 5) == 62


if __name__ == "__main__":
    test()
    main()
