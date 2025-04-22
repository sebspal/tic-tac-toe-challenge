class Match:
    def __init__(self, match_id, board=None, turn='X', state='ongoing'):
        self.match_id = match_id
        self.board = board or [' '] * 9
        self.turn = turn
        self.state = state

    def make_move(self, player, x, y):
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
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                self.state = f'{self.board[combo[0]]} wins'
                return
        if ' ' not in self.board:
            self.state = 'draw'
        else:
            self.state = 'ongoing'
