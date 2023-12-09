import math
import re

with open ('input.txt') as f:
    lines = f.read().splitlines()

instructions = lines[0]

paths = {}
for line in lines[2:]:
    match = re.match(r'(...) = \((...), (...)\)', line)
    paths.setdefault(match.group(1), ())
    paths[match.group(1)] = (match.group(2), match.group(3))

current = [i for i in paths.keys() if i[2] == 'A']
cycles = []

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

for c in current:
    steps = 0
    while c[2] != 'Z':
        for i in instructions:
            if i == 'L':
                c = paths[c][0]
            else:
                c = paths[c][1]

            steps += 1
            if c[2] == 'Z':
                break
    cycles.append(steps)

result = 1
for i in cycles:
    result = lcm(result, i)

print(result)
