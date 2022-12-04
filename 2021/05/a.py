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

    if pipe[1] == pipe[3]: # horizontal
        minimum, maximum = [min(pipe[0], pipe[2]), max(pipe[0], pipe[2])]
        for i in range(minimum, maximum + 1):
            grid[pipe[1]*n + i] += 1    

count = 0
for y in range(n):
    for x in range(n):
        if grid[y*n + x] > 1:
            count += 1
    #     print(grid[y*n + x], sep='', end='')
    # print()
print(count)
