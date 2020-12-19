def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [int(num) for num in f.readline().split(",")]


def run(vals: list, final: int) -> int:
    start_at, last = len(vals) + 1, vals[-1]
    mem = {val: [i + 1] for i, val in enumerate(vals)}
    for i in range(start_at, final + 1):
        last = 0 if len(mem[last]) == 1 else mem[last][-1] - mem[last][-2]
        if last in mem:
            mem[last].append(i)
        else:
            mem[last] = [i]
    return last


def part1(vals: list) -> int:
    return run(vals, 2020)


def part2(vals: list) -> int:
    return run(vals, 30000000)


def main():
    file_input = get_input()
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


def test():
    test_input = [0, 3, 6]
    assert part1(test_input) == 436
    assert part2(test_input) == 175594


if __name__ == "__main__":
    test()
    main()
