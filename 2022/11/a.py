with open('input.txt', 'r') as f:
    lines = f.read().split('\n\n')

class Monkey():
    def __init__(self):
        self.items = []
        self.operation = ''
        self.test = -1
        self.true_target = -1
        self.false_target = -1
        self.activity = 0
    
    def inspect(self, level):
        value = eval(self.operation)(level)
        return value // 3

monkeys = []
for m_input in lines:
    m_input = m_input.splitlines()
    monkey = Monkey()
    monkey.items = [int(i) for i in m_input[1][18:].split(',')]
    monkey.operation = 'lambda old: ' + m_input[2][19:]
    monkey.test = int(m_input[3][21:])
    monkey.true_target = int(m_input[4][29:])
    monkey.false_target = int(m_input[5][30:])
    monkeys.append(monkey)

for _ in range(20):
    for monkey in monkeys:
        monkey.activity += len(monkey.items)

        for item in monkey.items:
            value = monkey.inspect(item)
            if value % monkey.test == 0:
                monkeys[monkey.true_target].items.append(value)
            else:
                monkeys[monkey.false_target].items.append(value)
        
        monkey.items.clear()

activity = []
for monkey in monkeys:
    activity.append(monkey.activity)

activity.sort()
print(activity[-1] * activity[-2])
