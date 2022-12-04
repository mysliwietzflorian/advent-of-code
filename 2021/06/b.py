f = open('input.txt', 'r')
list = [int(i) for i in f.read().split(',')]

hist = [0 for _ in range(10)]
for entry in list:
    hist[entry] += 1

for gen in range(1, 257):
    newHist = [0 for _ in range(10)]
    
    for index in range(0, 10):
        if index == 0:
            hist[7] += hist[0]
            hist[9] += hist[0]
        else:
            newHist[index - 1] = hist[index]

    hist = newHist
    sum = 0
    for i in range(len(hist)):
        sum += hist[i]
    print(gen, sum)
