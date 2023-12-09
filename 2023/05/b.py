import re

with open ('input.txt') as f:
    lines = f.read().splitlines()

initial_seeds = list(map(int, re.findall('(\d+)', lines[0])))
locations = []
state = -1
maps = []
direct_mapping = False

# update initial seeds data structure
tmp = []
for seed_index in range(0, len(initial_seeds), 2):
    start_seed = initial_seeds[seed_index]
    seed_range = initial_seeds[seed_index + 1]
    tmp.append((start_seed, seed_range))
initial_seeds = tmp

# build data structure for state maps
for line in lines[1:]:
    if len(line) == 0:
        continue

    if not line[0].isnumeric():
        state += 1
        maps.append([])
        continue

    maps[state].append(list(map(int, re.findall('([\d-]+)', line))))

for state in range(len(maps)):
    new_ranges = []

    for start_seed, seed_range in initial_seeds:

        while seed_range > 0:
            min_value = seed_range
            found = False

            for dst, src, range in maps[state]:
                if start_seed >= src and start_seed < src + range:
                    diff = start_seed - src
                    remaining_range = min(range - diff, seed_range)
                    new_ranges.append((dst + diff, remaining_range))
                    start_seed += remaining_range
                    seed_range -= remaining_range
                    found = True                    
                    break
                elif start_seed < src:
                    min_value = min(src - start_seed, min_value)

            if not found:
                updated_range_value = min(min_value, seed_range)
                new_ranges.append((start_seed, updated_range_value))
                start_seed += updated_range_value
                seed_range -= updated_range_value

    initial_seeds = new_ranges

print(min(initial_seeds)[0])
