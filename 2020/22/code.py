def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l.strip() for l in f.readlines()]


def parse_input(lines: list) -> list:
    decks = list()
    for line in lines:
        if "Player" in line:
            decks.append(list())
        elif line.isnumeric():
            decks[-1].append(int(line))
    print(decks)
    return decks


def calc_score(deck: list) -> int:
    return sum([j * (i + 1) for i, j in enumerate(reversed(deck))])


def play_regular(decks: list) -> int:
    deck1, deck2 = decks[0].copy(), decks[1].copy()
    while deck1 and deck2:
        card1, card2 = deck1.pop(0), deck2.pop(0)
        if card1 > card2:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])
    winning_deck = deck1 if len(deck1) > 0 else deck2
    return calc_score(winning_deck)


def play_recursive_combat(decks: list) -> int:
    return 0


def part1(decks: list) -> int:
    return play_regular(decks)


def part2(decks: list) -> int:
    return 0


def main():
    file_input = parse_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
