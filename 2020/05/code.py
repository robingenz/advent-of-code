def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l[:-1] for l in f.readlines()]


def format_input(lines: list) -> list:
    return [int(l.replace("F", "0").replace("L", "0")
                .replace("B", "1").replace("R", "1"), 2) for l in lines]


def part1(vals: list) -> int:
    return max(vals)


def part2(vals: list) -> int:
    vals.sort()
    for idx, val in enumerate(vals[:-1]):
        if not vals[idx+1] - val == 1:
            return val + 1


def main():
    file_input = format_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


def test():
    test_input = format_input(["FBFBBFFRLR"])
    assert part1(test_input) == 357


if __name__ == "__main__":
    test()
    main()
