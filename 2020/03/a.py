f = open('input.txt', 'r')
lines = f.read().splitlines()

x = 0
hit_trees = 0
for line in lines:
    if line[x] == '#':
        hit_trees += 1
    x = (x + 3) % len(line)

print(hit_trees)
