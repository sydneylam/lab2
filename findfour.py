'''

This is the findfour module.
It prompts two users to play the game find four with each other, where user 1 is assigned "x" and user 2 is assigned "o"
A user wins if they get 4 of their "chips" in a row either horizontally or vertically

Authors: Sydney and Aditya
'''


# no imports

def main():

    # display
    print("Welcome to Find Four!")
    print("---------------------")

    height = int(input("Enter height of board (rows): "))

    # Verifying the user's height input
    while height < 4:
        print("Error: height must be at least 4!")
        height = int(input("Enter height of board (rows): "))
    while height > 25:
        print("Error: height can be at most 25!")
        height = int(input("Enter height of board (rows): "))

    width = int(input("Enter width of board (columns): "))

    # Verifying the user's width input
    while width < 4:
        print("Error: width must be at least 4!")
        width = int(input("Enter width of board (columns): "))
    while width > 25:
        print("Error: width can be at most 25!")
        width = int(input("Enter width of board (columns): "))

    # getting and printing the initial board
    board = get_initial_board(height, width)

    # board[height - 1] is the bottom row printed
    p1rows = [height for x in range(width)]
    p2rows = [height for y in range(width)]

    print_board(board)
    print()
    print("Player 1: x")
    print("Player 2: o")
    print()

    p1chip = "x"
    p2chip = "o"

    # main loop that runs throughout the game
    while True:
        p1Column = input("Player 1 - Select a Column: ")

        # verifying user input for negative numbers or random chars
        while p1Column.isnumeric() == False:
            if p1Column[0] == "-":
                print("Error: no such column!")
            else:
                print("Error: not a number!")
            p1Column = input("Player 1 - Select a Column: ")

        p1Column = int(p1Column)

        # verifying that the column exists in our board
        while p1Column > len(board[0]) - 1:
            print("Error: no such column!")
            p1Column = int(input("Player 1 - Select a Column: "))

        # inserting the chip and printing the board
        row_landed_on = insert_chip(board, p1Column, p1chip)
        print_board(board)
        print()
        # updating the row value
        p1rows[p1Column] -= 1

        # check if the game is now won by either player or a draw after each move
        if is_win_state(p1chip, board, row_landed_on, p1Column):
            print("Player 1 won the game!")
            break

        if is_board_full(board):
            print("Draw game! Players tied.")
            break

        p2Column = input("Player 2 - Select a Column: ")

        # verifying user input for negative numbers or random chars
        while p2Column.isnumeric() == False:
            if p2Column[0] == "-":
                print("Error: no such column!")
            else:
                print("Error: not a number!")
            p2Column = input("Player 2 - Select a Column: ")

        p2Column = int(p2Column)

        # verifying the selected column exists in our board
        while p2Column > len(board[0]) - 1:
            print("Error: no such column!")
            p2Column = int(input("Player 2 - Select a Column: "))

        # inserting the chip and printing the board
        row_landed_on2 = insert_chip(board, p2Column, p2chip)
        print_board(board)
        print()

        # update our row variable
        p2rows[p2Column] -= 1

        # check if the game is now won by either player or a draw after each move
        if is_win_state(p2chip, board, row_landed_on2, p2Column):
            print("Player 2 won the game!")
            break

        if is_board_full(board):
            print("Draw game! Players tied.")
            break


def get_initial_board(height, width):
    # initializing a 2-d array filled with "." based on the height and width
    board = ["."] * height
    for index, _ in enumerate(board):
        board[index] = ["."] * width

    return board


def print_board(board):
    width = len(board[0])
    print(" " + "_" * (width * 2 - 1) + " ")  # top border
    for i in range(len(board)-1, -1, -1):
        print("|", end="")
        for j in range(len(board[i])):  # columns of the board
            if j == len(board[i]) - 1:
                print(board[i][j], end="|\n")
            else:
                print(board[i][j], end=" ")
    print(" " + "-" * (width * 2 - 1))  # bottom border


def insert_chip(board, column, chip):
    # looping in range of the length, stopping at 0, -1 each step
    for i in range(0, len(board)):
        # looping until we see an empty spot
        if board[i][column] == ".":
            board[i][column] = chip
            return i
        else:
            continue


def is_win_state(chip, board, row, column):
    # checking horizontal win-state
    counter = 0
    num_chips = 0
    # looping through every element in the given row
    while counter < len(board[0]):
        if board[row][counter] == chip:
            num_chips += 1
        if num_chips >= 4:
            return True
        if num_chips > 0 and board[row][counter] != chip:
            num_chips = 0
        counter += 1

    # vertical
    counter1 = 0
    num_chips1 = 0
    # looping through every element in the given column
    while counter1 < len(board):
        if board[counter1][column] == chip:
            num_chips1 += 1
        if num_chips1 >= 4:
            return True
        if num_chips1 > 0 and board[counter1][column] != chip:
            num_chips1 = 0
        counter1 += 1

    # checking if there is either a horizontal or vertical win state
    if num_chips1 >= 4:
        return True
    elif num_chips >= 4:
        return True
    else:
        return False


def is_board_full(board):
    # using a nested loop to check if there are any "." throughout the whole 2-d array
    for j in range(len(board)):
        for i in range(len(board[0])):
            if board[j][i] == ".":
                return False
    else:
        return True


# dunder
if __name__ == "__main__":
    main()