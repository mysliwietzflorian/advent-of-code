f = open('input.txt', 'r')
lines = f.read().split('\n')

bits = [0 for _ in range(len(lines[0]))]

for line in lines:
    for i in range(len(line)):
        ch = line[i]
        if ch == '0':
            bits[i] -= 1
        elif ch == '1':
            bits[i] += 1

gamma = ''
epsilon = ''
for bit in bits:
    if bit < 0:
        gamma += '0'
        epsilon += '1'
    elif bit > 0:
        gamma += '1'
        epsilon += '0'
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)