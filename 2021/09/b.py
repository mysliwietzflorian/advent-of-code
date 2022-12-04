f = open('input.txt', 'r')
input = f.read().split('\n')

def in_bound(grid, x, y):
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]):
        return False
    return True

def is_low(grid, x, y):
    value = grid[y][x]
    for delta in [-1, 1]:
        if in_bound(grid, x + delta, y) and value >= grid[y][x + delta] or \
            in_bound(grid, x, y + delta) and value >= grid[y + delta][x]:
            return False
    return True

def expand_basin(grid, x, y):
    grid[y][x] = '9' # was now visited

    basin_size = 1
    for delta in [-1, 1]:
        if in_bound(grid, x + delta, y) and grid[y][x + delta] < '9':
            basin_size += expand_basin(grid, x + delta, y)
        if in_bound(grid, x, y + delta) and grid[y + delta][x] < '9':
            basin_size += expand_basin(grid, x, y + delta)
    return basin_size

# use grid[y][x] to access
grid = [[] for _ in range(len(input))]
for y in range(len(input)):
    grid[y] = [i for i in input[y]]

basin_sizes = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if is_low(grid, x, y):
            basin_sizes.append(expand_basin(grid, x, y))

basin_sizes.sort()
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
