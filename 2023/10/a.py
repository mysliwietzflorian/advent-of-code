f = open('input.txt', 'r')
input = f.read().split('\n')

grid = [[] for _ in range(len(input))]
for y in range(len(input)):
    grid[y] = [i for i in input[y]]

pipes = {
    '|': [(0,-1), (0,1)],
    '-': [(-1,0), (1,0)],
    'L': [(0,-1), (1,0)],
    'J': [(0,-1), (-1,0)],
    '7': [(-1,0), (0,1)],
    'F': [(1,0), (0,1)],
}

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

steps = 1
start = find_start(grid)
last_position = [start, start]
current_pos = find_starting_neighbors(grid, start)

while current_pos[0] != current_pos[1]:
    for curr_index in range(2):
        curr = current_pos[curr_index]
        neighbors = find_neighbors(grid, curr)
        for n in neighbors:
            if n != last_position[curr_index]:
                last_position[curr_index] = curr
                current_pos[curr_index] = n
                break

    steps += 1

print(steps)
