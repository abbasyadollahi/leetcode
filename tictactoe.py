class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """

        self.size = n
        self.board = [['_']*n for i in range(n)]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 winse
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """

        self.board[row][col] = 'x' if player == 1 else 'o'

        for i in range(self.size):
            if '_' not in self.board[i] and len(set(self.board[i])) == 1:
                if self.board[i][0] == 'x':
                    print('Player 1 won.1')
                    return 1
                elif self.board[i][0] == 'o':
                    print('Player 1 won.1')
                    return 2

            col_match = []
            for j in range(self.size):
                col_match.append(self.board[j][i])

            if '_' not in col_match and len(set(col_match)) == 1:
                print(col_match)
                if col_match[0] == 'x':
                    print('Player 1 won.1')
                    return 1
                elif col_match[0] == 'o':
                    print('Player 1 won.1')
                    return 2

            diag_match = []
            diag_match.append(self.board[i][i])

        if '_' not in diag_match and len(set(diag_match)) == 1:
            if diag_match[0] == 'x':
                print('Player 1 won.1')
                return 1
            elif diag_match[0] == 'o':
                print('Player 1 won.1')
                return 2

        print('Next turn.')
        for i in range(self.size):
            print(self.board[i])

        return
