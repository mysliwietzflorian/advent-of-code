f = open('input.txt', 'r')
lines = f.read().split('\n')

class Node:
    def __init__(self, type, name, size):
        self.type = type
        self.name = name
        self.size = size
        self.children = []

    def __str__(self):
        return f'{self.type} {self.name.ljust(10)}' + str(self.get_full_size())

    def get_full_size(self):
        if self.type == 'blob':
            return int(self.size)

        sum = 0
        for ch in self.children:
            sum += ch.get_full_size()
        return sum

def full_name(last):
    result = ref.name

    if last == '/':
        return last

    if ref.name[-1] != '/':
        result += '/'
    return result + last

def change_directory(name):
    global ref
    if name == '..':
        parts = ref.name.split('/')
        parts.pop()
        if len(parts) <= 1:
            path = '/'
        else:
            path = '/'.join(parts)
    else:
        path = full_name(name)

    for o in objects:
        if o.type == 'tree' and o.name == path:
            ref = o
            return

def process_list(index):
    data = lines[index].split()
    while data and not data[0] == '$':
        if data[0] == 'dir':
            objects.append(Node('tree', full_name(data[1]), 0))
        else:
            objects.append(Node('blob', full_name(data[1]), data[0]))

        ref.children.append(objects[-1])

        index += 1
        if index >= len(lines):
            return
        data = lines[index].split()

def print_fs():
    for o in objects:
        if o.type == 'tree':
            print(o)
            for ch in o.children:
                print('  -', ch)

ref = Node('tree', '/', 0)
objects = [ref]

for index in range(len(lines)):
    line = lines[index]

    if line.startswith('$ cd'):
        change_directory(line.split()[2])
    elif line.startswith('$ ls'):
        process_list(index + 1)

# print_fs()

root_size = objects[0].get_full_size()
space_missing = root_size + 30000000 - 70000000
min_size = root_size

for o in objects:
    if o.type == 'tree':
        s = o.get_full_size()
        if s > space_missing and s < min_size:
            min_size = s

print(min_size)
