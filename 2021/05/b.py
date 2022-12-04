f = open('input.txt', 'r')
input = f.read().split('\n')

pipes = []
for index in range(len(input)):
    pipes.append([int(i) for i in input[index].replace('-> ', '').replace(',', ' ').split()])

n = 1000
grid = [0 for _ in range(n*n)]
for pipe in pipes:
    if pipe[0] == pipe[2]: # vertical
        minimum, maximum = [min(pipe[1], pipe[3]), max(pipe[1], pipe[3])]
        for i in range(minimum, maximum + 1):
            grid[i*n + pipe[0]] += 1
    elif pipe[1] == pipe[3]: # horizontal
        minimum, maximum = [min(pipe[0], pipe[2]), max(pipe[0], pipe[2])]
        for i in range(minimum, maximum + 1):
            grid[pipe[1]*n + i] += 1
    else:
        min_X, max_X = [min(pipe[0], pipe[2]), max(pipe[0], pipe[2])]
        min_Y, max_Y = [min(pipe[1], pipe[3]), max(pipe[1], pipe[3])]

        rangeStep = 1
        if min_X != pipe[0] and min_Y == pipe[1] or min_X == pipe[0] and min_Y != pipe[1]:
            min_Y, max_Y = max_Y, min_Y
            rangeStep = -1

        for i in range(0, max_X - min_X + 1):
            x = i + min_X
            y = rangeStep * i + min_Y
            grid[y*n + x] += 1

count = 0
for y in range(n):
    for x in range(n):
        if grid[y*n + x] > 1:
            count += 1
#         print(grid[y*n + x], sep='', end='')
#     print()
# print()
print(count)
