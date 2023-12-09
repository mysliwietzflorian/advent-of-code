import re

with open ('input.txt') as f:
    lines = f.read().splitlines()

times = list(map(int,re.findall('(\d+)', lines[0])))
distances = list(map(int,re.findall('(\d+)', lines[1])))

prod = 1
for race in range(len(times)):
    count = 0
    for speed in range(0, times[race] + 1):
        if speed * (times[race] - speed) > distances[race]:
            count += 1
    
    prod *= count

print(prod)
