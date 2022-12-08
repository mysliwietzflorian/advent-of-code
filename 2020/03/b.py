f = open('input.txt', 'r')
lines = f.read().splitlines()

def calc_hits(dx, dy):
    x = 0
    hits = 0
    for index in range(0, len(lines), dy):
        line = lines[index]

        if line[x] == '#':
            hits += 1
        x = (x + dx) % len(line)
    return hits

prod = 1
for dx, dy in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
    prod *= calc_hits(dx, dy)
print(prod)

