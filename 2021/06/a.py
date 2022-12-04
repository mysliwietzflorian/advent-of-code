f = open('input.txt', 'r')
list = [int(i) for i in f.read().split(',')]

for gen in range(1, 81):
    for index in range(len(list)):
        value = list[index]
        if value == 0:
            list[index] = 6
            list.append(8)
        else:
            list[index] -= 1
    
    print(gen, len(list))
