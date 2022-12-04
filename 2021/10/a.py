import re

f = open('input.txt', 'r')
input = f.read().split('\n')

open_close_mapping = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
score_mapping = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

score = 0
for line in input:
    openings = []
    for ch in line:
        if re.match('\(|\[|\{|<', ch):
            openings.append(ch)
        elif re.match('\)|\]|\}|>', ch):
            open = openings.pop()
            if ch != open_close_mapping[open]:
                score += score_mapping[ch]

print(score)
