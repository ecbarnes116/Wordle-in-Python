from helpers import *

answer = get_random_answer()
guess = ""

guess_is_valid = True
win = False
round = 1

green_letters = ['_', '_', '_', '_', '_']
yellow_letters = []
black_letters = []

output = [["_", "_", "_", "_", "_"], 
          ["_", "_", "_", "_", "_"], 
          ["_", "_", "_", "_", "_"], 
          ["_", "_", "_", "_", "_"], 
          ["_", "_", "_", "_", "_"], 
          ["_", "_", "_", "_", "_"]]

#############
#print(answer)
#############

while win == False:
    if round > 6:
        print("You lose! The answer was:", answer)
        break

    guess, guess_is_valid = get_valid_guess(round)
    
    if guess_is_valid == True:
        output = check_guess(guess, answer, round, yellow_letters, green_letters, black_letters, output)

        output_guess(output)

        # Maybe add functionality to say "try" if geussed on 1st try
        win, round = check_win(guess, answer, round, win)

