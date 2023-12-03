with open ('input.txt') as f:
    input = f.read().splitlines()

grid = [[] for _ in range(len(input))]
for y in range(len(input)):
    grid[y] = [i for i in input[y]]

current_number = ''
current_gear_positions = []
result_set = {}

def in_bound(grid, x, y):
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[y]):
        return False
    return True

def find_adjacent_gears(grid, x, y):
    global current_gear_positions

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
        if value == '*' and (new_x, new_y) not in current_gear_positions:
            current_gear_positions += [(new_x, new_y)]

for y in range(len(grid)):
    for x in range(len(grid[y])):
        value = grid[y][x]

        if value.isnumeric():
            current_number += value

            find_adjacent_gears(grid, x, y)
        
        last_of_line = x >= len(grid[y]) - 1
        if not value.isnumeric() or last_of_line:
            if len(current_gear_positions) > 0:
                for key in current_gear_positions:
                    result_set.setdefault(key,[]).append(int(current_number))
            current_number = ''
            current_gear_positions = []

sum = 0
for gears in result_set.values():
    if len(gears) == 2:
        sum += gears[0] * gears[1]

print(sum)
