print('hello')

def display_board(board):
    
    print(board[1]+ '|' + board[2] + '|'+board[3])
    print('- - -')
    print(board[4]+ '|' + board[5] + '|'+board[6])
    print('- - -')
    print(board[7]+ '|' + board[8] + '|'+board[9])

test_board = ['#','1','2','3','4','5','6','7','8','9']
display_board(test_board)


def player_input():

    marker = ''

    #asking player 1 to choce  or O

    while marker != 'X' and marker != 'O':
        marker = input('Player One would you like to be X or O? ').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

player1_marker, player2_marker = player_input()

def place_marker(board,marker,position):
    board[position] = marker


place_marker(test_board,'$',8)
display_board(test_board)

def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark ) or #top row
    (board[4] == mark and board[5] == mark and board[6] == mark) or #middle row
    (board[7] == mark and board[8] == mark and board[9] == mark) or #bottom row
    (board[1] == mark and board[4] == mark and board[7] == mark) or #left column
    (board[2] == mark and board[5] == mark and board[8] == mark) or #middle column
    (board[3] == mark and board[6] == mark and board[9] == mark) or #right column
    (board[1] == mark and board[5] == mark and board[9] == mark) or #diagonal
    (board[3] == mark and board[5] == mark and board[7] == mark)) #diagonal 

win_check(test_board,'X')


import random

def choose_first():

    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check():

    return board[position] == ' '


def full_board_check(board):

    for i in range(1-10):
        if space_check(board,i):
            return False
    #board is full
    return True 

