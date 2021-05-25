def display_board(board):
    print('\n' * 50)
    print('Positional chart:\n1|2|3\n4|5|6\n7|8|9\n')
    print('Board:')
    pstring = ''
    for i in range(1,len(board)):
#         print(i)
        if i%3 == 0:
            pstring += board[i] + '\n'
        else:
            pstring += board[i] + '|'
    print(pstring)
    pass

def player_input():
    while True:
        x = input('Enter marker choice of player 1 (X or O): ')
        if x in ['x','o','X','O']:
            return x.upper()
        else:
            print('Invalid input. Please try again.')
            continue
    pass

def place_marker(board, marker, position):
    board[position] = marker
    pass

def win_check(board, mark):
    #     print(board[1:10:5])
    #     print(board[1:10:3])
    #     print(list(mark * 3))
    if board[1:4:1] == list(mark * 3):
        return True
    if board[4:7:1] == list(mark * 3):
        return True
    if board[7:10:1] == list(mark * 3):
        return True

    if board[1:10:3] == list(mark * 3):
        return True
    if board[2:10:3] == list(mark * 3):
        return True
    if board[3:10:3] == list(mark * 3):
        return True

    if board[1:10:4] == list(mark * 3):
        return True
    if board[3:8:2] == list(mark * 3):
        return True
    return False

import random

def choose_first():
    if random.randint(0,1):
        print('Player 1 starts first')
        return 1
    else:
        print('Player 2 starts first')
        return 2
    pass

def space_check(board, position):
    return board[position] == ' '
    pass

def full_board_check(board):
    try:
        board.index(' ')
        return False
    except:
        return True
    pass

def player_choice(board):
    while True:
        x = input('Enter the position of your choice (1 to 9) or "e" to exit game: ')
        try:
            x = int(x)
            if x not in range(1,10):
                continue
        except:
            exit(1)
            continue
        if space_check(board,x):
            return x
        else:
            continue
    pass

def replay():
    while True:
        x = input('Do you want to play again (y/n): ')
        if x in ['y','Y']:
            return True
        elif x in ['n','N']:
            return False
        else:
            print('Invalid input. Please try again.')
            continue
    pass


print('Welcome to Tic Tac Toe!')
while True:
    temp = 0
    # Set the game up here
    board = '#' + ' ' * 9
    board = list(board)
    print(board)
    # pass

    p1marker = player_input()
    if p1marker == 'X':
        p2marker = 'O'
    else:
        p2marker = 'X'

    turnvar = choose_first()
    game_on = True
    while game_on:
        # Player 1 Turn
        if turnvar == 1:
            display_board(board)
            if full_board_check(board):
                print('Game over! Game ended in a tie.')
                break
            print('Player 1:')
            mark = player_choice(board)
            place_marker(board, p1marker, mark)
            if win_check(board, p1marker):
                display_board(board)
                print('Game over! Player 1 won.')
                break
            turnvar = 2

        # Player2's turn.
        if turnvar == 2:
            display_board(board)
            if full_board_check(board):
                print('Game over! Game ended in a tie.')
                break
            print('Player 2:')
            mark = player_choice(board)
            place_marker(board, p2marker, mark)
            if win_check(board, p2marker):
                display_board(board)
                print('Game over! Player 2 won.')
                break
            turnvar = 1

    if not replay():
        break
