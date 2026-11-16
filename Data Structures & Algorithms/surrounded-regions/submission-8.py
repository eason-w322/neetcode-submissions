class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] == "X" or board[r][c] == "S":
                return
            board[r][c] = "S"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(row):
            for j in (0, col - 1):
                if board[i][j] == "O":
                    dfs(i, j)
        
        for i in (0, row - 1):
            for j in range(col):
                if board[i][j] == "O":
                    dfs(i, j)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"
            








