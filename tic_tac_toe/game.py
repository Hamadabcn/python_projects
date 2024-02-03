import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

# Define a class for the tic-tac-toe game logic
class TicTacToe():
    def __init__(self):
        self.board = self.make_board() # Initialize the board as a list of empty spaces
        self.current_winner = None # Initialize the current winner as None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)] # Return a list of 9 empty spaces

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]: # Loop through the board in 3-row chunks
            print('| ' + ' | '.join(row) + ' |') # Print each row with separators

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)] # Create a list of lists with numbers from 0 to 8
        for row in number_board: # Loop through the number board
            print('| ' + ' | '.join(row) + ' |') # Print each row with separators

    def make_move(self, square, letter):
        if self.board[square] == ' ': # If the chosen square is empty
            self.board[square] = letter # Assign the letter to the square
            if self.winner(square, letter): # Check if the move is a winning move
                self.current_winner = letter # Update the current winner
            return True # Return True to indicate a valid move
        return False # Return False to indicate an invalid move

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3) # Get the row index of the square
        row = self.board[row_ind*3:(row_ind+1)*3] # Get the row as a sublist of the board
        # print('row', row)
        if all([s == letter for s in row]): # If all the squares in the row have the same letter
            return True # Return True to indicate a win
        col_ind = square % 3 # Get the column index of the square
        column = [self.board[col_ind+i*3] for i in range(3)] # Get the column as a sublist of the board
        # print('col', column)
        if all([s == letter for s in column]): # If all the squares in the column have the same letter
            return True # Return True to indicate a win
        if square % 2 == 0: # If the square is on a diagonal (even index)
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # Get the first diagonal as a sublist of the board
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]): # If all the squares in the first diagonal have the same letter
                return True # Return True to indicate a win
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # Get the second diagonal as a sublist of the board
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]): # If all the squares in the second diagonal have the same letter
                return True # Return True to indicate a win
        return False # Return False to indicate no win

    def empty_squares(self):
        return ' ' in self.board # Return True if there is an empty space in the board

    def num_empty_squares(self):
        return self.board.count(' ') # Return the number of empty spaces in the board

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "] # Return a list of indices of empty spaces


# Define a function for the game loop
def play(game, x_player, o_player, print_game=True):

    if print_game: 
        game.print_board_nums() # Print the board with numbers for reference

    letter = 'X' # Initialize the letter as X (first player)
    while game.empty_squares(): # While there are still empty squares on the board
        if letter == 'O': 
            square = o_player.get_move(game) # Get the move from the O player (human or computer)
        else:
            square = x_player.get_move(game) # Get the move from the X player (human or computer)
        if game.make_move(square, letter): # If the move is valid

            if print_game:
                print(letter + ' makes a move to square {}\n'.format(square)) # Print the move
                game.print_board() # Print the board
                print('')

            if game.current_winner: # If there is a winner
                if print_game:
                    print(letter + ' wins!\n') # Print the winner
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(0.4) # Pause for 0.4 seconds

    if print_game:
        print('It\'s a tie!\n') # Print a tie message

# this is the classical way to play tic_tac_toe against an AI that will never lose, but if you play the RandomComputerPlayer its a easy version

#if __name__ == '__main__':
#    x_player = HumanPlayer('X') # Create an instance of the smart computer player with X symbol (impossible version)
#    #x_player = RandomComputerPlayer('X') # Create an instance of the random computer player with X symbol (easy version)
#    o_player = SmartComputerPlayer('O') # Create an instance of the human player with O symbol
#    t = TicTacToe() # Create an instance of the tic-tac-toe game
#    play(t, x_player, o_player, print_game=True) # Start the game loop with printing enabled

# the version on the top will let you play the smart_computer yourself (but you have to uncomment it and comment the one on the bottom)

# another way to make the RandomComputerPlayer play the SmartComputerPlayer (1000 times or as many as you want) and he will not lose 

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for i in range(10):  # you can add as many iterations as you want the computer will never lose (but remember to change it in the print)
        #x_player = HumanPlayer('X') # Create an instance of the human_player with X symbol (us)
        x_player = RandomComputerPlayer('X') # Create an instance of the random computer player with X symbol (easy version)
        o_player = SmartComputerPlayer('O') # Create an instance of the smart_computer_player with O symbol (impossible to win)
        t = TicTacToe() # Create an instance of the tic-tac-toe game
        result = play(t, x_player, o_player, print_game=False) # Start the game loop with printing enabled
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1
            
    print(f'After 10 iterations, we see {x_wins} X wins, we see {o_wins} O wins, {ties} ties')
    