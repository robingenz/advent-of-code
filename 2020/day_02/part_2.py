with open('input.txt') as input_file:
    entries = input_file.readlines()

valid_pwd_num = 0
for entry in entries:
    pos1, pos2, letter, pwd = entry.replace(
        ': ', '-').replace(' ', '-').split('-')
    pos1 = int(pos1)
    pos2 = int(pos2)
    valid_pwd_num += (pwd[pos1-1] == letter and pwd[pos2-1] !=
                      letter) or (pwd[pos1-1] != letter and pwd[pos2-1] == letter)

print(valid_pwd_num)
