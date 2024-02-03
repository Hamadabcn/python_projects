import random
import re

# main changes from minesweeper.py
# added a prompt to keep playing
# added error handling to everything
# added to choose the number of bombs at the beginning of the game makes it harder
# added important comments

# Define the Board class to represent the Minesweeper game
class Board:
    def __init__(self, dim_size, num_bombs):
        # Check for valid dimensions and number of bombs
        if dim_size <= 0:
            raise ValueError("Board dimensions must be greater than 0.")
        if num_bombs >= dim_size ** 2:
            raise ValueError("Number of bombs cannot exceed the total number of cells.")

        # Initialize board attributes
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()

    def make_new_board(self):
        # Create a new game board with empty cells
        board = [[' ' for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size ** 2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue

            board[row][col] = '*'  # Plant a bomb
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        # Calculate and assign values (number of neighboring bombs) to non-bomb cells
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        # Count the number of neighboring bombs for a given cell
        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1
        return num_neighboring_bombs

    def dig(self, row, col):
        # Perform the dig operation at the specified cell
        if (row, col) in self.dug:
            return True

        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False  # Bomb hit
        elif self.board[row][col] > 0:
            return True  # Cell has neighboring bombs

        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1):
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        return True

    def __str__(self):
        # Generate a string representation of the game board
        visible_board = [[' ' for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        string_rep = ''
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(len(max(columns, key=len)))

        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % col)
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % col)
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-' * str_len + '\n' + string_rep + '-' * str_len
        return string_rep

def play(dim_size=10, num_bombs=None):
    if num_bombs is None:
        num_bombs = int(input("\nEnter the number of bombs (default is 10): ") or 10)

    try:
        board = Board(dim_size, num_bombs)
    except ValueError as e:
        print(f"Error: {e}")
        return

    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(r'[,]\s*', input("Where would you like to dig? Input as row,col: "))
        if len(user_input) != 2:
            print("Invalid input format. Please use 'row, col' format.")
            continue

        try:
            row, col = int(user_input[0]), int(user_input[1])
            if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
                print("Invalid location. Try again.")
                continue

            safe = board.dig(row, col)
            if not safe:
                break
        except ValueError:
            print("\nInvalid input. Please enter valid numbers for row and column.\n")

    if safe:
        print("\nCONGRATULATIONS!!!! YOU ARE VICTORIOUS!\n")
    else:
        print("\nSORRY GAME OVER :(\n")
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    play_again = True
    while play_again:
        play()
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input != 'yes':
            play_again = False
