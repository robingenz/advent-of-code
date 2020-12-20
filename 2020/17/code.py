from itertools import product
import operator


def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l.strip() for l in f.readlines()]


def format_input(lines: list) -> dict:
    state = dict()
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            state[(i, j)] = char
    return state


def simulate(state: dict, cycles: int, dimensions: int) -> int:
    curr_state = dict()
    for key, _ in state.items():
        new_key = list(key)
        for _ in range(2, dimensions):
            new_key.append(0)
        curr_state[tuple(new_key)] = state[key]
    for _ in range(cycles):
        for key in list(curr_state):
            for p in product([-1, 0, 1], repeat=dimensions):
                i = tuple(map(operator.add, key, p))
                if i not in curr_state:
                    curr_state[i] = '.'
        next_state = dict()
        for key, val in curr_state.items():
            count = 0
            for p in product([-1, 0, 1], repeat=dimensions):
                i = tuple(map(operator.add, key, p))
                if key == i or i not in curr_state:
                    continue
                if curr_state[i] == "#":
                    count += 1
            if val == '#' and (count == 2 or count == 3):
                next_state[key] = '#'
            elif val == '.' and count == 3:
                next_state[key] = '#'
            else:
                next_state[key] = '.'
        curr_state = next_state
    return len([val for _, val in curr_state.items() if val == "#"])


def part1(state: dict) -> int:
    return simulate(state, 6, 3)


def part2(state: dict) -> int:
    return simulate(state, 6, 4)


def main():
    file_input = format_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
