import os
import random

def join_and(sequence, separator=', ', word='and'):
    match len(sequence):
        case 0:
            return ''
        case 1:
            return str(sequence[0])
        case 2:
            return f'{sequence[0]} {word} {sequence[1]}'

    leading_items = separator.join([str(num) for num in sequence[:-1]])
    last_item = sequence[-1]
    return f'{leading_items}{separator}{word} {last_item}'


def prompt(msg):
    print(f'==> {msg}')


def prompt_begin():
    prompt('Press Enter to begin:')
    input()


def prompt_continue():
    prompt('Press Enter to continue:')
    input()


def prompt_action():
    while True:
        prompt('Do you wish to hit(h) or stay(s)?')
        action = input().lower()
        if action not in ('h', 's'):
            prompt('Invalid response.')
        else:
            break
    return action


def prompt_yes_no(msg):
    while True:
        print('')
        prompt(f'{msg} (y or n)')
        answer = input().lower()
        if answer not in ('y', 'yes', 'n', 'no'):
            prompt('Invalid selection.')
        else:
            return answer[0]


def prompt_play_again():
    return prompt_yes_no('Do you want to play again?')


def prompt_rules():
    return prompt_yes_no('Do you want to read the rules?')


def display_rules():
    rules = '''
    INTRODUCTION TO TWENTY-ONE

    Twenty-one is a card game whose objective is for the player to reach
    the highest card count without exceeding 21, known as going bust.  
    Numbered cards are worth their face value, face cards are worth 10, and
    aces are worth either 1 or 11, depending on which gives the highest total
    count without the hand going bust. The game proceeds by the dealer dealing 
    one card to the player face-up, one card to the dealer face-up, another 
    card to the player face-up, and another card to the dealer face-down.
    The player has the option of requesting an additional card.  This request
    is called a hit. The player can keep hitting until their total reaches 21.
    When the player no longer wishes to receive any more cards, they 'stay',
    and the dealer takes a turn, which starts with the dealing flipping over
    the face-down card, and proceeds with the dealer hitting or staying.  The 
    first player to bust loses.  If neither player busts, the player with the 
    highest score wins.  If the scores are equal, the players tie.
    '''

    os.system('clear')
    print(rules)


def initialize_deck(game_state):
    deck = []
    numbered = list(range(2, 11))
    for card in (*numbered, 'Jack', 'Queen', 'King', 'Ace'):
        deck.extend([card] * 4)
    game_state['deck'] = deck


def deal(game_state):
    for _ in range(2):
        for hand in (game_state['player_hand'], game_state['dealer_hand']):
            index = random.choice(range(len(game_state['deck'])))
            hand.append(game_state['deck'].pop(index))

    prompt('Cards dealt.\n')
    game_state['player_hand'].sort(key=sort_value)


def sort_value(card):
    match card:
        case int():
            return card
        case 'Jack':
            return 11
        case 'Queen':
            return 12
        case 'King':
            return 13
        case 'Ace':
            return 14


def display_hands(game_state):
    if game_state['dealer_card_hidden']:
        hidden_dealer_card = game_state['dealer_hand'][0]
        dealer_str = f"Dealer has:     {hidden_dealer_card} and unknown card"
    else:
        dealer_str = f"Dealer has:     {join_and(game_state['dealer_hand'])}"

    player_str     = f"You have:       {join_and(game_state['player_hand'])}\n"

    prompt(dealer_str)
    prompt(player_str)


def display_score(game_state):
    if game_state['dealer_card_hidden']:
        print('')
    else:
        prompt(f"Dealer's score: {game_state['dealer_score']}")

    prompt(f"Your score:     {game_state['player_score']}")


def reveal_dealer_card(game_state):
    os.system('clear')
    revealed_card = game_state['dealer_hand'][1]
    if revealed_card in (8, 'Ace'):
        prompt(f'Dealer reveals an {revealed_card}.\n')
    else:
        prompt(f'Dealer reveals a {revealed_card}.\n')

    game_state['dealer_hand'].sort(key=sort_value)
    game_state['dealer_card_hidden'] = False


def hit(deck, hand):
    index = random.choice(range(len(deck)))
    card = deck.pop(index)

    hand.append(card)
    hand.sort(key=sort_value)

    return card


def hit_msg(card, participant):
    match participant:
        case 'dealer':
            subject = 'Dealer'
            verb1 = 'hits'
            verb2 = 'gets'
        case 'player':
            subject = 'You'
            verb1 = 'hit'
            verb2 = 'get'
    prompt(f'{subject} {verb1}.')
    if card in (8, 'Ace'):
        prompt(f'{subject} {verb2} an {card}.')
    else:
        prompt(f'{subject} {verb2} a {card}.')


def busted(hand_score):
    return hand_score > 21


def dealer_takes_turn(game_state):
    while True:
        score = game_state['dealer_score']
        if score < 17:
            os.system('clear')
            card = hit(game_state['deck'], game_state['dealer_hand'])
            game_state['dealer_score'] = score_hand(game_state['dealer_hand'])
            hit_msg(card, 'dealer')
            display_status(game_state)
            if not busted(game_state['dealer_score']):
                prompt_continue()
        else:
            if 17 <= score <= 21:
                os.system('clear')
                prompt('Dealer stays.\n')
                display_status(game_state)
            return score


def player_takes_turn(game_state):
    while True:
        score = game_state['player_score']
        if score >= 21:
            if score == 21:
                prompt('Your turn is over.')
                prompt_continue()
            return score

        if prompt_action() == 'h':
            os.system('clear')
            card = hit(game_state['deck'], game_state['player_hand'])
            game_state['player_score'] = score_hand(game_state['player_hand'])
            hit_msg(card, 'player')
            display_status(game_state)
        else:
            os.system('clear')
            prompt('You stay.\n')
            display_status(game_state)
            return score


def determine_outcome(game_state):
    dealer_score = game_state['dealer_score']
    player_score = game_state['player_score']
    dealer_card_hidden = game_state['dealer_card_hidden']

    if not busted(player_score) and dealer_card_hidden:
        outcome = 'in_progress'
    elif busted(player_score):
        outcome = 'player_busted'
    elif busted(dealer_score):
        outcome = 'dealer_busted'
    elif dealer_score > player_score:
        outcome = 'dealer_high_score'
    elif dealer_score < player_score:
        outcome = 'player_high_score'
    else:
        outcome = 'tie'

    return outcome


def display_outcome(outcome, game_state):
    match outcome:
        case 'in_progress':
            message = 'Game is still in progress.'
        case 'player_busted':
            hidden_dealer_card = game_state['dealer_hand'][1]
            if hidden_dealer_card in (8, 'Ace'):
                article = 'an'
            else:
                article = 'a'
            message = ('You busted. Dealer wins!\n'
                       '==> (Dealer flips over hidden card to reveal ' 
                       f'{article} {hidden_dealer_card}.)')
        case 'dealer_busted':
            message = 'Dealer busted. You win!'
        case 'dealer_high_score':
            message = 'Dealer has the highest score. Dealer wins!'
        case 'player_high_score':
            message = 'You have the highest score. You win!'
        case _:
            message = "It's a tie!"

    prompt(message)


def score_hand(hand):
    total = 0
    aces = 0
    for card in hand:
        if card == 'Ace':
            aces += 1
            total += 11
        elif card in ('Jack', 'Queen', 'King'):
            total += 10
        else:
            total += card

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return total


def display_status(game_state):
    print('')
    print('------------------------------------------')
    display_hands(game_state)
    display_score(game_state)
    print('------------------------------------------')
    print('')
    print('')


def play_21():
    os.system('clear')
    prompt('Welcome to Twenty-one!\n')
    if prompt_rules() == 'y':
        display_rules()
    prompt_begin()

    while True:
        os.system('clear')
        game_state = {
            'dealer_card_hidden': True,
            'dealer_hand': [],
            'player_hand': [],
            'dealer_score': 0,
            'player_score': 0,
        }
        initialize_deck(game_state)
        random.shuffle(game_state['deck'])
        deal(game_state)
        game_state['dealer_score'] = score_hand(game_state['dealer_hand'][:1])
        game_state['player_score'] = score_hand(game_state['player_hand'])
        display_status(game_state)

        while True:
            player_takes_turn(game_state)

            checkpoint = determine_outcome(game_state)
            if checkpoint != 'in_progress':
                display_outcome(checkpoint, game_state)
                break

            reveal_dealer_card(game_state)
            game_state['dealer_score'] = score_hand(game_state['dealer_hand'])
            display_status(game_state)
            prompt_continue()

            dealer_takes_turn(game_state)

            outcome = determine_outcome(game_state)
            display_outcome(outcome, game_state)
            break

        if prompt_play_again() == 'n':
            break


play_21()