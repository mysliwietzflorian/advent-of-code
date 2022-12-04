f = open('input.txt', 'r')
spec = f.read().split('\n')

outputs = [0 for _ in range(len(spec))]
for index in range(len(spec)):
    line = spec[index].split('|')
    outputs[index] = line[1].split()

sum = 0
for index in range(len(outputs)):
    for entry in outputs[index]:
        length = len(entry)
        if length == 2 or length == 3 or length == 4 or length == 7:
            sum += 1
print(sum)
