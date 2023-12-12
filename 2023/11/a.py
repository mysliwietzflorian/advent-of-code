f = open('input.txt', 'r')
input = f.read().split('\n')

grid = [[] for _ in range(len(input))]
for y in range(len(input)):
    grid[y] = [i for i in input[y]]

def in_bound(grid, point):
    x, y = point
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]):
        return False
    return True

def print_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], sep='', end='')
        print()
    print()

def find_empty_rows(grid):
    result = []
    for y in range(len(grid)):
        found = False
        for x in range(len(grid[y])):
            if grid[y][x] == '#':
                found = True
                break

        if not found:
            result.append(y)
    return result

def find_empty_cols(grid):
    result = []
    for x in range(len(grid[0])):
        found = False
        for y in range(len(grid)):
            if grid[y][x] == '#':
                found = True
                break

        if not found:
            result.append(x)
    return result

empty_rows = find_empty_rows(grid)
empty_cols = find_empty_cols(grid)

def find_distance(p1, p2):
    raw_distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    min_p = (min(p1[0], p2[0]), min(p1[1], p2[1]))
    max_p = (max(p1[0], p2[0]), max(p1[1], p2[1]))

    extra_rows = len(list(filter(lambda x: x >= min_p[0] and x <= max_p[0], empty_cols)))
    extra_cols = len(list(filter(lambda y: y >= min_p[1] and y <= max_p[1], empty_rows)))
    
    return raw_distance + extra_cols + extra_rows

print_grid(grid)
galaxies = []

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == '#':
            galaxies.append((x, y))

sum = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        sum += find_distance(galaxies[i], galaxies[j])

print(sum)
