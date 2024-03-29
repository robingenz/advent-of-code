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
        (0, 0): False
    }
    for instruction in instructions:
        coords = (0, 0)
        for item in instruction:
            coords = (coords[0] + dirs[item][0], coords[1] + dirs[item][1])
        tiles[coords] = not tiles[coords] if coords in tiles else True
    return tiles


def get_neighbours(tile: tuple, tiles: dict) -> dict:
    neighbours, dirs = dict(), get_directions()
    for v in dirs.values():
        coord = (tile[0] + v[0], tile[1] + v[1])
        neighbours[coord] = tiles[coord] if coord in tiles else False
    return neighbours


def count_black_tiles(tiles) -> int:
    return len([v for v in tiles.values() if v == True])


def part1(instructions: list) -> int:
    tiles = run(instructions)
    return count_black_tiles(tiles)


def part2(instructions: list) -> int:
    tiles = run(instructions)
    for _ in range(100):
        updates = dict()
        for k, v in tiles.items():
            neighbours = get_neighbours(k, tiles)
            updates.update(neighbours)
        tiles.update(updates)
        for k, v in tiles.items():
            neighbours = get_neighbours(k, tiles)
            black_neighbours_size = len(
                [n for n in neighbours.values() if n == True])
            if v == True and (black_neighbours_size == 0 or black_neighbours_size > 2):
                updates[k] = False
            elif v == False and black_neighbours_size == 2:
                updates[k] = True
        tiles.update(updates)
    return count_black_tiles(tiles)


def main():
    file_input = parse_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
