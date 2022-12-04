f = open('input.txt', 'r')
lines = f.read().split('\n')

def get_prio(ch):
    n = ord(ch) 
    if ord(ch) >= ord('a'):
        return ord(ch) - ord('a') + 1
    else:
        return ord(ch) - ord('A') + 27

prio = 0

for line in lines:
    first = line[:len(line) // 2]
    second = line[len(line) // 2:]

    for ch in first:
        if ch in second:
            prio += get_prio(ch)
            break

print(prio)
