from copy import deepcopy
import math
import re

with open ('input.txt') as f:
    workflows_raw, _ = f.read().split('\n\n')

workflows = {}

for w in workflows_raw.split('\n'):
    m = re.match(r'(\w+){(.*)}', w)
    name = m.group(1)
    workflows[name] = []

    for config in m.group(2).split(','):
        config = config.split(':')
        if len(config) == 1:
            workflows[name].append((config[0], None))
        else:
            workflows[name].append((config[1], config[0]))

def solve(name, rule_index, ranges):
    if name == 'A':
        return math.prod([i[1] - i[0] for i in ranges])
    elif name == 'R':
        return 0

    rule = workflows[name][rule_index]

    if rule[1] is None:
        return solve(rule[0], 0, ranges)

    m = re.match(r'(\w)(.)(\d+)', rule[1])
    part_index = 'xmas'.index(m.group(1))
    operator = m.group(2)
    value = int(m.group(3))

    range_low = deepcopy(ranges)
    range_high = deepcopy(ranges)

    result = 0
    if operator == '<':
        range_low[part_index] = (ranges[part_index][0], value - 1)
        range_high[part_index] = (value - 1, ranges[part_index][1])

        result += solve(rule[0], 0, range_low)
        result += solve(name, rule_index + 1, range_high)
    else:
        range_low[part_index] = (ranges[part_index][0], value)
        range_high[part_index] = (value, ranges[part_index][1])

        result += solve(rule[0], 0, range_high)
        result += solve(name, rule_index + 1, range_low)

    return result

print(solve('in', 0, [(0, 4000), (0, 4000), (0, 4000), (0, 4000)]))
