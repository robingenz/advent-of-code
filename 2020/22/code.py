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
    return decks


def calc_score(deck: list) -> int:
    return sum([j * (i + 1) for i, j in enumerate(reversed(deck))])


def play_regular(deck1: list, deck2: list) -> tuple:
    deck1, deck2 = deck1.copy(), deck2.copy()
    while deck1 and deck2:
        card1, card2 = deck1.pop(0), deck2.pop(0)
        if card1 > card2:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])
    if deck1:
        return 1, deck1
    else:
        return 2, deck2


def play_recursive_combat(deck1: list, deck2: list) -> tuple:
    deck1, deck2 = deck1.copy(), deck2.copy()
    deck1_history = set()
    deck2_history = set()
    while deck1 and deck2:
        if tuple(deck1) in deck1_history and tuple(deck2) in deck2_history:
            return 1, deck1
        deck1_history.add(tuple(deck1))
        deck2_history.add(tuple(deck2))
        card1, card2 = deck1.pop(0), deck2.pop(0)
        if len(deck1) >= card1 and len(deck2) >= card2:
            winner, _ = play_recursive_combat(deck1[0:card1], deck2[0:card2])
        else:
            winner = 1 if card1 > card2 else 2
        if winner == 1:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])
    if deck1:
        return 1, deck1
    else:
        return 2, deck2


def part1(decks: list) -> int:
    _, winning_deck = play_regular(decks[0], decks[1])
    return calc_score(winning_deck)


def part2(decks: list) -> int:
    _, winning_deck = play_recursive_combat(decks[0], decks[1])
    return calc_score(winning_deck)


def main():
    file_input = parse_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
