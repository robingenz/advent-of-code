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


def part1(decks: list) -> int:
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        print(decks[0][0], decks[1][0])
        if decks[0][0] > decks[1][0]:
            decks[0].append(decks[0][0])
            decks[0].append(decks[1][0])
            decks[0].pop(0)
            decks[1].pop(0)
        else:
            decks[1].append(decks[1][0])
            decks[1].append(decks[0][0])
            decks[0].pop(0)
            decks[1].pop(0)
    winner = 0 if len(decks[0]) > 0 else 1
    decks[winner].reverse()
    score = 0
    for i in range(len(decks[winner])):
        score += decks[winner][i] * (i + 1)
    return score


def part2(decks: list) -> int:
    return 0


def main():
    file_input = parse_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
