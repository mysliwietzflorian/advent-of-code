f = open('input.txt', 'r')

lines = f.read().split('\n\n')
sums = []
for entries in lines:
    curr_sum = 0
    entries = [int(i) for i in entries.split('\n')]
    for i in entries:
        curr_sum += i

    sums.append(curr_sum)

sums.sort()
print(sums[-1] + sums[-2] + sums[-3])
