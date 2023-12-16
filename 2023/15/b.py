import re

with open ('input.txt') as f:
    input = f.read().replace('\n', '').split(',')

def get_hash(key):
    hash = 0
    for ch in key:
        hash = (hash + ord(ch)) * 17 % 256
    return hash

boxes = [{} for _ in range(256)]
for entry in input:
    m = re.match(r'([\w]+)([\-=])([\d]?)', entry)
    label = m.group(1)
    operator = m.group(2)
    lense = int(m.group(3)) if m.group(3) else None

    hash = get_hash(label)

    if operator == '=':
        boxes[hash][label] = lense
    else:
        if label in boxes[hash]:
            boxes[hash].pop(label)

result = 0
for i in range(256):
    slot_number = 1
    for label, lense in boxes[i].items():
        result += (1 + i) * slot_number * lense
        slot_number += 1

print(result)
