def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l.strip() for l in f.readlines()]


def format_input(lines: list) -> dict:
    obj = {
        "ranges": [],
        "tickets": []
    }
    for line in lines:
        if "-" in line:
            ranges = []
            for val in line[line.find(":") + 2:].split(" or "):
                ranges.append([int(num) for num in val.split("-")])
            obj["ranges"].extend(ranges)
        elif "," in line:
            obj["tickets"].append([int(num) for num in line.split(",")])
    return obj


def part1(obj: dict) -> int:
    error_rate = 0
    for ticket in obj["tickets"][1:]:
        for val in ticket:
            error = True
            for r in obj["ranges"]:
                if val >= r[0] and val <= r[1]:
                    error = False
                    break
            if error:
                error_rate += val
    return error_rate


def part2(obj: dict) -> int:
    return 0


def main():
    file_input = format_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
