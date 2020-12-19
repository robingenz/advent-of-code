def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l.strip() for l in f.readlines()]


def format_input(lines: list) -> dict:
    obj = {
        "rules": dict(),
        "tickets": []
    }
    for line in lines:
        if "-" in line:
            valid_nums = set()
            for val in line[line.find(":") + 2:].split(" or "):
                nums = [int(num) for num in val.split("-")]
                valid_nums.update(range(nums[0], nums[1] + 1))
            obj["rules"][line[:line.find(":")]] = valid_nums
        elif "," in line:
            obj["tickets"].append([int(num) for num in line.split(",")])
    return obj


def check_rules(rules: dict, num: int) -> bool:
    return any(num in nums for rule, nums in rules.items())


def discard_invalid_tickets(tickets: list, rules: dict) -> list:
    valid_tickets = []
    for ticket in tickets:
        if all(check_rules(rules, num) for num in ticket):
            valid_tickets.append(ticket)
    return valid_tickets


def get_possible_positions(tickets: list, rules: dict) -> dict:
    ticket_size = len(tickets[0])
    possible_positions = dict()
    for rule, nums in rules.items():
        possible_positions[rule] = []
        for i in range(ticket_size):
            if all(ticket[i] in nums for ticket in tickets):
                possible_positions[rule].append(i)
    return possible_positions


def determine_positions(possible_positions: dict) -> dict:
    positions = dict()
    while len(positions) < len(possible_positions):
        for rule, pos in possible_positions.items():
            if len(pos) == 1:
                val = pos[0]
                positions[rule] = val
                for rule, pos in possible_positions.items():
                    if val in pos:
                        pos.remove(val)
    return positions


def part1(obj: dict) -> int:
    error_rate = 0
    for ticket in obj["tickets"][1:]:
        error_rate += sum(
            num for num in ticket if not check_rules(obj["rules"], num))
    return error_rate


def part2(obj: dict) -> int:
    valid_nearby_tickets = discard_invalid_tickets(
        obj["tickets"][1:], obj["rules"])
    possible_positions = get_possible_positions(
        valid_nearby_tickets, obj["rules"])
    positions = determine_positions(possible_positions)
    result = 1
    for rule, pos in positions.items():
        if rule.startswith("departure"):
            result *= obj["tickets"][0][pos]
    return result


def main():
    file_input = format_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
