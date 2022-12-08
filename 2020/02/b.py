f = open('input.txt', 'r')
lines = [i.split() for i in f.read().splitlines()]

valid = 0
for policy in lines:
    pos1, pos2 = [int(i) - 1 for i in policy[0].split('-')]
    ch = policy[1][0]
    password = policy[2]
    if bool(password[pos1] == ch) ^ bool(password[pos2] == ch):
        valid += 1

print(valid)