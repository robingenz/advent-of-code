def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l[:-1] for l in f.readlines()]


def parse_input(lines: list) -> list:
    instructions = []
    for line in lines:
        split = line.split(" ")
        instructions.append([split[0], int(split[1])])
    return instructions


def run(instructions: list) -> tuple:
    pointer, acc, size, history = 0, 0, len(instructions), []
    while not pointer in history and pointer < size:
        history.append(pointer)
        if instructions[pointer][0] == "acc":
            acc += instructions[pointer][1]
        elif instructions[pointer][0] == "jmp":
            pointer += instructions[pointer][1]
            continue
        pointer += 1
    return pointer, acc


def part1(vals: list) -> int:
    return run(vals)[1]


def part2(vals: list) -> int:
    pointer, acc = run(vals)
    i, size = 0, len(vals)
    while pointer < size:
        while vals[i][0] == "acc":
            i += 1
        vals[i][0] = "jmp" if vals[i][0] == "nop" else "nop"
        pointer, acc = run(vals)
        vals[i][0] = "jmp" if vals[i][0] == "nop" else "nop"
        i += 1
    return acc


def main():
    file_input = parse_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


def test():
    test_input = parse_input([
        "nop +0",
        "acc +1",
        "jmp +4",
        "acc +3",
        "jmp -3",
        "acc -99",
        "acc +1",
        "jmp -4",
        "acc +6",
    ])
    assert part1(test_input) == 5
    assert part2(test_input) == 8


if __name__ == "__main__":
    test()
    main()
