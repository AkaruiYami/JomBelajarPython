"""
    Game Tick Tack Toe in Terminal
    
    2 Players Game
    
    - Start with O
    - The first player able to create 3 consucutive line of their shape, win
    - The game end up draw if no player able to create 3 consucutive line after the board is full
    - User need to input coordinate of the box -> xy
    
    Example:
        Input:
            12
        Output:
            |   |   |   |
            | O |   |   |
            |   |   |   |
            
        Input:
            22
        Output:
            |   |   |   |
            | O | X |   |
            |   |   |   |
"""
import os

board_data = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
turns = 0


if os.name == "posix":
    clear_cmd = "clear"
else:
    clear_cmd = "cls"


def draw_board(board_data):
    for row in board_data:
        print(" | ".join(row))


def check_for_win(board_data, player):
    for i in range(3):
        # check for each row
        if (
            board_data[i][0] == player
            and board_data[i][1] == player
            and board_data[i][2] == player
        ):
            return player
        # check for each column
        if (
            board_data[0][i] == player
            and board_data[1][i] == player
            and board_data[2][i] == player
        ):
            return player

    if (
        board_data[0][0] == player
        and board_data[1][1] == player
        and board_data[2][2] == player
    ):
        return player

    if (
        board_data[0][2] == player
        and board_data[1][1] == player
        and board_data[2][0] == player
    ):
        return player


os.system(clear_cmd)
while True:
    draw_board(board_data)
    player = "O" if turns % 2 == 0 else "X"

    player_move = input(f"[{player}] :   ")
    x = int(player_move[0]) - 1
    y = int(player_move[1]) - 1

    if board_data[y][x] != "-":
        print("Cannot move at that box!")
        continue

    board_data[y][x] = player

    if check_for_win(board_data, player):
        print(f"\n{player} won the game!")
        draw_board(board_data)
        break

    cell_data = board_data[0] + board_data[1] + board_data[2]
    if "-" not in cell_data:
        print("\nDraw!")
        draw_board(board_data)
        break

    turns += 1
    os.system(clear_cmd)
