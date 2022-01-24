# 12 character random password generator

# List process structure:
# var : Defining the list as a string.
# var_list : Split string into a definable list.
# rand_var : Random selection from list.
# rand_var_str : Convert list to string.


import time
import string
import random

# First word list
words_1 = "blue teal spot feel drag work sudo snow soda nope goth heat goat arch ouch free lock luck pick pond corn cube fire wind pink rune push posh grey zeal jazz kill join"
word_list_1 = words_1.split()
rand_word_1 = random.choices(word_list_1)
rand_word_str_1 = " ".join(rand_word_1)

# Second word list
words_2 = "First Split Crash Grown Throw Enter Flame Water Earth Trash Green Violet Cloud Rhino Tiger Dread Death Third Egypt Claim Grass Goose Moose"
word_list_2 = words_2.split()
rand_word_2 = random.choices(word_list_2)
rand_word_str_2 = " ".join(rand_word_2)

# Integer list
int = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
int_list = int.split()
rand_int = random.choices(int_list)
rand_int_str = " ".join(rand_int)

# Character list
cha = "! $ @ % ? #"
cha_list = cha.split()
rand_cha = random.choices(cha_list)
rand_cha_str = " ".join(rand_cha)



print(f"Your password is: {rand_word_str_1}{rand_word_str_2}{rand_int_str}{rand_cha_str}")
time.sleep(2)
print("Your new password will not be saved or displayed after the program is closed. 
