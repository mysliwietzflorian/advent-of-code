f = open('input.txt', 'r')

lines = f.read().split('\n')

x = 0
y = 0
for line in lines:
    command, units = line.split(' ')
    units = int(units)
    if command == 'forward':
        x += units
    elif command == 'up':
        y -= units
    elif command == 'down':
        y += units

print(x * y)
