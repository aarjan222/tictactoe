# Tic Tac Toe Game in Python

board = [' ' for x in range(10)]
total_visited_states = 0

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
        except ValueError:
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


def minimax(board, depth, alpha, beta, isMaximizing):
    global total_visited_states
    total_visited_states += 1
    winner = checkWinner()
    if winner is not None:
        return 1 if winner == 'O' else -1 if winner == 'X' else 0

    if isMaximizing:  # computer(O)
        value = float('-inf')
        for i in range(len(board)):
            if spaceIsFree(i):
                insertLetter('O', i)
                value = max(value, minimax(board, depth+1, alpha, beta, False))
                insertLetter(' ', i)
                
                alpha = max(alpha, value)
                if value >= beta:
                    break

        return value
    else:  # player(X)
        value = float('inf')
        for i in range(len(board)):
            if spaceIsFree(i):
                insertLetter('X', i)
                value = min(value, minimax(board, depth+1, alpha, beta, True))
                insertLetter(' ', i)
                
                beta = min(beta, value)
                if value <= alpha:
                    break
                
        return value


def compMove():
    # get valid remaining moves
    possibleMoves = [x for x, letter in enumerate(
        board) if letter == ' ' and x != 0]

    bestMove = -1
    bestScore = float('-inf')
    a = float('-inf')
    b = float('inf')

    for i in possibleMoves:
        # fake computer placement in board for knowing the future states
        insertLetter('O', i)
        # call to player move by saying False(minimizing player)
        score = minimax(board, 0, a, b, False)
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
    global total_visited_states
    print('Welcome to TIC TAC TOE!')
    printBoard(board)

    while not (isBoardFull(board)):
        # check if computer has won or not
        if not (isWinner(board, 'O')):
            # get valid move from player
            playerMove()
            printBoard(board)
        else:
            print('Sorry, computer(AI)\'s O won this time!')
            break

        # check if player has won or not
        if not (isWinner(board, 'X')):
            # get winning strong move from different algorithms!
            move = compMove()
            if move == -1:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        else:
            print('Sorry, You X\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Game Tied!')
    print(total_visited_states)


main()
