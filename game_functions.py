import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    #x = random.choice(poss_values)   
    x = poss_values[int(len(poss_values)/2)]
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
    if letter in word:
        indlis = []
        for x in range(len(word)):
            if word[x] == letter:
                board[x] = letter
        print("Well done! "+ letter + " is in the word")
        return True
    else:
        print("Sorry, " + letter +" is not in the word")
        return False
    
    #pass
