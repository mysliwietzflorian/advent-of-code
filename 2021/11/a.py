f = open('input.txt', 'r')
input = f.read().split('\n')

grid = [[] for _ in range(len(input))]
for y in range(len(input)):
    grid[y] = [int(i) for i in input[y]]
flashes = []

def in_bound(grid, x, y):
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]):
        return False
    return True

def trigger_flash(grid, x, y):
    grid[y][x] = '#'

    for delta_x in range(-1, 2):
        for delta_y in range(-1, 2):
            if delta_x == 0 and delta_y == 0:
                continue

            if in_bound(grid, x+delta_x, y+delta_y) and grid[y+delta_y][x+delta_x] != '#':
                grid[y+delta_y][x+delta_x] += 1
                if grid[y+delta_y][x+delta_x] > 9 and [x+delta_x, y+delta_y] not in flashes:
                    flashes.append([x+delta_x, y+delta_y])

count = 0
for gen in range(1, 101):
    flashes.clear()

    # initially increase all states by one and mark flashes
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] = grid[y][x] + 1
            if grid[y][x] > 9:
                flashes.append([x, y])

    # iterate through all open flashes
    while len(flashes) > 0:
        coord = flashes.pop(0)
        trigger_flash(grid, coord[0], coord[1])

    # reset flashed states to 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '#':
                grid[y][x] = 0
                count += 1

print(count)
