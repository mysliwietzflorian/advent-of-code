f = open('input.txt', 'r')
lines = f.read().split('\n')

count = 0
for line in lines:
    pairs = line.split(',')
    range1 = [int(i) for i in pairs[0].split('-')]
    range2 = [int(i) for i in pairs[1].split('-')]

    if range1[1] >= range2[0] and range1[1] <= range2[1] or \
        range2[1] >= range1[0] and range2[1] <= range1[1]:
        count += 1
    
print(count)
