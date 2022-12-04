f = open('input.txt', 'r')

lines = [int(i) for i in f.read().split('\n')]

count = 0
measurement = lines[0] + lines[1] + lines[2]
for index in range(3, len(lines)):
    if measurement < measurement - lines[index - 3] + lines[index]:
        count += 1
    
    measurement += lines[index] - lines[index - 3]

print(count)
