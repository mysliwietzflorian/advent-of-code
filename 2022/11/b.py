import numpy

with open('input.txt', 'r') as f:
    lines = f.read().split('\n\n')

array_length = 50

class Monkey():
    def __init__(self):
        self.items = numpy.zeros(array_length, dtype=int)
        self.items_count = 0
        self.operation = ''
        self.test = -1
        self.true_target = -1
        self.false_target = -1
        self.activity = 0
    
    def inspect(self, index):
        value = self.items[index]
        return int(eval(self.operation)(value)) % modulo

monkeys = []
for m_input in lines:
    m_input = m_input.splitlines()
    monkey = Monkey()

    item_input = m_input[1][18:].split(',')
    for i in range(len(item_input)):
        monkey.items[i] = int(item_input[i])
        monkey.items_count += 1
    monkey.operation = 'lambda old: ' + m_input[2][19:]
    monkey.test = int(m_input[3][21:])
    monkey.true_target = int(m_input[4][29:])
    monkey.false_target = int(m_input[5][30:])
    monkeys.append(monkey)

# chinese remainder theorem to keep item values small
modulo = 1
for m in monkeys:
    modulo *= m.test

for _ in range(10000):
    for monkey in monkeys:
        monkey.activity += monkey.items_count

        for index in range(monkey.items_count):
            value = monkey.inspect(index)
            if value % monkey.test == 0:
                target = monkeys[monkey.true_target]
            else:
                target = monkeys[monkey.false_target]
            target.items[target.items_count] = value
            target.items_count += 1

        monkey.items = numpy.zeros(array_length, dtype=int)
        monkey.items_count = 0

activity = []
for monkey in monkeys:
    activity.append(monkey.activity)
activity.sort()
print(activity[-1] * activity[-2])
