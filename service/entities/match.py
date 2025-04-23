class Match:
    def __init__(self, match_id, board=None, turn='X', state='ongoing'):
        self.match_id = match_id
        self.board = board or [' '] * 9
        self.turn = turn
        self.state = state

    def make_move(self, player, x, y):
        if self.state != 'ongoing':
            raise ValueError("Game is already over")

        if player not in ('X', 'O'):
            raise ValueError("Invalid player")

        if player != self.turn:
            raise ValueError(f"It's {self.turn}'s turn")

        if not (1 <= x <= 3) or not (1 <= y <= 3):
            raise ValueError("Coordinates must be between 1 and 3")

        index = (y - 1) * 3 + (x - 1)
        if self.board[index] != ' ':
            raise ValueError("Square already occupied")

        self.board[index] = player
        self.turn = 'O' if player == 'X' else 'X'
        self.check_game_status()

    def check_game_status(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                self.state = f'{self.board[combo[0]]} wins'
                return

        if ' ' not in self.board:
            self.state = 'draw'
