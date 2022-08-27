# Get 5 letter words from a list of 10,000 most 
# common words between 5-8 letters

file_in = "huge_word_list"
file_out = "new_word_bank"

input_file = f"wordle_code\word_list\{file_in}.txt"
output_file = f"wordle_code\word_list\{file_out}.txt"

ALL_word_list = []
five_letter_words = []

with open(input_file, 'r') as f:
    for line in f.readlines():
        word = (line.strip()).upper()
        ALL_word_list.append(word)

for word in ALL_word_list:
    if len(word) == 5:
        five_letter_words.append(word)

with open(output_file, 'w') as f:
    for word in five_letter_words:
        f.write(word + "\n")

