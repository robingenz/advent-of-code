def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l.split("\n") for l in f.read().rstrip('\n').split("\n\n")]


def part1(vals: list) -> int:
    counter = 0
    for val in vals:
        counter += len(set(''.join(val)))
    return counter


def part2(vals: list) -> int:
    counter = 0
    for val in vals:
        val = [set(i) for i in val]
        counter += len(set.intersection(*val))
    return counter


def main():
    file_input = get_input()
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
