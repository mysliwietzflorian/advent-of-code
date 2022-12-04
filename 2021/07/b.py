f = open('input.txt', 'r')
input = [int(i) for i in f.read().split(',')]

seq = [0]
for i in range(1, max(input) + 1):
    seq.append(seq[i-1] + i)

cost = [0 for _ in range(max(input))]
for pos in range(len(cost)):
    for index in range(len(input)):
        cost[pos] += seq[abs(input[index] - pos)]

print(min(cost))
