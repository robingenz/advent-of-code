with open('input.txt') as input_file:
    entries = input_file.readlines()

valid_pwd_num = 0
for entry in entries:
    lowest, highest, letter, pwd = entry.replace(
        ': ', '-').replace(' ', '-').split('-')
    lowest = int(lowest)
    highest = int(highest)
    cnt = pwd.count(letter)
    valid_pwd_num += cnt >= lowest and cnt <= highest

print(valid_pwd_num)
