f = open('input.txt', 'r')
input = f.read().split('\n')

def in_bound(grid, x, y):
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]):
        return False
    return True

def is_low(grid, x, y):
    value = grid[y][x]
    if in_bound(grid, x-1, y) and value >= grid[y][x-1] or \
        in_bound(grid, x+1, y) and value >= grid[y][x+1] or \
        in_bound(grid, x, y-1) and value >= grid[y-1][x] or \
        in_bound(grid, x, y+1) and value >= grid[y+1][x]:
        return False
    return True

# use grid[y][x] to access
# + x
# y

grid = [[] for _ in range(len(input))]
for y in range(len(input)):
    grid[y] = [i for i in input[y]]

risk = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if is_low(grid, x, y):
            risk += int(grid[y][x]) + 1

print(risk)
