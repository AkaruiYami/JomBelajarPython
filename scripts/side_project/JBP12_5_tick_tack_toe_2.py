import os

board = "1|2|3/4|5|6/7|8|9"
turns = 1
running = True


def print_board(board):
    for row in board.split("/"):
        print("\t" + row)


def check_for_win(plr, board):
    t = lambda point: (point - 1) * 2
    if board[t(1)] + board[t(5)] + board[t(9)] == plr * 3:
        return plr
    if board[t(3)] + board[t(5)] + board[t(7)] == plr * 3:
        return plr
    for i in range(3):
        if board[t(1 + i * 3)] + board[t(2 + i * 3)] + board[t(3 + i * 3)] == plr * 3:
            return plr
        if board[t(1 + i)] + board[t(4 + i)] + board[t(7 + i)] == plr * 3:
            return plr


if __name__ == "__main__":
    while running:
        print_board(board)
        plr = "X" if turns % 2 == 0 else "O"
        plr_input = input(" $  ")
        os.system("cls")

        if plr_input not in board:
            if plr_input.lower() == "q":
                running = False
            else:
                print("Can't move on that space! Try again.")
            continue

        board = board.replace(plr_input, plr)

        if check_for_win(plr, board):
            print(f"Player '{plr}' has won the game!")
            running = False
        elif turns == 9:
            print("DRAW!!!")
            running = False

        turns += 1
    else:
        print("#" * 24)
        print_board(board)
