import re

with open ('input.txt') as f:
    lines = f.read().splitlines()

def calc_combinations(input, hints):
    head = hints[0]
    tail = hints[1:]
    rest = sum(tail) + len(tail)

    count = 0
    for index in range(len(input) - rest - head + 1):
        if not '.' in input[index:index+head]:
            if len(tail) == 0 and '#' not in input[index+head:]:
                count += 1
            elif len(tail) > 0 and input[index+head] != '#':
                count += calc_combinations(input[index+head+1:], tail)

        if input[index] == '#':
            break

    return count

result = 0
for line in lines:
    input, hints = line.split()
    hints = list(map(int, re.findall('([-\d]+)', hints)))
    result += calc_combinations(input, hints)

print(result)
