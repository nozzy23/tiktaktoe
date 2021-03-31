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