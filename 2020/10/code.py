def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [int(l[:-1]) for l in f.readlines()]


def complete_input(vals: list) -> list:
    vals.append(0)
    vals.append(max(vals) + 3)
    vals.sort()
    return vals


def part1(vals: list) -> int:
    diffs, size = [], len(vals)
    for i in range(1, size):
        diffs.append(vals[i] - vals[i-1])
    return diffs.count(1) * diffs.count(3)


def part2(vals: list) -> int:
    results, size = [1, 0, 0], len(vals)
    for i in range(1, size-1):
        result = results[0]
        if i - 2 >= 0 and vals[i] - vals[i-2] <= 3:
            result = sum(results[0:2])
        if i - 3 >= 0 and vals[i] - vals[i-3] <= 3:
            result = sum(results)
        results.insert(0, result)
        results.pop()
    return results[0]


def main():
    file_input = complete_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
