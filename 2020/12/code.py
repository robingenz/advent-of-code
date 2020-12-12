def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l.strip() for l in f.readlines()]


def format_input(lines: list) -> list:
    return lines


def part1(vals: list) -> int:
    x, y, orientation = 0, 0, 90
    for instruction in vals:
        action = instruction[:1]
        value = int(instruction[1:])
        if action == "N":
            y += value
        elif action == "S":
            y -= value
        elif action == "E":
            x += value
        elif action == "W":
            x -= value
        elif action == "L":
            orientation = (360 + (orientation - value)) % 360
        elif action == "R":
            orientation = (orientation + value) % 360
        elif action == "F":
            if orientation == 0:
                y += value
            elif orientation == 180:
                y -= value
            elif orientation == 90:
                x += value
            elif orientation == 270:
                x -= value
    return abs(x) + abs(y)


def part2(vals: list) -> int:
    ship, waypoint = [0, 0], [10, 1]
    for instruction in vals:
        action = instruction[:1]
        value = int(instruction[1:])
        if action == "N":
            waypoint[1] += value
        elif action == "S":
            waypoint[1] -= value
        elif action == "E":
            waypoint[0] += value
        elif action == "W":
            waypoint[0] -= value
        elif action == "L" or action == "R":
            for _ in range(0, value // 90):
                if action == "L":
                    tmp = waypoint[0]
                    waypoint[0] = -waypoint[1]
                    waypoint[1] = tmp
                else:
                    tmp = waypoint[0]
                    waypoint[0] = waypoint[1]
                    waypoint[1] = -tmp
        elif action == "F":
            ship[1] += waypoint[1] * value
            ship[0] += waypoint[0] * value
    return abs(ship[0]) + abs(ship[1])


def main():
    file_input = format_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


def test():
    test_input = format_input([
        "F10",
        "N3",
        "F7",
        "R90",
        "F11"
    ])
    assert part1(test_input) == 25
    assert part2(test_input) == 286


if __name__ == "__main__":
    test()
    main()
