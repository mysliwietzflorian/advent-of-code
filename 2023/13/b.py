f = open('input.txt', 'r')
input = f.read().split('\n\n')

MAX_SMUDGES = 1

def transpose(grid):
    result = [[] for _ in range(len(grid[0]))]
    for i in range(len(grid[0])):
        result[i] = [row[i] for row in grid]    
    return result

def diff_compare(a, b):
    count = 0
    for index in range(len(a)):
        if a[index] != b[index]:
            count += 1
    return count

def find_row_reflection(grid):
    grid = transpose(grid)
    return find_col_reflection(grid)

def find_col_reflection(grid):
    for i in range(len(grid) - 1):
        j = i + 1
        offset = 0

        smudge_count = diff_compare(grid[i], grid[j])
        while smudge_count <= MAX_SMUDGES and i - offset > 0 and j + offset + 1 < len(grid):
            offset += 1
            smudge_count += diff_compare(grid[i - offset], grid[j + offset])

        if smudge_count == MAX_SMUDGES:
            return i + 1

    return 0

sum = 0
for g in input:
    grid = [i for i in g.split('\n') if i]

    rows = find_row_reflection(grid)
    cols = find_col_reflection(grid)
    sum += cols * 100 + rows

print(sum)
