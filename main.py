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