with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

score = 0
cycle = 0
x = 1

def inc_cycle(n):
    global score, cycle
    for i in range(n):    
        cycle += 1
        if cycle % 40 == 20:
            score += cycle * x

for line in lines:
    if line.split()[0] == 'noop':
        inc_cycle(1)
    else:
        inc_cycle(2)
        x += int(line.split()[1])

print(score)