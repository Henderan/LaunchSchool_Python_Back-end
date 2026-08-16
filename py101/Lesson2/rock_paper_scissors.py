import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard']
CHOICE_KEYS = ['r', 'p', 'sc', 'sp', 'l']
CHOICE_MAPPING = dict(zip(CHOICE_KEYS, VALID_CHOICES))
WINNING_COMBOS = {
    'rock':     ['scissors', 'lizard'],
    'paper':    ['rock',     'spock'],
    'scissors': ['paper',    'lizard'],
    'spock':    ['rock',     'scissors'],
    'lizard':   ['paper',    'spock'],
}
WINNING_SCORE = 3

def prompt(message):
    print(f'==> {message}')

def match_complete():
    return WINNING_SCORE in [user_score, computer_score]

def determine_winner():
    global winner, user_score, computer_score

    if user_choice == computer_choice:
        winner = 'tie'
    elif computer_choice in WINNING_COMBOS[user_choice]:
        winner = 'user'
        user_score += 1
    else:
        winner = 'computer'
        computer_score += 1

def display_winner():
    if winner == 'user':
        prompt('You win!')
    elif winner == 'computer':
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")

def determine_grand_winner():
    global grand_winner

    if user_score == WINNING_SCORE:
        grand_winner = 'user'
    else:
        grand_winner = 'computer'

def display_grand_winner():
    if grand_winner == 'user':
        prompt('You are the grand winner!')
    else:
        prompt('Computer is the grand winner!')

grand_winner = ''
play_match = 'y'

while play_match == 'y':
    user_score = 0
    computer_score = 0
    winner = ''

    while not match_complete(): 
        prompt(f'Choose one:  {[value + '[' + key + ']' 
                                for key, value in CHOICE_MAPPING.items()]}')
        user_choice_key = input()

        while user_choice_key not in CHOICE_MAPPING:
            prompt("That's not a valid choice")
            user_choice_key = input()
        user_choice = CHOICE_MAPPING[user_choice_key]

        computer_choice = random.choice(VALID_CHOICES)

        prompt(f'You chose {user_choice}, computer chose {computer_choice}')

        determine_winner()
        display_winner()

    determine_grand_winner()
    display_grand_winner()

    while True:
        prompt('Would you like to play again? (y/n)')
        answer = input()[0].lower()
        if answer in ['y', 'n']:
            play_match = answer
            break
