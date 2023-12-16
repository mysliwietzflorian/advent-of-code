f = open('input.txt', 'r')
input = f.read().split('\n')

mirrors = {
    '|': {
        (1,0): [(0,-1),(0,1)],
        (-1,0): [(0,-1),(0,1)],
        (0,1): [(0,1)],
        (0,-1): [(0,-1)],
    },
    '-': {
        (1,0): [(1,0)],
        (-1,0): [(-1,0)],
        (0,1): [(-1,0),(1,0)],
        (0,-1): [(-1,0),(1,0)],
    },
    '/': {
        (1,0): [(0,-1)],
        (-1,0): [(0,1)],
        (0,1): [(-1,0)],
        (0,-1): [(1,0)],
    },
    '\\': {
        (1,0): [(0,1)],
        (-1,0): [(0,-1)],
        (0,1): [(1,0)],
        (0,-1): [(-1,0)],
    },
}

def in_bound(grid, point):
    x, y = point
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]):
        return False
    return True

grid = [[] for _ in range(len(input))]
for y in range(len(input)):
    grid[y] = [i for i in input[y]]

pos = (0, 0)
dir = (1, 0)
visited = {}
splits = []

while True:
    update = False

    if in_bound(grid, pos):
        if pos not in visited:
            visited[pos] = []
        if dir not in visited[pos]:
            visited[pos].append(dir)
        else:
            update = True
    else:
        update = True

    if update:
        if len(splits) == 0:
            break
        else:
            config = splits.pop()
            dir = config[1]
            pos = (config[0][0] + dir[0], config[0][1] + dir[1])
            continue

    value = grid[pos[1]][pos[0]]

    if value != '.':
        config = mirrors[value][dir]
        dir = config[0]
        if len(config) > 1:
            entry = (pos, config[1])
            if entry not in splits:
                splits.append(entry)
    
    pos = (pos[0] + dir[0], pos[1] + dir[1])

print(len(visited))
