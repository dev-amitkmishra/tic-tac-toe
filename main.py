#create board with index
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])

#print the output
display_board(['#','X','O','X','O','X','O','X','O','X'])


#Players' marker
def player_input():
    '''
    OUTPUT: (Player1, Player2)
    '''
    
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O:  ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


#tuple unpacking to get the marker of both player
player1_marker, player2_marker = player_input()

#place marker
def place_marker(board, marker, position):
    board[position] = marker

# check whether new data is updating or not in board
test_board = ['#','X','O','X','O','X','O','X','O','X']
place_marker(test_board, '%', 5)
display_board(test_board)

#win check of any player
def win_check(board, mark):
    #won the game or not
    return ((board[1] == board[2] == board[3] == mark) or 
            (board[4] == board[5] == board[6] == mark) or 
            (board[7] == board[8] == board[9] == mark) or 
            (board[1] == board[4] == board[7] == mark) or 
            (board[2] == board[5] == board[8] == mark) or 
            (board[3] == board[6] == board[9] == mark) or 
            (board[1] == board[5] == board[9] == mark) or 
            (board[3] == board[5] == board[7] == mark))

# check who will start first
import random

def choose_first():
    flip = random.randint(0, 1)
    return 'Player 1' if flip == 0 else 'Player 2'

# check position on board is empty or not
def space_check(board, position):
    return board[position] == ''

# check full board is empty or not
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True