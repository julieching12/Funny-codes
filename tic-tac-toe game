"""this program is to pretends how to play tic-tac-toe between the computer and the user(e.g. you). The computer plays
the game using 'X's, while the user (you) play the game using 'O's. The computer makes first move and puts 'X' in the
middle of the board, then user makes first move by inputting a number between 1 and 9. Two players rotate to input
number into the board until one side wins."""

from random import randrange

#we define the board to be be initialized when executing the program
board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print(f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print(f"|       |       |       |")
    print(f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |")
    print(f"|       |       |       |")
    print("+-------+-------+-------+")
    print(f"|       |       |       |")
    print(f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |")
    print(f"|       |       |       |")
    print("+-------+-------+-------+")
#display_board(board)

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move! The number must be between 1 and 9.")
                continue

            # after getting valid number, go ahead to below getting row and col index
            # Map number 1-9 to 2D array row and column
            row = (move - 1) // 3
            print(row)
            col = (move - 1) % 3
            print(col)

            if board[row][col] in ['X', 'O']:
                print("That square is already occupied! Try again")
                continue

            # when getting any move not in ['X', 'O'], then input it with 'O' as user move
            board[row][col] = 'O'
            break

        except ValueError:
            print("Invalid input! Please enter an integer.")

#enter_move(board)
#display_board(board)

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X', 'O']:
                free_fields.append((r, c))
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status to check if
    # the player using 'O's or 'X's has won the game

    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True
        if board[0][i] == board[1][i] == board[2][i] == sign:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True

    return False  #any other situation all return False

#print(victory_for(board, 'O'))  #this only return one time after one input, how to make it loop when execution


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    print(free_fields)
    if free_fields:
        # Pick a random tuple index from available open spaces
        index = randrange(len(free_fields))
        #print(len(free_fields))   #8
        #print(randrange(len(free_fields)))  #5
        #print(index)  #3  #output of randrange not necessary equals to index
        row, col = free_fields[index]
        print(row, col)
        #row, col = random.choice(free_fields)  #if import random
        board[row][col] = 'X'

#draw_move(board)
#display_board(board)

# --- Main Game Loop Execution --- #execution has separate code, while previous only defining definitions
# Initialize the board with numbers 1 to 9
board = [
    [1, 2, 3],
    [4, 'X', 6],  # First move belongs to computer: 'X' in the middle (5)
    [7, 8, 9]
]

# The computer always puts its first 'X' in the middle of the board (square 5)
board[1][1] = 'X'

display_board(board)

while True:  #rotate my move + your move, each time check for victory_for status(who wons), and if free_fields left(tie)
    # 1. User's turn
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):   #here specify the sign value, 'O' if you won
        print("You won!")
        break
    if not make_list_of_free_fields(board):
        print(make_list_of_free_fields(board))
        print("It's a tie!")
        break

    # 2. Computer's turn
    print("Computer makes a move...")
    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):  #here specify the sign value, 'X' if computer won
        print("Computer wins!")
        break
    if not make_list_of_free_fields(board):
        print(make_list_of_free_fields(board))  #when free_fields list is [], It's a tie!
        print("It's a tie!")
        break


# An example session with the program may look as follows:
#
# +-------+-------+-------+
# |       |       |       |
# |   1   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Enter your move: 1
# +-------+-------+-------+
# |       |       |       |
# |   O   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Enter your move: 8
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Enter your move: 4
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# Enter your move: 7
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# You won!
