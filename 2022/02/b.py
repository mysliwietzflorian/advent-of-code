f = open('input.txt', 'r')
lines = f.read().split('\n')

# A for Rock, B for Paper, and C for Scissors
# X means to lose, Y means draw, and Z means to win.
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

mapping = {
    'A X': 0 + 3,
    'B X': 0 + 1,
    'C X': 0 + 2,
    'A Y': 3 + 1,
    'B Y': 3 + 2,
    'C Y': 3 + 3,
    'A Z': 6 + 2,
    'B Z': 6 + 3,
    'C Z': 6 + 1,
}

score = 0
for line in lines:
    score += mapping[line]

print(score)
