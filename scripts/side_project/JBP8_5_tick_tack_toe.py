import os


def draw(board):
    for row in board:
        print(" | ".join(map(str, row)))


def check_for_win(board, shape):
    for i in range(3):
        # check for rows
        if board[i][0] == shape and board[i][1] == shape and board[i][2] == shape:
            return shape
        # check for columns
        if board[0][i] == shape and board[1][i] == shape and board[2][i] == shape:
            return shape

    # check for diagonal1
    if board[0][0] == shape and board[1][1] == shape and board[2][2] == shape:
        return shape
    # check for diagonal2
    if board[0][2] == shape and board[1][1] == shape and board[2][0] == shape:
        return shape


board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
turns = 0

while True:
    turns += 1
    draw(board)

    shape = "X" if turns % 2 == 0 else "O"

    move = input(f"[{shape}] :   ")
    x = int(move[0]) - 1
    y = int(move[1]) - 1

    if board[y][x] != 0:
        print("Cannot make a move on that square!")
        continue

    board[y][x] = shape

    if check_for_win(board, shape) is not None:
        print(f"\n'{shape}' has won the match!")
        draw(board)
        break

    if turns == 9:
        print("\nDraw!")
        draw(board)
        break

    os.system("cls")
