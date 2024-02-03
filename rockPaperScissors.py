import random

def play():
    # This function lets the player play a round of Rock, Paper, Scissors against the computer
    user = input("\nWhat's your choice? 'r' for Rock🪨, 'p' for Paper🧻, and 's' for Scissors✂️  : ") # Ask the player for their choice
    computer = random.choice(['r', 'p', 's']) # Generate a random choice for the computer
    
    if user == computer: # Check if the choices are the same
        return f'\nYou and the computer both chose {user}. It\'s a tie!\n' # Return a tie message with the choice
    
    # r > s , s > p, p > r 
    if is_win(user, computer): # Check if the player wins using the is_win function
        return f'\nYou chose {user} and the computer chose {computer}. You won!\n' # Return a win message with the choices
    
    return f'\nYou chose {user} and the computer chose {computer}. You lose!\n' # Return a lose message with the choices
    
def is_win(player, opponent):
    # This function returns true if the player wins and false otherwise
    # r > s , s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
            return True # Return true if the player's choice beats the opponent's choice
    return False # Otherwise, return false

print("\nWelcome to the Rock, Paper, Scissors game!") # Print a welcome message when the game starts

while True: # Start an infinite loop to play multiple rounds
    print(play()) # Call the play function to play a round
    play_again = input("\nWould you like to play another round? (yes/no): ") # Ask the user politely if they want to play again
    if play_again.lower() != 'yes': # If they don't want to play again, break out of the loop
        break

print("\nThank you for playing the Rock, Paper, Scissors game! Have a nice day!") # Print a farewell message when the game ends
