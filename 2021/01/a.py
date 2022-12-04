f = open('input.txt', 'r')

lines = [int(i) for i in f.read().split('\n')]

count = 0
prev = 2**16
for line in lines:
    if line > prev:
        count += 1
    
    prev = line

print(count)
