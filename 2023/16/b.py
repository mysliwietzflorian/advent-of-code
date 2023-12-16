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

def calc_energy(grid, pos, dir):
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
    
    return len(visited)

grid = [[] for _ in range(len(input))]
for y in range(len(input)):
    grid[y] = [i for i in input[y]]

results = []
length = len(grid) - 1

for i in range(length):
    results.append(calc_energy(grid, (i,0), (0,1)))
    results.append(calc_energy(grid, (i,length - 1), (0,-1)))
    results.append(calc_energy(grid, (0,i), (1,0)))
    results.append(calc_energy(grid, (length - 1,i), (-1,0)))

print(max(results))
