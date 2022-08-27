#   for i in range(0, WORD_LENGTH):
#             for j in range(0, WORD_LENGTH):
#                 if (guess[i] == answer[j]) and (guess[i] not in yellow_letters):
#                     yellow_letters.append(guess[i])

#                 if (guess[i] == answer[i]):
#                     green_letters[i] = Fore.GREEN + guess[i] + Fore.RESET
                
#             if (guess[i] not in yellow_letters) and (guess[i] not in black_letters):
#                 black_letters.append(guess[i])

#     #print("Yellow:", *yellow_letters)

#     print(f"Black: {' '.join((Fore.BLACK + letter + Fore.RESET) for letter in black_letters)}")
#     print(f"Yellow: {' '.join((Fore.YELLOW + letter + Fore.RESET) for letter in yellow_letters)}")
#     print(f"Green: {' '.join((letter) for letter in green_letters)} \n")

