def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return f.read().strip()


def get_next_cup_idx(cups: list, current_cup: int) -> int:
    idx, size = cups.index(current_cup), len(cups)
    return (idx + 1) % size


def part1(num: str) -> int:
    cups = [int(n) for n in list(num)]
    current_cup = cups[0]
    moves = 100
    maximum, minimum = max(cups), min(cups)
    for _ in range(moves):
        picked_up_cups = [cups.pop(get_next_cup_idx(
            cups, current_cup)) for _ in range(3)]
        destination_cup = current_cup - 1
        if destination_cup < minimum:
            destination_cup = maximum
        while destination_cup in picked_up_cups:
            destination_cup -= 1
            if destination_cup < minimum:
                destination_cup = maximum
        destination_cup_idx = cups.index(destination_cup)
        for removed_cup in reversed(picked_up_cups):
            cups.insert(destination_cup_idx + 1, removed_cup)
        current_cup = cups[get_next_cup_idx(cups, current_cup)]
    result = cups[cups.index(1) + 1:]
    result.extend(cups[:cups.index(1)])
    return int("".join([str(c) for c in result]))


def part2(input: str) -> int:
    return 0


def main():
    file_input = get_input()
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


def test():
    test_input = "389125467"
    assert part1(test_input) == 67384529
    assert part2(test_input) == 0


if __name__ == "__main__":
    test()
    main()
