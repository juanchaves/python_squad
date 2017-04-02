'''
Rock, Paper, Scissors
'''
import random

prompt_error = 'You did not select from the allowed options'

print('Hello and welcome to the rock, paper, scissors game!\n')
game_is_active = True

while game_is_active:
    options = ['rock', 'paper', 'scissors']
    player_choice = input('Choose to throw rock, paper or scissors ')
    player_choice.lower()
    while player_choice not in options
        print(prompt_error)
        player_choice = input('Choose to throw: rock, paper or scissors ')
        player_choice.lower()

    computer_choice = random.choice(option)
    print(computer_choice)

    while type(game_is_active) is not bool:
        game_is_active = input('Would you like to keep playing? (y/n) ')
        game_is_active.lower()

        if game_is_active == 'y' or if game_is_active == 'yes':
            game_is_active = True
        elif game_is_active == 'n' or if game_is_active == 'no':
            game_is_active = False
        else:
            print(prompt_error)
