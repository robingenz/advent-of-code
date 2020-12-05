def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l[:-1] for l in f.readlines()]


def count_trees(vals: list, right: int, down: int) -> int:
    counter, x, y = 0, 0, down
    while y < len(vals):
        x += right
        if x >= len(vals[y]):
            x -= len(vals[y])
        counter += vals[y][x] == "#"
        y += down
    return counter


def part1(vals: list) -> int:
    return count_trees(vals, 3, 1)


def part2(vals: list) -> int:
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    result = 1
    for slope in slopes:
        result *= count_trees(vals, slope[0], slope[1])
    return result


def main():
    file_input = get_input()
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


def test():
    test_input = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#",
    ]
    assert part1(test_input) == 7
    assert part2(test_input) == 336


if __name__ == "__main__":
    test()
    main()
