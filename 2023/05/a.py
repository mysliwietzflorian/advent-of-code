import re

with open ('input.txt') as f:
    lines = f.read().splitlines()

initial_seeds = list(map(int, re.findall('(\d+)', lines[0])))
locations = []
state = -1
maps = []
direct_mapping = False

for line in lines[1:]:
    if len(line) == 0:
        continue

    if not line[0].isnumeric():
        state += 1
        maps.append([])
        continue

    maps[state].append(list(map(int, re.findall('(\d+)', line))))

for seed in initial_seeds:
    current_value = seed

    for state in range(7):
        index = 0
        direct_mapping = False
        current_map = maps[state][index]

        while current_value < current_map[1] or current_value >= current_map[1] + current_map[2]:
            index += 1
            if index >= len(maps[state]):
                direct_mapping = True
                break

            current_map = maps[state][index]

        if not direct_mapping:
            diff = current_value - current_map[1]
            current_value = current_map[0] + diff

    locations.append(current_value)

print(min(locations))
