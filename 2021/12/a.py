import sys
sys.setrecursionlimit(10000)

f = open('input.txt', 'r')
input = f.read().split('\n')

count = 0
adjacency = {}

def init_adjacency():
    for line in input:
        a, b = line.split('-')

        if a not in adjacency:
            adjacency[a] = [b]
        else:
            adjacency[a].append(b)
        if b not in adjacency:
            adjacency[b] = [a]
        else:
            adjacency[b].append(a)

def solve(start, find_next, is_partial, is_goal):
    solution = [start]
    visit_next = [find_next(solution)]

    def extend_solution(visit_next):
        global count
        while len(visit_next) > 0 and len(visit_next[-1]) > 0:
            value = visit_next[-1].pop(0)
            solution.append(value)

            if is_partial(solution):
                visit_next.append(find_next(solution))
                if is_goal(value) or extend_solution(visit_next):
                    count += 1
                    solution.pop()
                    visit_next.pop()

            while len(visit_next) > 0 and len(visit_next[-1]) == 0:
                solution.pop()
                visit_next.pop()

    extend_solution(visit_next)

def find_next(solution):
    visit_next = []
    last_item = solution[-1]

    for i in adjacency[last_item]:
        if not i[0].islower() or i not in solution:
            visit_next.append(i)
    return visit_next

def is_partial(solution):
    last = solution[-1]
    if last in solution[:-1] and last[0].islower():
        return False
    return True

def is_goal(value):
    return value == 'end'

init_adjacency()
solve('start', find_next, is_partial, is_goal)
print(count)
