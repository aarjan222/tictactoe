# Tic Tac Toe Game in Python

board = [' ' for x in range(10)]


def insertBoard(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))


def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')

        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry this place is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def checkWinner():
    a = isWinner(board, 'X')
    b = isWinner(board, 'O')
    if a:
        return 'X'
    elif b:
        return 'O'
    elif isBoardFull(board):
        return 'tie'


def minimax(board, depth, isMaximizing):

    winner = checkWinner()
    if winner is not None:
        return 1 if winner == 'O' else -1 if winner == 'X' else 0

    if isMaximizing:
        bestScore = float('-inf')
        for i in range(len(board)):
            if spaceIsFree(i):
                insertLetter('O', i)
                score = minimax(board, depth+1, False)
                insertLetter(' ', i)
                bestScore = max(score, bestScore)

        return bestScore
    else:
        bestScore = float('inf')
        for i in range(len(board)):
            if spaceIsFree(i):
                insertLetter('X', i)
                score = minimax(board, depth+1, True)
                insertLetter(' ', i)
                bestScore = min(score, bestScore)

        return bestScore


def compMove():
    possibleMoves = [x for x, letter in enumerate(
        board) if letter == ' ' and x != 0]

    bestMove = -1
    bestScore = float('-inf')

    for i in possibleMoves:
        insertLetter('O', i)
        score = minimax(board, 0, False)
        insertLetter(' ', i)
        if score is not None and score > bestScore:
            bestScore = score
            bestMove = i

    return bestMove


def insertLetter(letter, pos):
    board[pos] = letter


def selectRandom(li):
    import random
    return li[random.randrange(0, len(li))]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


# computer = 0
# user = X
def main():
    print('Welcome to TIC TAC TOE!')
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, computer(AI)\'s won this time!')
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == -1:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        else:
            print('Sorry, X\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Game Tied!')


main()
