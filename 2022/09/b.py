with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def get_dir_delta(dir):
    if dir == 'L':
        return [-1, 0]
    elif dir == 'R':
        return [1, 0]
    elif dir == 'U':
        return [0, 1]
    elif dir == 'D':
        return [0, -1]

def is_touching(dx, dy):
    return abs(dx) <= 1 and abs(dy) <= 1

def get_delta_to_prev(index):
    return [rope[i-1][0] - rope[i][0], rope[i-1][1] - rope[i][1]]

def get_catchup_offset(dx, dy):
    return [
        0 if dx == 0 else dx - dx // abs(dx),
        0 if dy == 0 else dy - dy // abs(dy)
    ]

def get_diagonal_offset(dx, dy):
    if abs(dx) + abs(dy) != 3:
        return [0, 0]

    if abs(dx) == 1:
        return [dx, 0]
    if abs(dy) == 1:
        return [0, dy]
    return [0, 0]

length = 10
rope = [[0, 0] for _ in range(length)]
positions = [rope[-1]]

for line in lines:
    if line.startswith('#'):
        continue

    dir = line.split()[0]
    steps = int(line.split()[1])

    for _ in range(steps):
        for i in range(length):

            if i == 0:
                dir_delta = get_dir_delta(dir)
                rope[0] = [rope[0][0] + dir_delta[0], rope[0][1] + dir_delta[1]]
                continue

            curr_delta = get_delta_to_prev(i)
            if not is_touching(curr_delta[0], curr_delta[1]):
                catchup = get_catchup_offset(curr_delta[0], curr_delta[1])
                diagonal = get_diagonal_offset(curr_delta[0], curr_delta[1])
                rope[i] = [rope[i][0] + catchup[0] + diagonal[0], rope[i][1] + catchup[1] + diagonal[1]]
        
        if rope[-1] not in positions:
            positions.append(rope[-1])

print(len(positions))
