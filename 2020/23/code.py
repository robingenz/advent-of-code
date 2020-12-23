def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return f.read().strip()


def parse_input(line: str) -> list:
    return list(map(int, line))


class Cup:
    def __init__(self, value):
        self.value = value
        self.next = None


def play(cups: list, moves: int) -> Cup:
    size, cups_dict = len(cups), dict()
    for i in range(size):
        cups[i].next = cups[(i + 1) % size]
        cups_dict[cups[i].value] = cups[i]
    maximum, minimum = max(cups_dict.keys()), min(cups_dict.keys())
    current_cup = cups[0]
    for _ in range(moves):
        picked_up_cup = current_cup.next
        current_cup.next = current_cup.next.next.next.next
        destination_cup_value = current_cup.value
        forbidden_values = [current_cup.value,
                            picked_up_cup.value,
                            picked_up_cup.next.value,
                            picked_up_cup.next.next.value]
        while destination_cup_value in forbidden_values:
            destination_cup_value -= 1
            if destination_cup_value < minimum:
                destination_cup_value = maximum
        destination_cup = cups_dict[destination_cup_value]
        picked_up_cup.next.next.next = destination_cup.next
        destination_cup.next = picked_up_cup
        current_cup = current_cup.next
    return cups_dict[1]


def part1(val: int) -> int:
    cups, cups_size = [Cup(n) for n in val], len(val)
    cup_1 = play(cups, 100)
    result, next_cup = "", cup_1.next
    for _ in range(cups_size - 1):
        result += str(next_cup.value)
        next_cup = next_cup.next
    return int(result)


def part2(val: int) -> int:
    cups = [Cup(n) for n in range(1, 1000000 + 1)]
    for k, v in enumerate(val):
        cups[k] = Cup(v)
    cup_1 = play(cups, 10000000)
    return cup_1.next.value * cup_1.next.next.value


def main():
    file_input = parse_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


def test():
    test_input = parse_input("389125467")
    assert part1(test_input) == 67384529
    assert part2(test_input) == 149245887792


if __name__ == "__main__":
    test()
    main()
