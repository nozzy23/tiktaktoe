print('hello')

def display_board(board):
    
    print(board[1]+ '|' + board[2] + '|'+board[3])
    print('- - -')
    print(board[4]+ '|' + board[5] + '|'+board[6])
    print('- - -')
    print(board[7]+ '|' + board[8] + '|'+board[9])



def player_input():

    marker = ''

    #asking player 1 to choce  or O

    while marker != 'X' and marker != 'O':
        marker = input('Player One would you like to be X or O? ').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


def place_marker(board,marker,position):
    board[position] = marker


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark ) or #top row
    (board[4] == mark and board[5] == mark and board[6] == mark) or #middle row
    (board[7] == mark and board[8] == mark and board[9] == mark) or #bottom row
    (board[1] == mark and board[4] == mark and board[7] == mark) or #left column
    (board[2] == mark and board[5] == mark and board[8] == mark) or #middle column
    (board[3] == mark and board[6] == mark and board[9] == mark) or #right column
    (board[1] == mark and board[5] == mark and board[9] == mark) or #diagonal
    (board[3] == mark and board[5] == mark and board[7] == mark)) #diagonal 


import random

def choose_first():

    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board,position):

    return board[position] == ' '


def full_board_check(board):

    for i in range(1-10):
        if space_check(board,i):
            return False
    #board is full
    return True 

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Please choose a spot: 1-9  '))

    return position

def replay():

    choice = input('Would you like to play again? Yes or no? ')

    return choice == 'Yes'

#while loop for running game 

print ('Hello Lets play TikTakToe!')

while True:

    #play the game
    
    #set the game board, who is first and marker

    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print (turn + ' Will go First')

    play_game = input('Ready to play? y or n ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False


    #gameplay
    while game_on:

        if turn == 'Player 1':
            #player 1
            #Show board
            display_board(the_board)
            #position
            position = player_choice(the_board)
            #place marker at position 
            place_marker(the_board,player1_marker,position)
            #check if the won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 Won!!')
                game_on = False
            else:
                turn = 'Player 2'
        
#player 2

        else:
            display_board(the_board)
            #position
            position = player_choice(the_board)
            #place marker at position 
            place_marker(the_board,player2_marker,position)
            #check if the won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 Won!!')
                game_on = False
            else:
                turn = 'Player 1'




    if not replay():
        break
#break loop on replay()