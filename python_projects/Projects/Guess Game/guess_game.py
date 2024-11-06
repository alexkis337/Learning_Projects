import random


highscores = {}

def show_score():
    if len(highscores) == 0:
        print("There is no highscores yet")
    else:
        for player in highscores:
            print(f'{player} with score of {highscores[player]}\n')

def start_game():
    curr_score = 0
    curr_guess = 0
    n_to_guess = random.randint(1, 100)
    print('Sup mate, the game has started!')
    player_name = input('What\'s your name?\n')
    highscores[player_name] = 0
    want_to_play = input(f'Hi {player_name}, wanna play? [Enter Yes/No]\n')
    if want_to_play.lower() != 'yes':
        print('Bye, looser')
        exit()
    else:
        show_score()

    print('Guess the number, nerd')
    while curr_guess != n_to_guess:
        try:
            curr_guess = int(input('Sooo?\n'))
        except ValueError:
            print('Please enter integer')
            continue

        curr_score += 1
        print(curr_score)
        if curr_guess == n_to_guess:
            print('Gratz, you\'re the champ. Woooo')
            highscores[player_name] = curr_score
            show_score()

            try_again = input('Wanna one more?\n')
            if try_again.lower() == 'yes':
                start_game()
            else:
                print('Cya, lad')
                break

        elif curr_guess < n_to_guess:
            print('Think bigger')
        else:
            print('Mb some smaller?')


start_game()
show_score()


