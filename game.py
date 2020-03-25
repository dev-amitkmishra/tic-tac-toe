import helper_functions

print('Welcome to Tic-Tac-Toe')

while True:
    # Reset the board
    board = [' '] * 10
    player1_marker, player2_marker = helper_functions.player_input()
    turn = helper_functions.choose_first()
    print(turn, ' will start first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    isPersonalizedNameRequired = input('Do you want to enter name before contiuing the game? Yes or No: ')
    player1 = input('Please enter player1 name') if isPersonalizedNameRequired.lower()[0] == 'y' else 'Player1'
    player2 = input('Please enter player2 name') if isPersonalizedNameRequired.lower()[0] == 'y' else 'Player2'

    game_on = True if play_game.lower()[0] == 'y' else False

    while game_on:
        if turn == 'Player 1':
            helper_functions.display_board(board)
            position = helper_functions.player_choice(board)
            helper_functions.place_marker(board, player1_marker, position)

            if helper_functions.win_check(board, player1_marker):
                helper_functions.display_board(board)
                print(f'Congratulations! {player1} have won the game!')
                game_on = False
            else:
                if helper_functions.full_board_check(board):
                    helper_functions.display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            helper_functions.display_board(board)
            position = helper_functions.player_choice(board)
            helper_functions.place_marker(board, player2_marker, position)
            if helper_functions.win_check(board, player2_marker):
                helper_functions.display_board(board)
                print(f'Congratulations!  {player2} have won the game!')
                game_on = False
            else:
                if helper_functions.full_board_check(board):
                    helper_functions.display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not helper_functions.replay():
        break