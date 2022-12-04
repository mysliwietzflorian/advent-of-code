f = open('input.txt', 'r')
lines = f.read().split('\n')

def get_prio(ch):
    n = ord(ch)
    if ord(ch) >= ord('a'):
        return ord(ch) - ord('a') + 1
    else:
        return ord(ch) - ord('A') + 27

prio = 0
mod = 3

for group_id in range(len(lines) // mod):
    uniques = [*set(lines[3*group_id])]

    for line in lines[mod*group_id + 1:mod*group_id + mod]:
        for i in reversed(range(len(uniques))):
            ch = uniques[i]
            if ch not in line:
                uniques.remove(ch)
    
    prio += get_prio(uniques[0])

print(prio)
