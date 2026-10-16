class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def dfs(i, j, k):

            if k == len(word):
                return True

            if i < 0 or i >= row or j < 0 or j >= col or board[i][j] == "*":
                return False
            

            if board[i][j] != word[k]:
                return False
            
            board[i][j] = "*"
            result =  dfs(i + 1,j, k + 1) or dfs(i -1 , j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            return result
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False
        

            

            