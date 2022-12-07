f = open('input.txt', 'r')
input = f.read().split('\n')

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

def solve():
    count = 0
    solution = ['start']
    visit_next = [find_next(solution)]

    while len(visit_next) > 0 and len(visit_next[-1]) > 0:
        value = visit_next[-1].pop(-1)
        solution.append(value)
        visit_next.append(find_next(solution))
        
        if value == 'end' and check_small_caves(solution):
            count += 1
            solution.pop()
            visit_next.pop()

        while len(visit_next) > 0 and len(visit_next[-1]) == 0:
            solution.pop()
            visit_next.pop()
    print(count)

def find_next(solution):
    visit_next = []
    last_item = solution[-1]

    for i in adjacency[last_item]:
        if i == 'start':
            continue

        if not i.islower() or check_small_caves(solution + [i]):
            visit_next.append(i)
    return visit_next

def check_small_caves(solution):
    visited_twice_count = 0
    for p in solution:
        if p.islower():
            count = solution.count(p)
            if count > 2:
                return False
            elif count == 2:
                visited_twice_count += 1
    return visited_twice_count <= 2

init_adjacency()
solve()
