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
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

scores_array = []
for line in input:
    openings = []
    for ch in line:
        if re.match('\(|\[|\{|<', ch):
            openings.append(ch)
        elif re.match('\)|\]|\}|>', ch):
            open = openings.pop()
            if ch != open_close_mapping[open]:
                break
    else:
        score = 0
        while len(openings) > 0:
            open = openings.pop()
            close = open_close_mapping[open]
            score = 5*score + score_mapping[close]

        scores_array.append(score)
        continue

scores_array.sort()
print(scores_array[len(scores_array) // 2])
