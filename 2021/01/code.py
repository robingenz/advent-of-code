def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [int(l) for l in f.readlines()]


def part1(vals: list) -> int:
    num = 0
    for i in range(1, len(vals)):
        if vals[i-1] < vals[i]:
            num += 1
    return num


def part2(vals: list) -> int:
    return 0


def main():
    file_input = get_input()
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


def test():
    test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert part1(test_input) == 7
    # assert part2(test_input) == 241861950


if __name__ == "__main__":
    test()
    main()
