class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])

        memo = {}
        def dfs(r, c, current_val):
            if r < 0 or r >= row or c < 0 or c >= col or matrix[r][c] <= current_val:
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            result = 1 + max(dfs(r + 1, c, matrix[r][c]),
                           dfs(r - 1, c, matrix[r][c]),
                           dfs(r, c + 1, matrix[r][c]),
                           dfs(r, c - 1, matrix[r][c])
            )
            memo[(r, c)] = result
            return result

        longest = 0
        for i in range(row):
            for j in range(col):
                longest = max(longest, dfs(i, j, -1))
        
        return longest
