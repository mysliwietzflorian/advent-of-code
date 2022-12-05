import re

f = open('input.txt', 'r')
lines = f.read().split('\n\n')
crates_input = lines[0].split('\n')
moves_input = lines[1].split('\n')

nr_of_stacks = len(re.findall(r'\d+', crates_input[-1]))
stacks = [[] for _ in range(nr_of_stacks)]

def init_stacks():
    for crateLine in reversed(crates_input[:-1]):
        for index in range(len(stacks)):
            curr = crateLine[4*index + 1]
            if curr != ' ':
                stacks[index].append(curr)

def calc_moves():
    for move_line in moves_input:
        move, from_stack, to_stack = [int(i) for i in re.findall(r'\d+', move_line)]

        for i in range(move):
            value = stacks[from_stack - 1].pop()
            stacks[to_stack - 1].append(value)

def print_solution():
    solution = ''
    for s in stacks:
        solution += s.pop()
    print(solution)

init_stacks()
calc_moves()
print_solution()
