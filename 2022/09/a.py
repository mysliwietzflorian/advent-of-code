with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def is_touching(dx, dy):
    return abs(dx) <= 1 and abs(dy) <= 1

def update_delta(dir, dx, dy):
    if dir == 'L':
        return [dx + 1, dy]
    elif dir == 'R':
        return [dx - 1, dy]
    elif dir == 'U':
        return [dx, dy - 1]
    elif dir == 'D':
        return [dx, dy + 1]

def get_diagonally_offset(dx, dy):
    diag_x = 0 if dx == 0 or dy == 0 or abs(dx) == 2 else -dx
    diag_y = 0 if dx == 0 or dy == 0 or abs(dy) == 2 else -dy
    return [diag_x, diag_y]

# position of tail on the grid
pos = [0, 0]
# delta to head
delta = [0, 0]
positions = [pos]

for line in lines:
    dir = line.split()[0]
    steps = int(line.split()[1])

    for _ in range(steps):
        delta = update_delta(dir, delta[0], delta[1])

        if not is_touching(delta[0], delta[1]):
            diag = get_diagonally_offset(delta[0], delta[1])
            delta = [int(delta[0] / 2), int(delta[1] / 2)]
            pos = [pos[0] - delta[0] + diag[0], pos[1] - delta[1] + diag[1]]

        if pos not in positions:
            positions.append(pos)

print(len(positions))
