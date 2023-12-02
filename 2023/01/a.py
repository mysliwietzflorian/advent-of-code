f = open('input.txt', 'r')
lines = f.read().split('\n')

sum = 0
for line in lines:

    filtered = list(filter(lambda x: x.isnumeric(), line))
    number = int(filtered[0] + filtered[-1])
    sum += number

print(sum)
