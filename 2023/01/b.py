from functools import reduce

f = open('input.txt', 'r')
lines = f.read().split('\n')

repls = {
    'one':   '1',
    'two':   '2',
    'three': '3',
    'four':  '4',
    'five':  '5',
    'six':   '6',
    'seven': '7',
    'eight': '8',
    'nine':  '9',
}

def find_in_line(part, index):
    for i, j in repls.items():
        if i in part:
            return j
        
    if line[index].isnumeric():
        return line[index]

    return None

def find_first(line):
    for index in range(0, len(line)):
        part = line[0:index]
        
        result = find_in_line(part, index)
        if result:
            return result

def find_last(line):
    for index in reversed(range(0, len(line))):
        part = line[index:]

        result = find_in_line(part, index)
        if result:
            return result

sum = 0
for line in lines:
    first = find_first(line)
    last = find_last(line)

    number = int(first + last)
    sum += number

print(sum)
