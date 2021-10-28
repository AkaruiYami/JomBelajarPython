"""
    Game Tick Tack Toe v2 in Terminal
    
    2 Players Game
    
    - Start with O
    - The first player able to create 3 consucutive line of their shape, win
    - The game end up draw if no player able to create 3 consucutive line after the board is full
    - User need to input coordinate of the box -> n
    
    Example:
        Input:
            4
        Output:
            | 1  | 2  |  3 |
            | O  | 5  |  6 |
            | 7  | 8  |  9 |
            
        Input:
            5
        Output:
            | 1  | 2  |  3 |
            | O  | X  |  6 |
            | 7  | 8  |  9 |
"""
import os

if os.name == "posix":
    clear_cmd = "clear"
else:
    clear_cmd = "cls"

board = "1|2|3/4|5|6/7|8|9"
turns = 1
running = True

def print_board(board):
    for row in board.split("/"):
        print(row)


def check_for_win(plr, board):
    t = lambda cell: (cell - 1) * 2

    if board[t(1)] + board[t(5)] + board[t(9)] == plr * 3:
        return plr
    if board[t(3)] + board[t(5)] + board[t(7)] == plr * 3:
        return plr
    for i in range(3):
        if board[t(1 + i * 3)] + board[t(2 + i * 3)] + board[t(3 + i * 3)] == plr * 3:
            return plr
        if board[t(1 + i)] + board[t(4 + i)] + board[t(7 + i)] == plr * 3:
            return plr
    return None


if __name__ == "__main__":
    while running:
        plr = "X" if turns%2==0 else "O"
        print(f"{plr}'s Turn")
        print_board(board)
        move = input(" $  ")
        os.system(clear_cmd)

        if move in board:
            board = board.replace(move, plr)
            plr_win = check_for_win(plr, board)
            if plr_win or turns == 9:
                print(f"Player '{plr}' has won the game!") if plr_win else print("DRAW!")
                print_board(board)
                running = False
            turns += 1
        else:
            print("Invalid move! Try again.")