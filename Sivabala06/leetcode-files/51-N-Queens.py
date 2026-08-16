class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def safe(row, col):

            # Same row
            for i in range(col):
                if board[row][i] == "Q":
                    return False

            # Upper-left diagonal
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Lower-left diagonal
            i = row + 1
            j = col - 1
            while i < n and j >= 0:
                if board[i][j] == "Q":
                    return False
                i += 1
                j -= 1

            return True

        def solve(col):

            # All columns filled
            if col == n:
                res.append(["".join(row) for row in board])
                return

            # Try every row in this column
            for row in range(n):

                if safe(row, col):

                    # CHOICE
                    board[row][col] = "Q"

                    # EXPLORE
                    solve(col + 1)

                    # BACKTRACK / UNDO
                    board[row][col] = "."

        solve(0)

        return res