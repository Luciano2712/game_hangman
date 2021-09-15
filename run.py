# Import tools and libraries
import random
from words import words
import string  # Import pre-dertermined list of uppercased characteres


# Getting a valid word with only letters from our WORDS list
def get_valid_word(words):
    word = random.choice(words)  # Randomly chooses a word from the list
    while "-" in word or " " in word:
        word = random.choice(words)  # Loops trhough list, getting valid words

    return word.upper()  # Return valid word, uppercased to make it standard


# Keep track of possible guesses and letters already guessed
def hangman():
    # Add a counter for lives
    lives = 7

    word = get_valid_word(words)  # Call get_valid_word function
    word_letters = set(word)  # Set of letters in the word
    alphabet = set(string.ascii_uppercase)  # Import pre-dertermined list
    used_letters = set()  # Keep track of what user has guessed

    while len(word_letters) > 0 and lives > 0:  # Loops until finds all letters
        # Join and print letters already used
        print(f"You have {lives} lives left!")
        print("You have used these letters: ", " ".join(used_letters))
        # Show what current word is
        word_l = [letter if letter in used_letters else "-" for letter in word]
        print("\nSecret word: ", " ".join(word_l))
        # Getting user input
        user_letter = input("\nGuess a letter: ").upper()  # User Input
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)  # Add valid letter
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # Remove letter from word

            else:
                lives = lives - 1  # Removes a life if wrong
                print("Letter is not in word.")

        elif user_letter in used_letters:  # Check for repeated letters
            print("\nYou have already used this letter. Please try again: ")

        else:  # Check for invalid characteres
            print("\nInvalid character. Please try again: ")
    # Print when the word is guessed correctly
    if lives == 0:
        print("You lost, sorry. The word was", word)
    elif len(word_letters) == 0:
        print("\nCongratulations ** YOU WON **")
        print("The word is", word)


# Call function for the game to start
hangman()
