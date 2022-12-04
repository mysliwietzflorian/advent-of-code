f = open('input.txt', 'r')
input = f.read().split('\n\n')

numbers = [int(i) for i in input[0].split(',')]

def remove_number(board, number):
    if number in board:
        i = board.index(number)
        board[i] = -1
    return board

def is_solved(board):
    for i in range(5):
        solved = is_line_solved(board, i) or is_column_solved(board, i)
        if solved:
            return True
    return False
    
def is_line_solved(board, line):
    for i in range(5):
        if board[5*line + i] != -1:
            return False
    return True

def is_column_solved(board, column):
    for i in range(5):
        if board[5*i + column] != -1:
            return False
    return True

boards = input[1:]
for index in range(len(boards)):
    boards[index] = [int(i) for i in boards[index].split()]

for number in numbers:
    for index in range(len(boards)):
        board = boards[index]
        boards[index] = remove_number(board, number)
        if is_solved(board):
            print('number drawn: ', number)
            print('board index:  ', index)
            print('board:        ', board)
            
            # ihh python
            break
    else:
        continue
    break

# calculate solution
sum = 0
for n in boards[index]:
    if n != -1:
        sum += n

print(sum * number)
