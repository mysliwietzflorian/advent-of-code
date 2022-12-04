f = open('input.txt', 'r')
input = [int(i) for i in f.read().split(',')]

cost = [0 for _ in range(max(input))]
for pos in range(len(cost)):
    for index in range(len(input)):
        cost[pos] += abs(input[index] - pos)

print(min(cost))
