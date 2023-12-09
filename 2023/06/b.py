import re
from functools import reduce

with open ('input.txt') as f:
    lines = f.read().splitlines()

time = int(reduce(lambda a, b: a+b, re.findall('(\d+)', lines[0])))
distance = int(reduce(lambda a, b: a+b, re.findall('(\d+)', lines[1])))

count = 0
for speed in range(0, time + 1):
    if speed * (time - speed) > distance:
        count += 1

print(count)
