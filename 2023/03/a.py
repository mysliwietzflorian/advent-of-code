with open ('input.txt') as f:
    input = f.read().splitlines()

def in_bound(grid, x, y):
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]):
        return False
    return True

def find_adjacent_symbol(grid, x, y):
    neighbors = [
        [-1,-1], [0,-1], [1,-1],
        [-1, 0],         [1, 0],
        [-1, 1], [0, 1], [1, 1],
    ]

    for n in neighbors:
        new_x = x + n[0]
        new_y = y + n[1]

        if not in_bound(grid, new_x, new_y):
            continue
        
        value = grid[new_y][new_x]
        if not value.isnumeric() and value != '.':
            return True
    return False

grid = [[] for _ in range(len(input))]
for y in range(len(input)):
    grid[y] = [i for i in input[y]]

current_number = ''
has_adjacent_symbol = False
sum = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        value = grid[y][x]
        if value.isnumeric():
            current_number += value

            if find_adjacent_symbol(grid, x, y):
                has_adjacent_symbol = True
        else:
            if has_adjacent_symbol:
                sum += int(current_number)
            current_number = ''
            has_adjacent_symbol = False

    if has_adjacent_symbol:
        sum += int(current_number)
    current_number = ''
    has_adjacent_symbol = False

print(sum)
