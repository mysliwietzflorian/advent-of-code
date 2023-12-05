import re

with open ('input.txt') as f:
    lines = f.read().splitlines()

sum = 0
for line in lines:
    m = re.match('.*: ([\d ]+) \| ([\d ]+)', line)
    winning = list(map(int, re.findall('(\d+)', m.group(1))))
    yours = list(map(int, re.findall('(\d+)', m.group(2))))
    
    count = 0
    for nr in yours:
        if nr in winning:
            count += 1

    if count > 0:
        sum += 2 ** (count - 1)

print(sum)
