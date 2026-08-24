class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != "O":
                return
            board[r][c] = "Y"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in [0, row-1]:
            for j in range(0, col):
                if board[i][j] == "O":
                    dfs(i, j)
        
        for j in [0, col-1]:
            for i in range(0, row):
                if board[i][j] == "O":
                    dfs(i, j)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Y":
                    board[i][j] = "O"
















