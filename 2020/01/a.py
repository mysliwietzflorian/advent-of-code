f = open('input.txt', 'r')
lines = [int(i) for i in f.read().splitlines()]

for index in range(len(lines)):
    a = lines[index]
    for b in lines[index+1:]:
        if a + b == 2020:
            print(a*b)
