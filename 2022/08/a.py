f = open('input.txt', 'r')
input = f.read().splitlines()

m = len(input[0])
n = len(input)

grid = [[] for _ in range(n)]
for y in range(n):
    grid[y] = [int(i) for i in input[y]]

def is_visible(x, y):
    return (
        is_single_visible(x, y, range(0, x), 'h') or
        is_single_visible(x, y, range(x + 1, m), 'h') or
        is_single_visible(x, y, range(0, y), 'v') or
        is_single_visible(x, y, range(y+ 1 , n), 'v')
    )

def is_single_visible(x, y, list, direction):
    for i in list:
        comp = grid[y][i] if direction == 'h' else grid[i][x]
        if comp >= grid[y][x]:
            return False
    return True

visible = 0
for y in range(n):
    for x in range(m):
        if is_visible(x, y):
            visible += 1

print(visible)
