import re

with open ('input.txt') as f:
    lines = f.read().splitlines()

copies_dict = {}

sum = 0
for line in lines:
    m = re.match('[^\d]*(\d+): ([\d ]+) \| ([\d ]+)', line)
    gameNr = int(m.group(1))
    winning = list(map(int, re.findall('(\d+)', m.group(2))))
    yours = list(map(int, re.findall('(\d+)', m.group(3))))

    count = 0
    for nr in yours:
        if nr in winning:
            count += 1

    current_copies = list(range(gameNr + 1, gameNr + 1 + count))
    for c in current_copies:
        copies_dict[c] = copies_dict.setdefault(c, 0) + 1
    sum += 1

    copies_dict.setdefault(gameNr, 0)
    while copies_dict.get(gameNr) > 0:
        for c in current_copies:
            copies_dict[c] = copies_dict.setdefault(c, 0) + 1
        
        sum += 1
        copies_dict[gameNr] = copies_dict.get(gameNr) - 1

print(sum)
