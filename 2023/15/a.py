with open ('input.txt') as f:
    input = f.read().replace('\n', '').split(',')

def get_hash(key):
    hash = 0
    for ch in key:
        hash = (hash + ord(ch)) * 17 % 256
    return hash

result = 0
for entry in input:
    result += get_hash(entry)

print(result)
