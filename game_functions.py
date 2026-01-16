import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    # current_val != next_val 
    actual_compare = ''
    compare = max(current_val,next_val)
    if compare == current_val:
        actual_compare = 'l'
    else: 
        actual_compare = 'h'
    
    return actual_compare == user_input
    


# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    pass
