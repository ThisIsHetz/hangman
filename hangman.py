#! /usr/bin/python3

# hangman.py
# a simple hangman style game in Python3

import random
from os import system, name


def clear():
    # clearing the command prompt / terminal
    if name == 'nt': # for windows
        system('cls')
    if name == 'posix': # for linux & Mac
        system('clear')


def set_word(wordlist):
    # pick a word at random from the wordlist
    # break the word into a list of it's individual letters
    # create a matching list of underscores to represent
    # unguessed letters
    winning_word = random.choice(wordlist)
    winning_word = [letter for letter in winning_word]
    guess_status = ['_' for letter in winning_word]
    return winning_word, guess_status


def game_loop(wordlist):
    winning_word, guess_status = set_word(wordlist)
    guessed_letters = []
    wrong_guesses = 0

    win_lose = False

    # loop until a winning or losing condition is achieved
    while win_lose != True:
        clear()
        print(' '.join(guess_status))
        print(f"Guessed Letters: {' '.join(sorted(guessed_letters))}")
        print(f"Remaining Guesses: {6 - wrong_guesses}")

        # losing condition
        # 6 is arbitrary and represents the head, body, two arms and
        # two legs in a traditional game of hangman
        # this can be higher or lower to provide more or less guesses
        if wrong_guesses == 6:
            win_lose == True
            clear()
            print("Game Over\n")
            print(f"The word was: {' '.join(winning_word)}\n")

            # check for new game
            again = input("Play again? (y/n): ")
            if again == 'y':
                return True
            elif again == 'n':
                return False

        # winning condition
        if guess_status == winning_word:
            win_lose == True
            clear()
            print("You Won!\n")
            print(f"You gussed correctly: {' '.join(winning_word)}\n")

            # check for new game
            again = input("Play again? (y/n): ")
            if again == 'y':
                return True
            elif again == 'n':
                return False

        guess = input("Enter a letter: ")
        if guess in guessed_letters:
            pass
        elif guess in winning_word:
            guessed_letters.append(guess)
            letter_locs = [value for value, x in enumerate(winning_word) if x == guess]
            for i in letter_locs:
                guess_status[i] = guess
        else:
            guessed_letters.append(guess)
            wrong_guesses += 1
        

def main():
    # create wordlist from wordlist file, stripping any
    # newline characters or trailing whitespace
    wordlist = [line.strip() for line in open('wordlist.txt')]

    # game set to True & remains true unless
    # 'n' is provided during the game_loop to
    # confirm a new game is not desired
    game = True
    while game == True:
        game = game_loop(wordlist)


if __name__ == "__main__":
    main()