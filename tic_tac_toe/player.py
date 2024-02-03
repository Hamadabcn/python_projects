import math
import random

# Define a base class for players
class Player():
    def __init__(self, letter):
        self.letter = letter # The letter represents the player's symbol on the board

    def get_move(self, game):
        pass # This method will be overridden by subclasses


# Define a subclass for human players
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter) # Call the parent class constructor

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ') # Ask the user for a move
            try:
                val = int(square) # Convert the input to an integer
                if val not in game.available_moves(): # Check if the move is valid
                    raise ValueError # If not, raise an error
                valid_square = True # If yes, exit the loop
            except ValueError: # Catch the error
                print('Invalid square. Try again.') # Print a message and repeat the loop
        return val # Return the move


# Define a subclass for random computer players
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter) # Call the parent class constructor

    def get_move(self, game):
        square = random.choice(game.available_moves()) # Choose a random move from the available moves
        return square # Return the move


# Define a subclass for smart computer players
class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter) # Call the parent class constructor

    def get_move(self, game):
        if len(game.available_moves()) == 9: # If the board is empty
            square = random.choice(game.available_moves()) # Choose a random move
        else: # Otherwise
            square = self.minimax(game, self.letter)['position'] # Use the minimax algorithm to find the optimal move
        return square # Return the move

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player: # If the other player has won the game
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)} # Return a score based on the number of empty squares and the max player
        elif not state.empty_squares(): # If there are no empty squares left
            return {'position': None, 'score': 0} # Return a score of zero

        if player == max_player: # If it is the max player's turn
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else: # If it is the other player's turn
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves(): # For each possible move in the available moves
            state.make_move(possible_move, player) # Make the move on the board
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' ' # Undo the move on the board
            state.current_winner = None 
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']: # If the simulated score is better than the best score so far
                    best = sim_score # Update the best score and position
            else: 
                if sim_score['score'] < best['score']: # If the simulated score is worse than the best score so far
                    best = sim_score # Update the best score and position
        return best # Return the best score and position
