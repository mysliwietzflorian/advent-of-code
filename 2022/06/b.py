f = open('input.txt', 'r')
line = f.read()
n = 14

for index in range(len(line)):
    window = [*set(line[index:index+n])]
    if len(window) >= n:
        print(index + n)
        break
