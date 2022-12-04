f = open('input.txt', 'r')

lines = f.read().split('\n\n')
max_sum = 0
for entries in lines:
    curr_sum = 0
    entries = [int(i) for i in entries.split('\n')]
    for i in entries:
        curr_sum += i

    if curr_sum > max_sum:
        max_sum = curr_sum

print(max_sum)
