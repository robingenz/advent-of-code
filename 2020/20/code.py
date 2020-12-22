from itertools import combinations


def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l.strip() for l in f.readlines() if l.strip()]


def parse_input(lines: list) -> dict:
    tiles = dict()
    for line in lines:
        if ":" in line:
            last_tile_id = int(line.replace("Tile ", "").replace(":", ""))
            tiles[last_tile_id] = {
                "id": last_tile_id,
                "data": list()
            }
        else:
            tiles[last_tile_id]["data"].append(
                line.replace("#", "1").replace(".", "0"))
    return tiles


def get_borders(tile_data: list) -> dict:
    borders = dict()
    borders["top"] = tile_data[0]
    borders["right"] = "".join([row[-1] for row in tile_data])
    borders["bottom"] = tile_data[-1]
    borders["left"] = "".join([row[0] for row in tile_data])
    return borders


def get_hashes(tiles: dict) -> dict:
    hashes = dict()
    for k, v in tiles.items():
        borders = get_borders(v["data"])
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
    for k, v in matches.items():
        matches[k] = set(v)
    return matches


def rotate(tile_data: list) -> list:
    return list(''.join(x[::-1]) for x in zip(*tile_data))


def flip(tile_data: list) -> list:
    return list(reversed(tile_data.copy()))


def get_tile_data_transformations(tile_data: list) -> list:
    tile_90 = rotate(tile_data)
    tile_180 = rotate(tile_90)
    tile_270 = rotate(tile_180)
    transformations = [tile_data, tile_90, tile_180, tile_270]
    transformations += [flip(t) for t in transformations]
    return transformations


def arrange_matches(tiles: dict, matches: dict) -> list:
    remaining = set(tiles.keys())
    result_size = int(len(tiles) ** 0.5)
    result = list([None for _ in range(result_size)]
                  for _ in range(result_size))
    for row in range(result_size):
        for col in range(result_size):
            if row in [0, result_size - 1] or col in [0, result_size - 1]:
                if (row == 0 or row == result_size - 1) and (col == 0 or col == result_size - 1):
                    possible_matches = {
                        k: v for k, v in matches.items() if len(v) == 2}
                else:
                    possible_matches = {
                        k: v for k, v in matches.items() if len(v) == 3}
            else:
                possible_matches = matches
            possible_matches = remaining.intersection(
                set(possible_matches.keys()))
            if row > 0 and col > 0:
                a = possible_matches.intersection(
                    matches[result[row - 1][col]["id"]])
                b = possible_matches.intersection(
                    matches[result[row][col - 1]["id"]])
                selected_match = list(a.intersection(b))[0]
            elif row > 0:
                selected_match = list(possible_matches.intersection(
                    matches[result[row - 1][col]["id"]]))[0]
            elif col > 0:
                selected_match = list(possible_matches.intersection(
                    matches[result[row][col - 1]["id"]]))[0]
            else:
                selected_match = list(possible_matches)[0]
            result[row][col] = {
                "id": selected_match,
                "data": None
            }
            remaining.remove(selected_match)

    dts_0 = get_tile_data_transformations(tiles[result[0][0]["id"]]["data"])
    dts_1 = get_tile_data_transformations(tiles[result[0][1]["id"]]["data"])
    dts_2 = get_tile_data_transformations(tiles[result[1][0]["id"]]["data"])
    for dt_0 in dts_0:
        borders_0 = get_borders(dt_0)
        for dt_1 in dts_1:
            borders_1 = get_borders(dt_1)
            for dt_2 in dts_2:
                borders_2 = get_borders(dt_2)
                if borders_0["right"] == borders_1["left"] and borders_0["bottom"] == borders_2["top"]:
                    result[0][0]["data"] = dt_0
                    break
        if result[0][0]["data"]:
            break

    for row in range(result_size):
        for col in range(result_size):
            if row == 0 and col == 0:
                continue
            dts = get_tile_data_transformations(
                tiles[result[row][col]["id"]]["data"])
            for dt in dts:
                borders = get_borders(dt)
                if row > 0 and col > 0:
                    top_borders = get_borders(result[row - 1][col]["data"])
                    left_borders = get_borders(result[row][col - 1]["data"])
                    if borders["left"] == left_borders["right"] and borders["top"] == top_borders["bottom"]:
                        result[row][col]["data"] = dt
                        break
                elif row > 0:
                    top_borders = get_borders(result[row - 1][col]["data"])
                    if borders["top"] == top_borders["bottom"]:
                        result[row][col]["data"] = dt
                        break
                elif col > 0:
                    left_borders = get_borders(result[row][col - 1]["data"])
                    if borders["left"] == left_borders["right"]:
                        result[row][col]["data"] = dt
                        break
    return result


def assemble(tiles: dict) -> dict:
    hashes = get_hashes(tiles)
    matches = match_hashes(hashes)
    return arrange_matches(tiles, matches)


def part1(tiles: dict) -> int:
    assembled_tiles = assemble(tiles)
    return (assembled_tiles[0][0]["id"]
            * assembled_tiles[0][-1]["id"]
            * assembled_tiles[-1][0]["id"]
            * assembled_tiles[-1][-1]["id"])


def part2(tiles: dict) -> int:
    return 0


def main():
    file_input = parse_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
