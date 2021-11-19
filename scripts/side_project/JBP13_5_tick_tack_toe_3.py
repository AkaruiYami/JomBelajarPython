import os
import time


class Board:
    def __init__(self):
        self.cells = {i: str(i) for i in range(1, 10)}

    def render(self):
        for i, cell in self.cells.items():
            print(f"[{cell}]", end="")
            if i % 3 == 0:
                print()

    def update_cell(self, cell_index, player_shape):
        if self.cells[cell_index].isdecimal():
            self.cells[cell_index] = player_shape
            return True
        print("Cannot move to that space! Try again.")
        time.sleep(1)
        return False


class Game:
    def __init__(self):
        self.turns = 0
        self.board = Board()

    def get_input(self):
        _input = input("$  ")
        if _input.lower() in ["q", "quit", "exit"]:
            self.running = False
            return -1
        elif _input.isdecimal():
            return int(_input)
        else:
            print("Invalid Input!")
            return 0

    def run(self):
        self.running = True
        self.turns += 1
        while self.running:
            self.update()
        self.board.render()

    def update(self):
        self._clear_terminal()
        self.board.render()
        _turn = "X" if self.turns % 2 == 0 else "O"
        print(f"Turn {_turn}")
        _input = self.get_input()
        if _input < 0:
            return
        if self.board.update_cell(_input, _turn):
            if self._check_for_win():
                self._end_game(_turn)
            self.turns += 1
            if self.turns > 9:
                self._end_game(None)

    def _check_for_win(self):
        _cells = self.board.cells
        if len(set([_cells[1], _cells[5], _cells[9]])) == 1:
            return True
        if len(set([_cells[3], _cells[5], _cells[7]])) == 1:
            return True

        for i in range(3):
            if len(set([_cells[1 + i * 3], _cells[2 + i * 3], _cells[3 + i * 3]])) == 1:
                return True
            if len(set([_cells[1 + i], _cells[4 + i], _cells[7 + i]])) == 1:
                return True

        return False

    def _end_game(self, winner):
        if winner:
            print(f"{winner} has won the game!")
        else:
            print("Draw!")
        self.running = False

    def _clear_terminal(self):
        if os.name == "nt":
            _command = "cls"
        else:
            _command = "clear"
        os.system(_command)


if __name__ == "__main__":
    game = Game()
    game.run()
