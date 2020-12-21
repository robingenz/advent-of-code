def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l.strip().replace(" = ", " ").replace("mem[", "").replace("]", "") for l in f.readlines()]


def parse_input(lines: list) -> list:
    instructions = []
    for line in lines:
        if line.startswith('mask'):
            instructions.append([line.split()[1], []])
            continue
        instructions[-1][1].append([int(i) for i in line.split()])
    return instructions


def part1(instructions: list) -> int:
    results = dict()
    for instr in instructions:
        mask_and = int(instr[0].replace("X", "1"), 2)
        mask_or = int(instr[0].replace("X", "0"), 2)
        for mem in instr[1]:
            results[mem[0]] = (mem[1] | mask_or) & mask_and
    return sum(results.values())


def part2(instructions: list) -> int:
    results = dict()
    for instr in instructions:
        mask_or = int(instr[0].replace("X", "0"), 2)
        for mem in instr[1]:
            addrs = [mem[0] | mask_or]
            idxs = [i for i, val in enumerate(
                reversed(instr[0])) if val == "X"]
            for idx in idxs:
                tmp = [addr | (1 << idx) for addr in addrs]
                tmp += [addr & ~(1 << idx) for addr in addrs]
                addrs = tmp
            for addr in addrs:
                results[addr] = mem[1]
    return sum(results.values())


def main():
    file_input = parse_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
