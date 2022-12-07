f = open('input.txt', 'r')
lines = f.read().split('\n\n')

dots = []
folds = []
grid = []

def init_dots():
    dots_input = lines[0].split('\n')
    for i in dots_input:
        parts = i.split(',')
        dots.append([int(parts[0]), int(parts[1])])

def init_folds():
    fold_input = lines[1].split('\n')
    for line in fold_input:
        parts = line.split()[2]
        folds.append(parts.split('='))

def init_grid():
    global grid
    max_x, max_y = find_dims()
    grid = create_grid(max_x, max_y, '.')
    for dot in dots:
        grid[dot[1]][dot[0]] = '#'

def create_grid(width, height, init_char):
    grid = [[] for _ in range(height)]
    for y in range(height):
        grid[y] = [init_char for _ in range(width)]
    return grid

def find_dims():
    max_x = 0
    max_y = 0
    for dot in dots:
        if dot[0] > max_x:
            max_x = dot[0]
        if dot[1] > max_y:
            max_y = dot[1]
    return [max_x + 1, max_y + 1]

def print_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], sep='', end='')
        print()
    print()

init_dots()
init_folds()
init_grid()

for fold in folds:
    new_height = int(fold[1]) if fold[0] == 'y' else len(grid)
    new_width = int(fold[1]) if fold[0] == 'x' else len(grid[0])
    shadow = create_grid(new_width, new_height, '.')

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            value = grid[y][x]
            if value == '#':
                cx = x if x < new_width else new_width - (x - new_width)
                cy = y if y < new_height else new_height - (y - new_height)
                shadow[cy][cx] = '#'
    grid = shadow
    break

count = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == '#':
            count += 1
print(count)