import re

with open ('input.txt') as f:
    lines = f.read().splitlines()

max_dict = {
    'red': 0,
    'green': 0,
    'blue': 0,
}

sum = 0

for line in lines:
    max_dict['red'] = 0
    max_dict['green'] = 0
    max_dict['blue'] = 0

    first, second = line.split(': ')
    gameId = int(first[5:])
    
    subparts = second.split('; ')
    for sp in subparts:
        for p in sp.split(', '):
            nr, color = p.split(' ')
            nr = int(nr)
            if max_dict[color] < nr:
                max_dict[color] = nr   

    sum += max_dict['red'] * max_dict['green'] * max_dict['blue']

print(sum)
