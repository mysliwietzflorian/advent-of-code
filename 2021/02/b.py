f = open('input.txt', 'r')

lines = f.read().split('\n')

x = 0
y = 0
aim = 0
for line in lines:
    command, units = line.split(' ')
    units = int(units)
    if command == 'forward':
        x += units
        y += aim * units
    elif command == 'up':
        aim -= units
    elif command == 'down':
        aim += units

print(x * y)
