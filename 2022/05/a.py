import re

def main():
    f = open('input.txt', 'r')
    lines = f.read().split('\n\n')
    crates_input = lines[0].split('\n')
    moves_input = lines[1].split('\n')

    stacks = init_stacks(crates_input)
    calc_moves(moves_input, stacks)

    solution = ''
    for s in stacks:
        solution += s.pop()
    print(solution)

def init_stacks(crates_input):
    
    nr_of_stacks = len(re.findall(r'\d+', crates_input[-1]))
    stacks = [[] for _ in range(nr_of_stacks)]

    for crateLine in reversed(crates_input[:-1]):
        for index in range(len(stacks)):
            curr = crateLine[4*index + 1]
            if curr != ' ':
                stacks[index].append(curr)
    return stacks

def calc_moves(moves_input, stacks):
    for move_line in moves_input:
        move, from_stack, to_stack = [int(i) for i in re.findall(r'\d+', move_line)]

        for i in range(move):
            value = stacks[from_stack - 1].pop()
            stacks[to_stack - 1].append(value)

if __name__ == '__main__':
    main()
