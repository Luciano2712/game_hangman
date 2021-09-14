# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import words

def get_valid_word(words):
    word = random.choice(words) #randomly chooses a word from the list
    while "-" in word or " " in word:
        word = random.choice(words) #loops trhough the list getting only valid words

    return word.upper() #return valid word and uppercase it to make it standard