from itertools import combinations


def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l.strip() for l in f.readlines() if l.strip()]


def parse_input(lines: list) -> dict:
    tiles = dict()
    for line in lines:
        if ":" in line:
            last_tile_id = line.replace("Tile ", "").replace(":", "")
            tiles[last_tile_id] = {"data": list(),
                                   "pos": (None, None)}
        else:
            tiles[last_tile_id]["data"].append(
                line.replace("#", "1").replace(".", "0"))
    return tiles


def get_borders(tile: dict) -> dict:
    borders = dict()
    borders["top"] = tile["data"][0]
    borders["right"] = "".join([row[-1] for row in tile["data"]])
    borders["bottom"] = tile["data"][-1]
    borders["left"] = "".join([row[0] for row in tile["data"]])
    return borders


def get_hashes(tiles: dict) -> dict:
    hashes = dict()
    for k, v in tiles.items():
        borders = get_borders(v)
        h = list(borders.values())
        h += [x[::-1] for x in h[:]]
        hashes[k] = set([int(x, 2) for x in h])
    return hashes


def match_hashes(hashes: dict) -> dict:
    matches = dict()
    for (x, y), (i, j) in combinations(hashes.items(), 2):
        result = y.intersection(j)
        if result:
            matches[x] = matches.get(x, []) + [i]
            matches[i] = matches.get(i, []) + [x]
    return matches


# def arrange_matches(tiles: dict, matches: dict) -> list:
#     for k, v in matches.items():
#         if len(v) == 2:
#             tiles[k]["pos"] = (0, 0)
#             break
#     return tiles


def rotate(tile: dict, times: int) -> dict:
    return []


def flip(tile: dict, dir: int) -> dict:
    return []


def assemble(tiles: dict) -> dict:
    assembled_tiles = []
    hashes = get_hashes(tiles)
    matches = match_hashes(hashes)
    print(matches)
    # tiles = arrange_matches(tiles, matches)
    # print(tiles)
    return tiles


def part1(tiles: dict) -> int:
    assembled_tiles = assemble(tiles)
    return 0
    # return (assembled_tiles[0][0]
    #         * assembled_tiles[0][-1]
    #         * assembled_tiles[-1][0]
    #         * assembled_tiles[-1][-1])


def part2(tiles: dict) -> int:
    return 0


def main():
    file_input = parse_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
