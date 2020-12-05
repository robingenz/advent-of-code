def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l[:-1] for l in f.readlines()]


def format_input(lines: list) -> list:
    return [l.replace("F", "L")
            .replace("B", "U").replace("R", "U") for l in lines]


def calc(lowest: int, highest: int, val: str) -> int:
    for char in val:
        diff = highest - lowest
        if char == "L":
            highest -= round(diff / 2)
        else:
            lowest += round(diff / 2)
    return lowest if char == "L" else highest


def part1(vals: list) -> int:
    ids = []
    for val in vals:
        row = calc(0, 127, val[:7])
        col = calc(0, 7, val[7:])
        ids.append(row * 8 + col)
    return max(ids)


def part2(vals: list) -> int:
    ids = []
    for val in vals:
        row = calc(0, 127, val[:7])
        col = calc(0, 7, val[7:])
        ids.append(row * 8 + col)
    ids.sort()
    for idx, aaa in enumerate(ids[:-2]):
        if not ids[idx+1] - aaa == 1:
            return aaa + 1


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
