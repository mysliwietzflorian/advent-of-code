f = open('input.txt', 'r')
input = f.read().splitlines()

m = len(input[0])
n = len(input)

grid = [[] for _ in range(n)]
for y in range(n):
    grid[y] = [int(i) for i in input[y]]

def get_scenic_score(x, y):
    score = 1
    score *= get_single_score(x, y, reversed(range(0, x)), 'h')
    score *= get_single_score(x, y, range(x + 1, m), 'h')
    score *= get_single_score(x, y, reversed(range(0, y)), 'v')
    score *= get_single_score(x, y, range(y+ 1 , n), 'v')
    return score

def get_single_score(x, y, list, direction):
    count = 0
    for i in list:
        comp = grid[y][i] if direction == 'h' else grid[i][x]
        if comp >= grid[y][x]:
            return count + 1
        count += 1
    return count

highest_score = 0
for y in range(n):
    for x in range(m):
        score = get_scenic_score(x, y)
        if score > highest_score:
            highest_score = score

print(highest_score)
