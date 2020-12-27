
def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l.strip() for l in f.readlines()]


def parse_input(lines: list) -> list:
    instructions = list()
    for line in lines:
        i = 0
        instructions.append([])
        while i < len(line):
            if line[i] == "s" or line[i] == "n":
                instructions[-1].append(line[i:i+2])
                i += 2
                continue
            instructions[-1].append(line[i])
            i += 1
    return instructions


def run(instructions: list) -> dict:
    dirs = {"e": (2, 0), "se": (1, -1), "sw": (-1, -1),
            "w": (-2, 0), "nw": (-1, 1), "ne": (1, 1)}
    result = {
        (0, 0): True
    }
    for instruction in instructions:
        coords = (0, 0)
        for item in instruction:
            coords = (coords[0] + dirs[item][0], coords[1] + dirs[item][1])
        result[coords] = not result[coords] if coords in result else False
    return result


def part1(instructions: list) -> int:
    tiles = run(instructions)
    return len([v for _, v in tiles.items() if v == False])


def part2(instructions: list) -> int:
    return 0


def main():
    file_input = parse_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
