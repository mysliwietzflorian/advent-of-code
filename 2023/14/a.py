with open ('input.txt') as f:
    input = f.read().splitlines()

grid = [[] for _ in range(len(input))]
for y in range(len(input)):
    grid[y] = [i for i in input[y]]

sum = 0
for x in range(len(grid[0])):
    last_fixpoint = 0
    for y in range(len(grid)):
        value = grid[y][x]
        if value == 'O':
            sum += len(grid) - last_fixpoint
            last_fixpoint += 1
        elif value == '#':
            last_fixpoint = y + 1

print(sum)
