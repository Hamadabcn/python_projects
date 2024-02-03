import random
from words import words
from hangman_visual import lives_visual_dict
import string

def get_valid_word(words):
    # This function returns a random word from the words list that does not contain '-' or ' '
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words) # chooses another word if the first one is not valid

    return word.upper() # returns the word in uppercase


def hangman():
    # This function lets the player play a game of hangman
    word = get_valid_word(words) # gets a valid word using the get_valid_word function
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase) # all the uppercase letters in the alphabet
    used_letters = set()  # what the user has guessed

    lives = 7 # number of lives the player has

    # getting user input
    while len(word_letters) > 0 and lives > 0: # loop until the player guesses the word or runs out of lives
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('\nYou have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word] # shows the guessed letters and the blanks
        print(lives_visual_dict[lives]) # shows the hangman stage based on the lives left
        print('Current word: ', ' '.join(word_list)) # prints the current word

        user_letter = input('Guess a letter: ').upper() # asks the user to guess a letter and converts it to uppercase
        if user_letter in alphabet - used_letters: # checks if the user's letter is a valid letter that has not been used before
            used_letters.add(user_letter) # adds the user's letter to the used letters set
            if user_letter in word_letters: # checks if the user's letter is in the word
                word_letters.remove(user_letter) # removes the user's letter from the word letters set
                print('') # prints an empty line

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.') # prints a message that the letter is not in the word

        elif user_letter in used_letters: # checks if the user's letter has been used before
            print('\nYou have already used that letter. Guess another letter.') # prints a message that the letter has been used

        else:
            print('\nThat is not a valid letter.') # prints a message that the letter is not valid

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0: # checks if the player has no lives left
        print(lives_visual_dict[lives]) # shows the final hangman stage
        print('You died, sorry. The word was', word) # prints a message that the player lost and shows the word
    else:
        print('YAY! You guessed the word', word, '!!') # prints a message that the player won and shows the word


if __name__ == '__main__':
    while True: # starts an infinite loop to play multiple games
        hangman() # calls the hangman function to play a game
        play_again = input("\nWould you like to play again? (yes/no): ") # asks the user politely if they want to play again
        if play_again.lower() != 'yes': # checks if the user does not want to play again
            break # breaks out of the loop
    
    print("\nThank you for playing hangman! Have a nice day!") # prints a farewell message when the game ends

