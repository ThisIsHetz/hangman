# hangman.py

## A command-line/terminal implementation of the game Hangman

Running the script puts the player immediatley into a game. At the end of the game the player is prompted for a **y** or **n** to indicate if they'd like to play again. There is currently no error-handling, input validating, and input is expected to be single, lowercase letters. The provided **wordlist.txt** is a modification of an Oxford 3000 wordlist with the removal of lines containing digits, punctuation, whitespace, or words of a length shorter than five letters.

When the game begins the player is presented with a series of underscores to represent the unguessed letters of a word. The player has a limit of six incorrect guesses (representing the head, body, two arms & two legs in a typical game of Hangman) to correctly guess the word. Duplicate guesses do not count against the player's limit of incorrect guesses.
