import random

def guess(x):
    # This function lets the player guess a random number between 1 and x
    random_number = random.randint(1, x) # Generate a random number
    guess = 0 # Initialize the guess variable
    while guess != random_number: # Loop until the guess is correct
        try:
            guess = int(input(f'\nGuess a number between 1 and {x}: ')) # Ask the player for a guess
            if guess < 1 or guess > x: # Check if the guess is out of range
                print(f"Please enter a number between 1 and {x}.")
                continue # Skip the rest of the loop and ask again
            if guess < random_number: # Check if the guess is too low
                print("\nGuess is low")
            elif guess > random_number: # Check if the guess is too high
                print("\nGuess is high")
        except ValueError: # Catch the exception if the input is not a valid number
            print("Invalid input. Please enter a valid number.")
            
    print(f"\nWow, congrats! You have guessed the number {random_number} correctly!") # Congratulate the player

def computer_guess(x):
    # This function lets the computer guess the player's number between 1 and x
    low = 1 # Initialize the lower bound
    high = x # Initialize the upper bound
    feedback = '' # Initialize the feedback variable
    while feedback != 'c': # Loop until the feedback is 'c' for correct
        if low != high: # Check if there is more than one possible number
            guess = random.randint(low, high) # Generate a random guess within the range
        else:
            guess = low # If there is only one possible number, use that as the guess
        feedback = input(f'\nIs {guess} too high (H), too low (L), or correct (C)?? ').lower() # Ask the player for feedback
        if feedback == 'h': # If the feedback is 'h' for too high, adjust the upper bound
            high = guess - 1
        elif feedback == 'l': # If the feedback is 'l' for too low, adjust the lower bound
            low = guess + 1
    print(f'\nYay! The computer guessed your number, {guess}, correctly!') # Congratulate the computer

print("\nWelcome to the guessing game!") # Print a welcome message
print("\nYou can choose between two games: ") # Print the game options
print("\n1. You guess the computer's number")
print("\n2. The computer guesses your number")

while True: # Start an infinite loop to play multiple games
    game_choice = input("\nChoose a game: '1' for guess your number or '2' for computer guesses your number: ") # Ask the player to choose a game
    
    if game_choice == '1': # If the player chooses game 1, let them guess the computer's number
        try:
            max_number = int(input("\nEnter the maximum number to guess (e.g., 100): ")) # Ask the player to enter the maximum number for guessing
            guess(max_number) # Call the guess function with that number as an argument
        except ValueError: # Catch the exception if the input is not a valid number
            print("Invalid input. Please enter a valid number.")
    elif game_choice == '2': # If the player chooses game 2, let the computer guess their number
        try:
            max_number = int(input("\nEnter the maximum number for the computer to guess (e.g., 100): ")) # Ask the player to enter the maximum number for guessing
            computer_guess(max_number) # Call the computer_guess function with that number as an argument
        except ValueError: # Catch the exception if the input is not a valid number
            print("Invalid input. Please enter a valid number.")
    else:
        print("\nInvalid choice. Please enter '1' for guess() or '2' for computer_guess().") # If the player enters an invalid choice, print an error message
    
    play_again = input("\nDo you want to play again? (yes/no): ").lower() # Ask the player if they want to play again
    if play_again != 'yes': # If they don't want to play again, break out of the loop
        break

print("\nThank you for playing the guessing game! Have a nice day!") # Print a farewell message when the game ends
