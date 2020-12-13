def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l.strip() for l in f.readlines()]


def format_input(lines: list) -> list:
    return lines


def part1(vals: list) -> int:
    return 0


def part2(vals: list) -> int:
    return 0


def main():
    file_input = format_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


def test():
    test_input = format_input([])
    assert part1(test_input) == 0
    assert part2(test_input) == 0


if __name__ == "__main__":
    test()
    main()
