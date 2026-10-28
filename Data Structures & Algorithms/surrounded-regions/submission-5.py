class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])

        def dfs1(i, j):
            if i < 0 or i >= row or j < 0 or j >= col or board[i][j] == "X" or board[i][j] == "Y":
                return

            board[i][j] = "Y"
            dfs1(i + 1, j)
            dfs1(i - 1, j)
            dfs1(i, j + 1)
            dfs1(i, j - 1)
        
        for i in range(row):
            for j in (0, col - 1):
                if board[i][j] == "O":
                    dfs1(i, j)
        
        for j in range(col):
            for i in (0, row - 1):
                if board[i][j] == "O":
                    dfs1(i, j)
        
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == "Y":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"













