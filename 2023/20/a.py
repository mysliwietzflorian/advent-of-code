import re
from collections import deque

with open ('input.txt') as f:
    lines = f.read().splitlines()

modules = {}
queue = deque()
count = [0, 0]

class Module():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.inputs = []
        self.outputs = []

        if self.type == '%': # flip flop
            self.state = False
        elif self.type == '&': # conjunction
            self.state = []
        else: # broadcast
            self.state = None
    
    def send(self, high):
        global count

        for o in self.outputs:
            count[high] += 1
            queue.append((self.name, o, high))

    def pulse(self, high, source):
        if self.type == '%':
            self.pulseFlipFlop(high)
        elif self.type == '&':
            self.pulseConjunction(high, source)
        else:
            self.send(high)

    def pulseFlipFlop(self, high):
        if high:
            return
        else:
            self.state = not self.state
            self.send(self.state)

    def pulseConjunction(self, high, source):
        i = self.inputs.index(source)
        self.state[i] = high
        self.send(not all(self.state))
    
    def addInput(self, input):
        self.inputs.append(input)
        if self.type == '&': # conjunction
            self.state.append(False)

def trigger_broadcast():
    high = False
    count[high] += 1
    modules['broadcaster'].send(high)

for line in lines:
    m = re.match(r'([%&]?)(\w+) -> (.*)', line)
    module = Module(m.group(2), m.group(1))
    modules[m.group(2)] = module

for line in lines:
    m = re.match(r'([%&]?)(\w+) -> (.*)', line)
    name = m.group(2)
    ioList = m.group(3).split(', ')
    modules[name].outputs = ioList
    for io in ioList:
        if io in modules:
            modules[io].addInput(name)

for _ in range(1000):
    queue = deque()
    trigger_broadcast()
    while queue:
        source, target, high = queue.popleft()
        if target in modules:
            modules[target].pulse(high, source)

print(count[0] * count[1])
