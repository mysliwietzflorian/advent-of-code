with open ('input.txt') as f:
    input = f.read().splitlines()

MAX_STEPS = 1_000_000_000

grid = [[] for _ in range(len(input))]
for y in range(len(input)):
    grid[y] = [i for i in input[y]]

def print_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], sep='', end=' ')
        print()
    print()

def calc_load(grid):
    result = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == 'O':
                result += len(grid) - y
    return result

def rotate(grid):
    result = [[] for _ in range(len(grid[0]))]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            result[y].append(grid[len(grid) - x - 1][y])
    return result

def step(grid):
    for x in range(len(grid[0])):
        last_fixpoint = 0
        for y in range(len(grid)):
            value = grid[y][x]
            if value == 'O':
                if y != last_fixpoint:
                    grid[y][x] = '.'
                    grid[last_fixpoint][x] = 'O'
                last_fixpoint += 1

            elif value == '#':
                last_fixpoint = y + 1
    return grid

def calc_hash(grid):
    hash = ''
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            hash += str(grid[y][x])
    return hash

cache = {}
cycle = 0
while True:
    hash = calc_hash(grid)

    if hash in cache:
        initial_cycle = cache[hash]
        if (MAX_STEPS - initial_cycle) % (cycle - initial_cycle) == 0:
            print(calc_load(grid))
            exit()

    cache[hash] = cycle
    cycle += 1
    for _ in range(4):
        grid = step(grid)
        grid = rotate(grid)
