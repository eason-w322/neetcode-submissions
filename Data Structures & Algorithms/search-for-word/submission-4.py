class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def dfs(i, j, word):

            if not word:
                return True

            if i < 0 or i >= row or j < 0 or j >= col or board[i][j] == "*":
                return False
            

            if board[i][j] != word[0]:
                return False
            
            board[i][j] = "*"
            result =  dfs(i + 1,j, word[1:]) or dfs(i -1 , j, word[1:]) or dfs(i, j + 1, word[1:]) or dfs(i, j - 1, word[1:])
            board[i][j] = word[0]
            return result
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if dfs(i, j, word):
                        return True
        
        return False
        

            

            