import random
from os import system, name

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


def display_board(board):
    # clear_output()
    clear()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[1] + '|' + board[2] + '|' + board[3])


#Players' marker
def player_input():
    '''
    OUTPUT: (Player1, Player2)
    '''
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('What do you want to be "X" or "O"? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#place marker
def place_marker(board, marker, position):
    board[position] = marker

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
def choose_first():
    flip = random.randint(0, 1)
    return 'Player 1' if flip == 0 else 'Player 2'

# check position on board is empty or not
def space_check(board, position):
    return board[position] == ' '

# check full board is empty or not
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# check position provided by user exists, empty or not on board
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    
    return position

# check player want to play again
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')