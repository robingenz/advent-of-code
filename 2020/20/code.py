def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l.strip() for l in f.readlines()]


def parse_input(lines: list) -> dict:
    tiles = dict()
    last_tile_id = ""
    for line in lines:
        if ":" in line:
            last_tile_id = line.replace("Tile ", "").replace(":", "")
            tiles[last_tile_id] = []
        else:
            tiles[last_tile_id].append(line)
    return tiles


def rotate(tile: dict, times: int) -> list:
    return []


def flip(tile: dict, dir: int) -> list:
    return []


def assemble(tiles: dict) -> dict:
    assembled_tiles = []

    return assembled_tiles


def part1(tiles: dict) -> int:
    assembled_tiles = assemble(tiles)
    return 0


def part2(tiles: list) -> int:
    return 0


def main():
    file_input = parse_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


def test():
    test_input = parse_input([])
    assert part1(test_input) == 0
    assert part2(test_input) == 0


if __name__ == "__main__":
    test()
    main()
