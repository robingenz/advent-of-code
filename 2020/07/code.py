def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l[:-1] for l in f.readlines()]


def parse_input(lines: list) -> list:
    rules = []
    for line in lines:
        cnt_str = line.rstrip(".").replace("no other bags", "").replace(
            " bags", "").replace(" bag", "").split(" contain ")
        content = [content.split(" ", 1)
                   for content in cnt_str[1].split(", ") if cnt_str[1]]
        rule = {
            "color": cnt_str[0],
            "contents": [{"count": int(item[0]), "color": item[1]} for item in content],
        }
        rules.append(rule)
    return rules


def get_valid_bag_colors(color: str, bags: list) -> list:
    valid_bags = []
    for bag in bags:
        if color in (map(lambda c: c["color"], bag["contents"])):
            valid_bags.append(bag["color"])
    return valid_bags


def count_bags(color: str, bags: list, total: int) -> int:
    bag = next(x for x in bags if x["color"] == color)
    for content in bag["contents"]:
        total += content["count"] + content["count"] * \
            count_bags(content["color"], bags, 0)
    return total


def part1(vals: list) -> int:
    colors = ["shiny gold"]
    for color in colors:
        colors.extend(get_valid_bag_colors(color, vals))
    return len(set(colors)) - 1


def part2(vals: list) -> int:
    return count_bags("shiny gold", vals, 0)


def main():
    file_input = parse_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
