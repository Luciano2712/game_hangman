import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses a word from the list
    while "-" in word or " " in word:
        word = random.choice(words)  # loops trhough list, getting valid words

    return word.upper()  # return valid word, uppercased to make it standard


def hangman():
    word = get_valid_word(words)  # call get_valid_word function
    word_letters = set(word)  # set letters in the word
    alphabet = set(string.ascii_uppercase)  # import pre-dertermined list of uppercased characteres.
    used_letters = set()  # keep track of what user has guessed
