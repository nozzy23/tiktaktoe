print('hello')

def display_board(board):
    
    print(board[1]+ '|' + board[2] + '|'+board[3])
    print('- - -')
    print(board[4]+ '|' + board[5] + '|'+board[6])
    print('- - -')
    print(board[7]+ '|' + board[8] + '|'+board[9])

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)