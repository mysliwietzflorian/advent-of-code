f = open('input.txt', 'r')
lines = [i.split() for i in f.read().splitlines()]

valid = 0
for policy in lines:
    c_from, c_to = [int(i) for i in policy[0].split('-')]
    ch = policy[1][0]
    password = policy[2]
    if c_from <= password.count(ch) <= c_to:
        valid += 1

print(valid)