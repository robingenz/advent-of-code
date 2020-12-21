def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return [l.strip().replace("(", "( ").replace(")", " )").split(" ") for l in f.readlines()]


def parse_input(lines: list) -> list:
    for i, j in enumerate(lines):
        for x, y in enumerate(j):
            if y.isnumeric():
                lines[i][x] = int(y)
    return lines


def solve_without_parentheses(expression: list, precedence_operator: str = None) -> int:
    if len(expression) == 1:
        return expression[0]
    if precedence_operator in expression:
        num = expression.count(precedence_operator)
        for _ in range(num):
            idx = expression.index(precedence_operator)
            expression[idx - 1] = solve_without_parentheses(
                expression[idx - 1:idx + 2], None)
            del expression[idx:idx + 2]
        return solve_without_parentheses(expression, None)
    if expression[1] == "+":
        expression[0] = expression[0] + expression[2]
    else:
        expression[0] = expression[0] * expression[2]
    del expression[1:3]
    return solve_without_parentheses(expression, None)


def solve(expression: list, precedence_operator: str = None) -> int:
    expression = expression[:]
    num_parentheses = expression.count("(")
    for _ in range(num_parentheses):
        start = len(expression) - expression[::-1].index("(") - 1
        end = expression.index(")", start)
        expression[start] = solve_without_parentheses(
            expression[start + 1:end], precedence_operator)
        del expression[start + 1:end + 1]
    return solve_without_parentheses(expression, precedence_operator)


def part1(vals: list) -> int:
    return sum(solve(exp, None) for exp in vals)


def part2(vals: list) -> int:
    return sum(solve(exp, "+") for exp in vals)


def main():
    file_input = parse_input(get_input())
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")


if __name__ == "__main__":
    main()
