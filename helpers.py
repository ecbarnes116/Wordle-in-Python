from multiprocessing.connection import answer_challenge
from unittest.mock import DEFAULT

import random
from colorama import Fore, Back, Style # Back and Style are not being used currently, don't need
from word_bank import word_list
from answer_bank import answer_list

WORD_LENGTH = 5

# Get rid of this by making a new file where every answer is already in CAPS
########################################################
answer_list = [answer.upper() for answer in answer_list]
########################################################

def get_random_answer():
    answer = answer_list[random.randint(0, 1367)]

    return answer



def get_valid_guess(round):
    round = round
    guess_is_valid = True
    
    print("Attempt: ", round)

    guess = input("Enter your guess here: ").upper()

    if len(guess) != WORD_LENGTH:
        print("Guess needs to be 5 letters!", '\n')
        guess_is_valid = False

    elif (guess not in answer_list) and (guess not in word_list):
        print("Guess must be a valid word!", '\n')
        guess_is_valid = False
    
    return guess, guess_is_valid



def check_guess(guess, answer, round, yellow_letters, green_letters, black_letters, output):
    guess = guess
    answer = answer
    round = round
    yellow_letters = yellow_letters
    green_letters = green_letters
    black_letters = black_letters
    output = output

    # Logic is not 100% fixed, repeated letters still fail in certain cases
    # Try using "if letter in string" and "if letter not in string" for yellow and black
    
    #######################################################################
    for i in range(0, WORD_LENGTH):
            for j in range(0, WORD_LENGTH):
                if (guess[i] == answer[i]):
                    output[round-1][i] = Fore.GREEN + guess[i] + Fore.RESET
                    break

                if (guess[i] == answer[j]):
                    output[round-1][i] = Fore.YELLOW + guess[i] + Fore.RESET
                    break
                
                else:
                    output[round-1][i] = Fore.BLACK + guess[i] + Fore.RESET
    #######################################################################

    return output



def output_guess(output):
    output = output

    for list in output:
        for letter in list:
                print(letter, end=' ')
        print()
    print()



# Take a look at these "in_" variables and decide whether or not to rename them
def check_win(in_guess, in_answer, in_round, in_win):
    guess = in_guess
    answer = in_answer
    round = in_round
    win = in_win

    if guess == answer:
        win = True
        print("You win! The answer was:", guess)

        if round == 1:
            print("You must have cheated!")

        else:
            print("You guessed the answer in", round, "attempts.", '\n')

    round += 1

    return win, round
