
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


def get_directions() -> dict:
    return {"e": (2, 0), "se": (1, -1), "sw": (-1, -1),
            "w": (-2, 0), "nw": (-1, 1), "ne": (1, 1)}


def run(instructions: list) -> dict:
    dirs = get_directions()
    tiles = {
        (0, 0): True
    }
    for instruction in instructions:
        coords = (0, 0)
        for item in instruction:
            coords = (coords[0] + dirs[item][0], coords[1] + dirs[item][1])
        tiles[coords] = not tiles[coords] if coords in tiles else False
    return tiles


def get_neighbours(tile: tuple, tiles: dict) -> dict:
    neighbours, dirs = dict(), get_directions()
    for v in dirs.values():
        coord = (tile[0] + v[0], tile[1] + v[1])
        neighbours[coord] = tiles[coord] if coord in tiles else True
    return neighbours


def part1(instructions: list) -> int:
    tiles = run(instructions)
    return len([v for v in tiles.values() if v == False])


def part2(instructions: list) -> int:
    tiles = run(instructions)
    for _ in range(100):
        updates = dict()
        for k, v in tiles.items():
            neighbours = get_neighbours(k, tiles)
            updates.update(neighbours)
            black_neighbours_size = len(
                [n for n in neighbours.values() if n == False])
            if v == False and (black_neighbours_size == 0 or black_neighbours_size > 2):
                updates[k] = True
            elif v == True and black_neighbours_size == 2:
                updates[k] = False
        tiles.update(updates)
    return len([v for v in tiles.values() if v == False])


def main():
    file_input = parse_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
