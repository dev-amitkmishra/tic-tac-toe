import helper_functions

print('Welcome to Tic-Tac-Toe')

while True:
    # Reset the board
    board = [' '] * 10
    player1_marker, player2_marker = helper_functions.player_input()
    turn = helper_functions.choose_first()
    print(turn, ' will start first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    # game_on = True if play_game.lower()[0] == 'y' else False
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            helper_functions.display_board(board)
            position = helper_functions.player_choice(board)
            helper_functions.place_marker(board, player1_marker, position)

            if helper_functions.win_check(board, player1_marker):
                helper_functions.display_board(board)
                print('Congratulations! Player 1 have won the game!')
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
                print('Congratulations! Player 2 have won the game!')
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