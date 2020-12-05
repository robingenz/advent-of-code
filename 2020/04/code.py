import re


def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        vals = []
        for l in f.read().split("\n\n"):
            vals.append({})
            for group in l.replace("\n", " ").strip().split(" "):
                group = group.split(":")
                vals[-1][group[0]] = group[1]
        return vals


def validate_passport(passport: dict, strict: bool) -> bool:
    patterns = {
        "byr": "19[2-9][0-9]|200[0-2]",
        "iyr": "20(1[0-9]|20)",
        "eyr": "20(2[0-9]|30)",
        "hgt": "1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in",
        "hcl": "#[0-9a-f]{6}",
        "ecl": "amb|blu|brn|gry|grn|hzl|oth",
        "pid": "[0-9]{9}"
    }
    if not all(x in passport for x in patterns.keys()):
        return False
    if not strict:
        return True
    for key, val in patterns.items():
        if not re.fullmatch(val, passport[key]):
            return False
    return True


def part1(vals: list) -> int:
    counter = 0
    for passport in vals:
        counter += validate_passport(passport, False)
    return counter


def part2(vals: list) -> int:
    counter = 0
    for passport in vals:
        counter += validate_passport(passport, True)
    return counter


def main():
    file_input = get_input()
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
