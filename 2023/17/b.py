from heapq import heappop, heappush

with open ('input.txt') as f:
    input = f.read().splitlines()

def print_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], sep='', end='')
        print()
    print()

def in_bound(grid, point):
    x, y = point
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]):
        return False
    return True

def get_possible_neighbors(dir):
    if dir[0] == 0:
        return [(1,0), (-1,0)]
    else:
        return [(0,1), (0,-1)]

grid = [[] for _ in range(len(input))]
for y in range(len(input)):
    grid[y] = [i for i in input[y]]

visited = set()
open = [(0, (0,0), (1,0)), (0, (0,0), (0,1))] # current value, position, direction
goal = (len(grid[0]) - 1, len(grid) - 1)

min_dist = 4
max_dist = 10

while open:
    value, pos, dir = heappop(open)

    if pos == goal:
        print(value)
        break
    if (pos, dir) in visited:
        continue
    visited.add((pos, dir))

    for new_dir in get_possible_neighbors(dir):
        for step in range(min_dist, max_dist+1):
            new_pos = (pos[0] + new_dir[0] * step, pos[1] + new_dir[1] * step)
            if not in_bound(grid, new_pos):
                break

            cost = 0
            for i in range(1, step+1):
                cost += int(grid[pos[1] + new_dir[1] * i][pos[0] + new_dir[0] * i])
            new_value = value + cost
            heappush(open, (new_value, new_pos, new_dir))
