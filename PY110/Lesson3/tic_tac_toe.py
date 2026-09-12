import os
import random
import time

INITIAL_MARKER = ' '
PLAYER1_MARKER = 'X'
PLAYER2_MARKER = 'O'
PLAYER_MARKERS = (PLAYER1_MARKER, PLAYER2_MARKER)
WINNING_SCORE = 5
WINNING_LINES = ((1, 2, 3), (4, 5, 6), (7, 8, 9), # rows
                 (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columns
                 (1, 5, 9), (3, 5, 7))            # diagonals


def join_or(sequence, separator=', ', word='or'):
    match len(sequence):
        case 0:
            return ''
        case 1:
            return str(sequence[0])
        case 2:
            return f'{sequence[0]} {word} {sequence[1]}'
        
    leading_items = separator.join(sequence[:-1])
    last_item = sequence[-1]
    return f'{leading_items}{separator}{word} {last_item}'


def prompt(message):
    print(f"=> {message}")


def prompt_player_order():
    while True:
        prompt('Would you like to go first(1) or second(2) for this match?')
        human_order = input().strip()
        if human_order in ('1', '2'):
            if human_order == '1':
                return ('Human', 'Computer')
            else:
                return ('Computer', 'Human')
        prompt('Invalid selection.  Please enter 1 or 2.')


def prompt_play_again():
    play_again = ''
    while play_again not in ('y', 'yes', 'n', 'no'):
        prompt("Play another match? (y or n)")
        play_again = input().lower()
        if play_again not in ('y', 'yes', 'n', 'no'):
            prompt("Your response was not valid.")

    return play_again


def display_match_score(match_score):
    prompt(f"MATCH SCORE:  You: {match_score['Human']}, Computer: {match_score['Computer']}")


def display_board(game_number, player_order, match_score, board):
    os.system('clear')

    if player_order[0] == 'Human':
        predicate1 = 'You are'
        predicate2 = 'Computer is'
    else:
        predicate1 = 'Computer is'
        predicate2 = 'You are'

    prompt(f"Game {game_number}")
    prompt(f"{predicate1} Player 1 ('{PLAYER1_MARKER}'). " 
           f"{predicate2} Player 2 ('{PLAYER2_MARKER}').")
    display_match_score(match_score)
    prompt(f"First player to win {WINNING_SCORE} games wins the match.")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')


def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}


def board_full(board):
    return len(empty_squares(board)) == 0


def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]


def optimal_choice(player_marker, board):
    def optimal_choice_helper(target_marker, board):
        for line in WINNING_LINES:
                string = board[line[0]] + board[line[1]] + board[line[2]]
                count_target_marks = string.count(target_marker)
                count_empty_marks = string.count(INITIAL_MARKER)
                if count_target_marks == 2 and count_empty_marks == 1:
                    for square in line:
                        if board[square] == INITIAL_MARKER:
                            return square
        return None

    offensive_choice = optimal_choice_helper(player_marker, board)
    if offensive_choice:
        return offensive_choice

    opponent_marker = PLAYER_MARKERS[0] if player_marker == PLAYER_MARKERS[1] else PLAYER_MARKERS[1]
    defensive_choice = optimal_choice_helper(opponent_marker, board)
    if defensive_choice:
        return defensive_choice
                                           
    return None


def computer_chooses_square(player_marker, board):
    square = optimal_choice(player_marker, board)
    if not square:
        if 5 in empty_squares(board):
            square = 5
        else:
            square = random.choice(empty_squares(board))
    board[square] = player_marker


def human_chooses_square(player_marker, board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break
        prompt("Sorry, that's not a valid choice.")
    board[int(square)] = player_marker


def player_chooses_square(player, player_marker, board):
    if player == 'Human':
        human_chooses_square(player_marker, board)
    else:
        computer_chooses_square(player_marker, board)


def is_game_winner(player_marker, board):
    for line in WINNING_LINES:
            sq1, sq2, sq3 = line
            if (board[sq1] == player_marker
                    and board[sq2] == player_marker
                    and board[sq3] == player_marker):
                return True
    return False


def is_match_winner(player, match_score):
    return match_score[player] == WINNING_SCORE


def play_tic_tac_toe():
    session_over = False

    while not session_over:
        # set up match
        game_number = 1
        match_score = {'Human': 0, 'Computer': 0}
        match_over = False
        os.system('clear')
        player_order = prompt_player_order()

        while not match_over:
            # set up game
            game_over = False
            game_winner = None
            board = initialize_board()
            display_board(game_number, player_order, match_score, board)

            # associate players with their markers
            players_and_markers = tuple(zip(player_order, PLAYER_MARKERS))

            while not game_over:
                for player, player_marker in players_and_markers:
                    player_chooses_square(player, player_marker, board)
                    display_board(game_number, player_order, match_score, board)

                    if is_game_winner(player_marker, board):
                        game_winner = player
                    if game_winner or board_full(board):
                        game_over = True
                        break
            
                    time.sleep(1)
            
            if game_winner:
                match_score[game_winner] += 1
                display_board(game_number, player_order, match_score, board)
                msg_map = {'Computer': 'Computer', 'Human': 'You'}
                prompt(f"{msg_map[game_winner]} won game {game_number}!")
                if is_match_winner(game_winner, match_score):
                    prompt(f'{msg_map[game_winner]} won the match!')
                    match_over = True
            else:
                prompt("It's a tie!")

            prompt('Press Enter to continue:')
            input()

            game_number += 1

        play_again = prompt_play_again()
        if play_again in ('n', 'no'):
            session_over = True

    prompt('Thanks for playing Tic Tac Toe!')


play_tic_tac_toe()
