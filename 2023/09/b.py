import re

with open ('input.txt') as f:
    lines = f.read().splitlines()

def is_empty(list):
    for i in list:
        if i != 0:
            return False
    return True

sum = 0
for line in lines:
    sequence = list(map(int, re.findall('([\d-]+)', line)))
    sequence = list(reversed(sequence))

    stack = []
    current = sequence
    while not is_empty(current):
        stack.append(current)
        diff = [current[i + 1] - current[i] for i in range(len(current) - 1)]
        current = diff

    value = 0
    for i in reversed(range(len(stack))):
        value += stack[i][-1]
    sum += value

print(sum)
