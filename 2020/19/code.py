import re


def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l.strip() for l in f.readlines()]


def parse_input(lines: list) -> dict:
    obj = {
        "rules": dict(),
        "messages": []
    }
    for line in lines:
        if ":" in line:
            parts = line.split(": ")
            obj["rules"][parts[0]] = [val.replace(
                "\"", "") for val in parts[1].split(" ")]
        else:
            obj["messages"].append(line)
    return obj


def generate_pattern(rules: dict, rule_no: str, depth: int = 0) -> str:
    if depth > 13:
        return ""
    pattern = "("
    for val in rules[rule_no]:
        if val.isnumeric():
            pattern += generate_pattern(rules, val, depth + 1)
        else:
            pattern += val
    pattern += ")"
    return pattern


def count_matches(pattern: str, messages: list) -> int:
    matches = 0
    for msg in messages:
        if re.fullmatch(pattern, msg):
            matches += 1
    return matches


def part1(obj: dict) -> int:
    pattern = generate_pattern(obj["rules"], "0")
    return count_matches(pattern, obj["messages"])


def part2(obj: dict) -> int:
    obj["rules"]["8"] = ["42", "|", "42", "8"]
    obj["rules"]["11"] = ["42", "31", "|", "42", "11", "31"]
    pattern = generate_pattern(obj["rules"], "0")
    return count_matches(pattern, obj["messages"])


def main():
    file_input = parse_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
