import random
from words import words
import string  # import pre-dertermined list of uppercased characteres


# Getting a valid word with only letters from our WORDS list
def get_valid_word(words):
    word = random.choice(words)  # randomly chooses a word from the list
    while "-" in word or " " in word:
        word = random.choice(words)  # loops trhough list, getting valid words

    return word.upper()  # return valid word, uppercased to make it standard


# Keep track of possible guesses and letters already guessed
def hangman():
    word = get_valid_word(words)  # call get_valid_word function
    word_letters = set(word)  # set of letters in the word
    alphabet = set(string.ascii_uppercase)  # import pre-dertermined list
    used_letters = set()  # keep track of what user has guessed

    while len(word_letters) > 0:  # loops until all letters are found
        # Join and print letters already used
        print("You have used these letters: ", " ".join(used_letters))
        # Show what current word is
        word_l = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_l))

        user_letter = input("Guess a letter: ").upper()  # User Input
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)  # Add valid letter
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # Remove letter from word

        elif user_letter in used_letters:  # Check for repeated letters
            print("\nYou have already used this letter. Please try again: ")

        else:  # Check for invalid characteres
            print("\nInvalid character. Please try again: ")


hangman()
