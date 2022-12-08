f = open('input.txt', 'r')
lines = [int(i) for i in f.read().splitlines()]

for i_1 in range(len(lines)):
    a = lines[i_1]
    for i_2 in range(i_1 + 1, len(lines)):
        b = lines[i_2]
        for i_3 in range(i_2 + 1, len(lines)):
            c = lines[i_3]
            if a + b + c == 2020:
                print(a*b*c)
