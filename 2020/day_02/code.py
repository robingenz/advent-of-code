def get_input() -> list:
    with open(f"{__file__.rstrip('code.py')}input.txt") as f:
        return f.readlines()

def part1(vals: list) -> int:
    valid_pwd_num = 0
    for val in vals:
        lowest, highest, letter, pwd = val.replace(
            ': ', '-').replace(' ', '-').split('-')
        lowest = int(lowest)
        highest = int(highest)
        cnt = pwd.count(letter)
        valid_pwd_num += cnt >= lowest and cnt <= highest
    return valid_pwd_num

def part2(vals: list) -> int:
    valid_pwd_num = 0
    for val in vals:
        pos1, pos2, letter, pwd = val.replace(
            ': ', '-').replace(' ', '-').split('-')
        pos1 = int(pos1)
        pos2 = int(pos2)
        valid_pwd_num += (pwd[pos1-1] == letter and pwd[pos2-1] !=
                        letter) or (pwd[pos1-1] != letter and pwd[pos2-1] == letter)
    return valid_pwd_num

def main():
    file_input = get_input()
    print(f"Part 1: {part1(file_input)}")
    print(f"Part 2: {part2(file_input)}")

if __name__ == "__main__":
    main()