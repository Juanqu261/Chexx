import chess


# Piece values
PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0
}

class MinimaxBot:
    def __init__(self):
        self.board = chess.Board()

    def evaluate_board(self):
        '''Simple evaluation based on pieces:
        Evaluate the position as white by summing the values of white pieces
        and subtracting black pieces values.

        returns:
            - evaluation (int): > 0, white is winning.
                                = 0, the game is drawing.
                                < 0, black is winning.
        '''
        evaluation = 0
        for piece_type in PIECE_VALUES.keys():
            evaluation += len(self.board.pieces(piece_type, chess.WHITE)) * PIECE_VALUES[piece_type]
            evaluation -= len(self.board.pieces(piece_type, chess.BLACK)) * PIECE_VALUES[piece_type]
        return evaluation


    def minimax(self, depth, is_maximizing):
        '''Takes the best possible evaluation by looking what would happen after a move according to 'evaluate_board'.

        parameters:
            - depth (int) = Indicates how many moves ahead will be checked.
            - is_maximizing (bool) = True for white and False for black.
        '''
        if self.board.is_game_over():
            return self.evaluate_board()

        if depth == 0:
            return self.evaluate_board()

        legal_moves = list(self.board.legal_moves)

        if is_maximizing:
            max_eval = -float('inf')
            # Consider all legal moves
            for move in legal_moves:
                self.board.push(move)
                # After making the move evaluates the new position (recursively)
                eval = self.minimax(depth - 1, False)
                # Takes the move back
                self.board.pop()
                # If the evaluation is better than the evaluation in the previous move,
                # then this is the new best evaluation
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in legal_moves:
                self.board.push(move)
                eval = self.minimax(depth - 1, True)
                self.board.pop()
                min_eval = min(min_eval, eval)
            return min_eval

    def best_move(self, depth):
        '''Choose the best move according to 'minimax'.

        parameters:
            - depth (int): How many moves ahead are being evaluated.
        
        returns:
            - best_move (chess.Move): Best move in the position.
        '''
        best_move = None

        # Check if its  Whites or Blacks turn
        if self.board.turn == chess.WHITE:
            best_value = -float('inf')
            for move in list(self.board.legal_moves):
                self.board.push(move)
                board_value = self.minimax(depth - 1, False)
                self.board.pop()
                if board_value > best_value:
                    best_value = board_value
                    best_move = move
        else:  # Black's turn, minimizing player
            best_value = float('inf')
            for move in list(self.board.legal_moves):
                self.board.push(move)
                board_value = self.minimax(depth - 1, True)
                self.board.pop()
                if board_value < best_value:
                    best_value = board_value
                    best_move = move

        return best_move


    def play_game(self, depth=2):
        # Play until the game ends
        while not self.board.is_game_over():
            move = self.best_move(depth)
            print(f"MinimaxBot made move: {move}")
            self.board.push(move)
            print(self.board)

        print("Game over:", self.board.result())


if __name__ == "__main__":
    bot = MinimaxBot()
    bot.play_game(depth=2)
