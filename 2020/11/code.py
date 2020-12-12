def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [list(l.strip()) for l in f.readlines()]


def get_num_of_occupied_seats(layout: list, row: int, col: int, adjacent: bool) -> int:
    direction_patterns = (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    )
    row_size, col_size = len(layout), len(layout[0])
    counter = 0
    for pattern in direction_patterns:
        dr, dc = row + pattern[0], col + pattern[1]
        while dr >= 0 and dr < row_size and dc >= 0 and dc < col_size:
            counter += layout[dr][dc] == "#"
            if layout[dr][dc] != "." or adjacent:
                break
            dr += pattern[0]
            dc += pattern[1]
    return counter


def apply_rules(layout: list, adjacent: bool) -> list:
    row_size, col_size = len(layout), len(layout[0])
    tolerance = 4 if adjacent else 5
    while True:
        changes = []
        for row in range(row_size):
            for col in range(col_size):
                if layout[row][col] == ".":
                    continue
                elif layout[row][col] == "L":
                    if get_num_of_occupied_seats(layout, row, col, adjacent) == 0:
                        changes.append((row, col, "#"))
                elif layout[row][col] == "#":
                    if get_num_of_occupied_seats(layout, row, col, adjacent) >= tolerance:
                        changes.append((row, col, "L"))
        if len(changes) < 1:
            break
        for change in changes:
            layout[change[0]][change[1]] = change[2]
    return layout


def part1(vals: list) -> int:
    final_layout = apply_rules(vals, True)
    return sum([row.count("#") for row in final_layout])


def part2(vals: list) -> int:
    final_layout = apply_rules(vals, False)
    return sum([row.count("#") for row in final_layout])


def main():
    print(f"Part 1: {part1(get_input())}")
    print(f"Part 2: {part2(get_input())}")


if __name__ == "__main__":
    main()
