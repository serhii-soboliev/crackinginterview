class TicTacToe:

    def result(self, moves):

        win_combinations = [
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            [[0, 0], [1, 1], [2, 2]],
            [[2, 0], [1, 1], [0, 2]],
        ]

        a_moves = []
        b_moves = []
        for i in range(len(moves)):
            if i % 2 == 0:
                a_moves.append(moves[i])
            else:
                b_moves.append(moves[i])

        for win_combination in win_combinations:
            if all(elem in a_moves for elem in win_combination):
                return "A"
            if all(elem in b_moves for elem in win_combination):
                return "B"

        return "Draw" if len(moves) == 9 else "Pending"
