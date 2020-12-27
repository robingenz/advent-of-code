def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l.strip() for l in f.readlines()]


def parse_input(lines: list) -> dict:
    return {
        "card": int(lines[0]),
        "door": int(lines[1]),
    }


def transform(val: int, subj_num: int) -> int:
    return (val * subj_num) % 20201227


def find_encryption_key(keys: dict, subj_num: int) -> int:
    loop_size, val = 0, 1
    while val != keys["card"]:
        val = transform(val, subj_num)
        loop_size += 1
    val = 1
    for _ in range(loop_size):
        val = transform(val, keys["door"])
    return val


def part1(keys: dict) -> int:
    return find_encryption_key(keys, 7)


def part2(keys: dict) -> int:
    return 0


def main():
    file_input = parse_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
