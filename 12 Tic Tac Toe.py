import random


def print_board(board):
    print("\n".join([" | ".join(row) for row in board]))


def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # Row 1
        [board[1][0], board[1][1], board[1][2]],  # Row 2
        [board[2][0], board[2][1], board[2][2]],  # Row 3
        [board[0][0], board[1][0], board[2][0]],  # Column 1
        [board[0][1], board[1][1], board[2][1]],  # Column 2
        [board[0][2], board[1][2], board[2][2]],  # Column 3
        [board[0][0], board[1][1], board[2][2]],  # Diagonal \
        [board[2][0], board[1][1], board[0][2]]  # Diagonal /
    ]
    return [player, player, player] in win_conditions


def check_full(board):
    return all(cell != ' ' for row in board for cell in row)


def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("Cell already taken, try again.")
        except (ValueError, IndexError):
            print("Invalid input, please enter a number between 1 and 9.")


def computer_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    row, col = random.choice(empty_cells)
    board[row][col] = 'O'


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    for turn in range(9):
        if turn % 2 == 0:
            player_move(board)
        else:
            computer_move(board)
        print_board(board)

        if check_win(board, 'X'):
            print("Congratulations! You win!")
            break
        elif check_win(board, 'O'):
            print("Computer wins! Better luck next time.")
            break
        elif check_full(board):
            print("It's a draw!")
            break


tic_tac_toe()