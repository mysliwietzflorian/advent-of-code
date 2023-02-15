with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

cycle = 0
x = 1

def inc_cycle(n):
    global cycle

    for i in range(n):
        pixel_nr = cycle % 40
        
        if pixel_nr >= x - 1 and pixel_nr <= x + 1:
            print('#', sep='', end='')
        else:
            print('.', sep='', end='')

        if pixel_nr == 39:
            print()
        cycle += 1

for line in lines:
    if line.split()[0] == 'noop':
        inc_cycle(1)
    else:
        inc_cycle(2)
        x += int(line.split()[1])
