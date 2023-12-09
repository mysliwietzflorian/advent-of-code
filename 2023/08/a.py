import re

with open ('input.txt') as f:
    lines = f.read().splitlines()

instructions = lines[0]

paths = {}
for line in lines[2:]:
    match = re.match(r'(...) = \((...), (...)\)', line)
    paths.setdefault(match.group(1), ())
    paths[match.group(1)] = (match.group(2), match.group(3))

current = 'AAA'
steps = 0
while current != 'ZZZ':
    for i in instructions:
        if i == 'L':
            current = paths[current][0]
        else:
            current = paths[current][1]

        steps += 1
        if current == 'ZZZ':
            break

print(steps)
