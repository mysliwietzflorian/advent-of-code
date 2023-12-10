from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

f = open('input.txt', 'r')
input = f.read().split('\n')

grid = [[] for _ in range(len(input))]
clone = [[] for _ in range(len(input))]
for y in range(len(input)):
    grid[y] = [i for i in input[y]]
    clone[y] = [' ' for _ in input[y]]

pipes = {
    '|': [(0,-1), (0,1)],
    '-': [(-1,0), (1,0)],
    'L': [(0,-1), (1,0)],
    'J': [(0,-1), (-1,0)],
    '7': [(-1,0), (0,1)],
    'F': [(1,0), (0,1)],
}

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

def find_connecting_pipes(ch):
    if ch not in pipes:
        return None
    return pipes[ch]

def is_connected_pipe(grid, p1, p2):
    diff = (p2[0] - p1[0], p2[1] - p1[1])
    inv_diff = (-diff[0], -diff[1])
    c1 = find_connecting_pipes(grid[p1[1]][p1[0]])
    c2 = find_connecting_pipes(grid[p2[1]][p2[0]])

    if c1 is None or c2 is None:
        return False

    return diff in c1 and inv_diff in c2

def find_neighbors(grid, point):
    deltas = [(-1,0),(0,-1),(1,0),(0,1)]
    result = []

    for d in deltas:
        neighbor = (point[0] + d[0], point[1] + d[1])
        if not in_bound(grid, neighbor):
            continue

        if is_connected_pipe(grid, point, neighbor):
            result.append(neighbor)
    return result

def find_starting_neighbors(grid, start):
    deltas = [(-1,0),(0,-1),(1,0),(0,1)]
    result = []

    for d in deltas:
        neighbor = (start[0] + d[0], start[1] + d[1])
        if not in_bound(grid, neighbor):
            continue

        connecting = find_connecting_pipes(grid[neighbor[1]][neighbor[0]])
        if connecting is None:
            continue

        if (-d[0], -d[1]) in connecting:
            result.append(neighbor)
    return result

def find_start(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                return (x, y)
    return None

start = find_start(grid)
last_position = start
starting_neighbors = find_starting_neighbors(grid, start)
curr = starting_neighbors[0]
loop = [start, starting_neighbors[0], starting_neighbors[1]]

while curr != starting_neighbors[1]:
    neighbors = find_neighbors(grid, curr)
    for n in neighbors:
        if n != last_position:
            last_position = curr
            curr = n
            break
    loop.append(curr)
    clone[curr[1]][curr[0]] = '#'

clone[start[1]][start[0]] = '#'
clone[starting_neighbors[0][1]][starting_neighbors[0][0]] = '#'

polygon = Polygon(loop)
inside = 0

for y in range(len(clone)):
    for x in range(len(clone[y])):
        value = clone[y][x]
        if value == '#':
            continue

        point = Point(x, y)
        if polygon.contains(point):
            clone[y][x] = '.'
            inside += 1

print(inside)
