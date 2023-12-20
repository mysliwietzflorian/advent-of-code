import re

with open ('input.txt') as f:
    workflows_raw, parts_raw = f.read().split('\n\n')

def parse_config(config):
    c = config.split(':')
    if len(c) == 1:
        return f'lambda x: "{c[0]}"'

    c[0] = c[0].replace('x', 'x[0]').replace('m', 'x[1]').replace('a', 'x[2]').replace('s', 'x[3]')
    return f'lambda x: "{c[1]}" if {c[0]} else None'

def traverse(workflows, part):
    curr = workflows['in']

    while True:
        for w in curr:
            result = eval(w)(part)
            if result == 'A':
                return sum(part)
            elif result == 'R':
                return 0
            elif result:
                curr = workflows[result]
                break

workflows = {}

for w in workflows_raw.split('\n'):
    m = re.match(r'(\w+){(.*)}', w)
    name = m.group(1)
    workflows[name] = []
    for config in m.group(2).split(','):
        workflows[name].append(parse_config(config))

result = 0
for part in parts_raw.split('\n'):
    part = tuple(map(int, re.findall(r'(\d+)', part)))
    if not part:
        continue

    result += traverse(workflows, part)

print(result)
