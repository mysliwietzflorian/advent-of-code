with open ('input.txt') as f:
    input = f.read().splitlines()

def get_dir(raw_dir):
    match raw_dir:
        case 'L':
            return (-1,0)
        case 'R':
            return (1,0)
        case 'U':
            return (0,-1)
        case 'D':
            return (0,1)

x = 0
y = 0
points = [(0,0)]
perimeter = 0

for line in input:
    raw_dir, step, color = line.split(' ')
    step = int(color[2:7], 16)
    raw_dir = 'RDLU'[int(color[7:8])]

    dir = get_dir(raw_dir)
    x += dir[0]*step
    y += dir[1]*step
    points.append((x,y))
    perimeter += step

# shoelace formula (https://stackoverflow.com/a/717367)
area = 0
for i in range(len(points) - 1):
    area += points[i][0]*(points[i+1][1] - points[i-1][1])

print((area + perimeter) // 2 + 1)
